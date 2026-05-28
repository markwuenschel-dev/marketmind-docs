from typing import Any

logger: Any
KalmanFilter: Any
class MissingValueParams(BaseModel):
    model_config: Any
    method: Literal['forward_fill', 'backward_fill', 'interpolate', 'median', 'kalman'] = ...
    backward_fill: bool = ...
class MissingValueNormalizerStep(CleaningStep):
    ...
