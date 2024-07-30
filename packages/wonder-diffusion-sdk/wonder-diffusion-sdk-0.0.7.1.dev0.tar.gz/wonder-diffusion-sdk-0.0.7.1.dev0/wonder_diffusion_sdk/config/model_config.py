import os

from .lora_config import WonderLoraConfig
from .controlnet_config import WonderControlNetConfig
from .scheduler_config import WonderSchedulerConfig
from ..types.pipeline_type import WonderPipelineType
from ..types.scheduler_type import WonderSchedulerType


class WonderDiffusionModelConfig:

    def __init__(
        self,
        pipeline_type: WonderPipelineType | str,
        pretrained_model_name_or_path: str | os.PathLike = 'models/',
        scheduler_config: WonderSchedulerConfig = None,
        precision: str = 'float16',
        lora_config: WonderLoraConfig = None,
        controlnet_config: WonderControlNetConfig = None,
        # Optimization variables
        use_half_precision_vae: bool = False,
        use_tiny_vae: bool = False,
        fuse_qkv_projections: bool = False,
        use_channels_last: bool = False,
        use_deep_cache: bool = False,
        # Lightning model variables
        use_lightning_model: bool = False,
        lightning_model_step_count: int = 4,

        **kwargs,
    ):
        self.pipeline_type = pipeline_type if type(
            pipeline_type) == WonderPipelineType else WonderPipelineType(pipeline_type)

        self.pretrained_model_name_or_path = pretrained_model_name_or_path
        self.scheduler_config = scheduler_config

        self.precision = precision
        self.use_half_precision_vae = use_half_precision_vae
        self.use_tiny_vae = use_tiny_vae
        self.fuse_qkv_projections = fuse_qkv_projections
        self.use_channels_last = use_channels_last

        self.use_deep_cache = use_deep_cache

        self.use_lightning_model = use_lightning_model
        self.lightning_model_step_count = lightning_model_step_count

        self.lora_config = lora_config
        self.controlnet_config = controlnet_config

        self.kwargs = kwargs

        self.check_controlnet_pipeline_type()
        self.check_vae_optimizations()


    def check_controlnet_pipeline_type(self):
        if self.controlnet_config != None:
            assert self.pipeline_type.is_controlnet(), 'Pipeline type must be a controlnet pipeline type'

    def check_vae_optimizations(self):
        assert not (self.use_half_precision_vae and self.use_tiny_vae), 'Cannot use both half precision and tiny VAE optimizations'