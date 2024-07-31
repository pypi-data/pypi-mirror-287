import inspect
from collections import OrderedDict
from tempfile import TemporaryDirectory
from typing import Any, Dict

import torch
from hydra.utils import get_class
from openvino.runtime import properties
from optimum.intel.openvino import OVConfig as OVQuantizationConfig  # naming conflict
from optimum.intel.openvino import OVQuantizer

from ...generators.dataset_generator import DatasetGenerator
from ...import_utils import is_accelerate_available, is_torch_distributed_available
from ...task_utils import TEXT_GENERATION_TASKS
from ..base import Backend
from ..transformers_utils import fast_weights_init
from .config import OVConfig
from .utils import TASKS_TO_MODEL_TYPES_TO_OVPIPELINE, TASKS_TO_OVMODEL

if is_accelerate_available():
    from accelerate import Accelerator

if is_torch_distributed_available():
    import torch.distributed


class OVBackend(Backend[OVConfig]):
    NAME: str = "openvino"

    def __init__(self, config: OVConfig) -> None:
        super().__init__(config)

        if self.config.task in TASKS_TO_OVMODEL:
            self.ovmodel_class = get_class(TASKS_TO_OVMODEL[self.config.task])
            self.logger.info(f"\t+ Using OVModel class {self.ovmodel_class.__name__}")
        elif self.config.task in TASKS_TO_MODEL_TYPES_TO_OVPIPELINE:
            if self.config.model_type in TASKS_TO_MODEL_TYPES_TO_OVPIPELINE[self.config.task]:
                self.ovmodel_class = get_class(
                    TASKS_TO_MODEL_TYPES_TO_OVPIPELINE[self.config.task][self.config.model_type]
                )
                self.logger.info(f"\t+ Using OVPipeline class {self.ovmodel_class.__name__}")
            else:
                raise NotImplementedError(
                    f"OVBackend does not support model {self.config.model_type} for task {self.config.task}"
                )
        else:
            raise NotImplementedError(f"OVBackend does not support task {self.config.task}")

        if self.config.inter_op_num_threads is not None:
            self.logger.info(f"\t+ Setting inter_op_num_threads to {self.config.inter_op_num_threads}")
            self.config.openvino_config[properties.inference_num_threads()] = self.config.inter_op_num_threads

    def load(self) -> None:
        self.logger.info("\t+ Creating backend temporary directory")
        self.tmpdir = TemporaryDirectory()

        if self.config.quantization:
            if self.config.no_weights:
                self.logger.info("\t+ Creating no weights AutoModel")
                self.create_no_weights_model()
                self.logger.info("\t+ Loading no weights AutoModel")
                self._load_automodel_with_no_weights()
            else:
                self.logger.info("\t+ Loading pretrained AutoModel")
                self._load_automodel_from_pretrained()
            self.logger.info("\t+ Applying post-training quantization")
            self.quantize_automodel()
            original_model, self.config.model = self.config.model, self.quantized_model
            original_export, self.config.export = self.config.export, False
            self.logger.info("\t+ Loading quantized OVModel")
            self._load_ovmodel_from_pretrained()
            self.config.model, self.config.export = original_model, original_export
        elif self.config.no_weights:
            self.logger.info("\t+ Creating no weights OVModel")
            self.create_no_weights_model()
            self.logger.info("\t+ Loading no weights OVModel")
            self._load_ovmodel_with_no_weights()
        else:
            self.logger.info("\t+ Loading pretrained OVModel")
            self._load_ovmodel_from_pretrained()

        if self.config.reshape:
            static_shapes = {
                key: value
                for key, value in {**self.input_shapes, **self.model_shapes}.items()
                if key in inspect.getfullargspec(self.pretrained_model.reshape).args
            }
            if ("sequence_length" in static_shapes) and ("height" in static_shapes) and ("width" in static_shapes):
                # for vision models, sequence_length is the number of channels
                static_shapes["sequence_length"] = self.model_shapes.get("num_channels")

            self.logger.info(f"\t+ Reshaping model with static shapes: {static_shapes}")
            self.pretrained_model.reshape(**static_shapes)

        if self.config.half:
            self.logger.info("\t+ Converting model to half precision")
            self.pretrained_model.half()

        if self.config.reshape or self.config.half:
            self.logger.info("\t+ Compiling model")
            self.pretrained_model.compile()

        self.tmpdir.cleanup()

    def _load_automodel_from_pretrained(self) -> None:
        self.pretrained_model = self.automodel_loader.from_pretrained(self.config.model, **self.config.model_kwargs)

    def _load_automodel_with_no_weights(self) -> None:
        original_model, self.config.model = self.config.model, self.no_weights_model

        with fast_weights_init():
            self._load_automodel_from_pretrained()

        self.logger.info("\t+ Tying model weights")
        self.pretrained_model.tie_weights()

        self.config.model = original_model

    def _load_ovmodel_from_pretrained(self) -> None:
        self.pretrained_model = self.ovmodel_class.from_pretrained(
            self.config.model,
            export=self.config.export,
            ov_config=self.config.openvino_config,
            device=self.config.device,
            **self.config.model_kwargs,
            **self.ovmodel_kwargs,
        )

    def _load_ovmodel_with_no_weights(self) -> None:
        with fast_weights_init():
            original_model, self.config.model = self.config.model, self.no_weights_model
            original_export, self.config.export = self.config.export, True
            self.logger.info("\t+ Loading no weights OVModel")
            self._load_ovmodel_from_pretrained()
            self.config.export = original_export
            self.config.model = original_model

    @property
    def is_dp_distributed(self) -> bool:
        return is_torch_distributed_available() and torch.distributed.is_initialized()

    @property
    def ovmodel_kwargs(self) -> Dict[str, Any]:
        kwargs = {}

        if self.config.task in TEXT_GENERATION_TASKS:
            kwargs["use_cache"] = self.config.use_cache
            kwargs["use_merged"] = self.config.use_merged

        return kwargs

    def quantize_automodel(self) -> None:
        self.logger.info("\t+ Attempting quantization")
        self.quantized_model = f"{self.tmpdir.name}/quantized_model"
        self.logger.info("\t+ Processing quantization config")
        quantization_config = OVQuantizationConfig(**self.config.quantization_config)
        self.logger.info("\t+ Creating quantizer")
        quantizer = OVQuantizer.from_pretrained(self.pretrained_model, task=self.config.task, seed=self.config.seed)

        if self.config.calibration:
            self.logger.info("\t+ Generating calibration dataset")
            dataset_shapes = {"dataset_size": 1, "sequence_length": 1, **self.model_shapes}
            calibration_dataset = DatasetGenerator(
                task=self.config.task, dataset_shapes=dataset_shapes, model_shapes=self.model_shapes
            )()
            columns_to_be_removed = list(set(calibration_dataset.column_names) - set(quantizer._export_input_names))
            calibration_dataset = calibration_dataset.remove_columns(columns_to_be_removed)
        else:
            calibration_dataset = None

        self.logger.info("\t+ Quantizing model")
        quantizer.quantize(
            save_directory=self.quantized_model,
            quantization_config=quantization_config,
            calibration_dataset=calibration_dataset,
            # TODO: add support for these (maybe)
            remove_unused_columns=True,
            data_collator=None,
            weights_only=False,
            file_name=None,
            batch_size=1,
        )

    def prepare_input_shapes(self, input_shapes: Dict[str, Any]) -> Dict[str, Any]:
        if self.is_dp_distributed:
            if input_shapes["batch_size"] % torch.distributed.get_world_size() != 0:
                raise ValueError(
                    f"Batch size {input_shapes['batch_size']} must be divisible by "
                    f"data parallel world size {torch.distributed.get_world_size()}"
                )
            # distributing batch size across processes
            input_shapes["batch_size"] //= torch.distributed.get_world_size()

        # registering input shapes for usage during model reshaping
        self.input_shapes = input_shapes

        return input_shapes

    def prepare_inputs(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        if self.is_dp_distributed:
            with Accelerator().split_between_processes(inputs=inputs, apply_padding=False) as process_inputs:
                inputs = process_inputs

        return inputs

    def forward(self, inputs: Dict[str, Any], kwargs: Dict[str, Any]) -> OrderedDict:
        return self.pretrained_model.forward(**inputs, **kwargs)

    def prefill(self, inputs: Dict[str, Any], kwargs: Dict[str, Any]) -> OrderedDict:
        return self.pretrained_model.generate(**inputs, **kwargs)

    def generate(self, inputs: Dict[str, Any], kwargs: Dict[str, Any]) -> OrderedDict:
        return self.pretrained_model.generate(**inputs, **kwargs)

    def call(self, inputs: Dict[str, Any], kwargs: Dict[str, Any]) -> OrderedDict:
        return self.pretrained_model(**inputs, **kwargs)
