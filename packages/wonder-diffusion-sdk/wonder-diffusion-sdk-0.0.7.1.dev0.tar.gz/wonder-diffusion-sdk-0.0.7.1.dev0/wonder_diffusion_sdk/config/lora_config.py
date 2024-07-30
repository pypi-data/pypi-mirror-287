import os


class WonderLora:
    """
    Lora model initialization wrapper.

    NOTES:
        - `base_model_name_or_path` and `adapter_name` are required when loading multiple Loras with peft.
    """

    def __init__(
        self,
        path: str | os.PathLike = None,
        weight_name: str = None,
        adapter_name: str = None,
        adapter_weight: float = None,
        base_model_name_or_path: str = None,
    ):
        self.path = path
        self.weight_name = weight_name
        self.adapter_name = adapter_name
        self.adapter_weight = adapter_weight
        self.base_model_name_or_path = base_model_name_or_path


class WonderLoraConfig:
    """
    NOTES:
        - When using peft, both Loras must have the same `base_model_name_or_path`.
    """
    def __init__(
        self,
        loras: list[WonderLora] = [],
        use_peft: bool = False,
        peft_combination_type: str = "dare_linear",
        peft_density: float = 0.5
    ):
        self.loras = loras
        self.use_peft = use_peft
        self.peft_combination_type = peft_combination_type
        self.peft_density = peft_density
