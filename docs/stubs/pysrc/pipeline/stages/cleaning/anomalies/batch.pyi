from typing import Any

class BatchAnomalyParams(BaseModel):
    model_config: Any
    contamination: float = ...
class AnomalyNormalizerStep(CleaningStep):
    ...
