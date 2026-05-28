from typing import Any

pd: Any
pl: Any
class CleaningStep(ABC):
    STEP_TYPE: Any
    STEP_VERSION: Any
    def __init__(self: Any, *, spec: CleaningStepSpec, params: BaseModel, registration: Any | None = ...) -> None: ...
    def apply(self: Any, df: Any, *, state: CleaningPipelineState | None = ..., context: CleaningRuntimeContext | None = ...) -> CleaningStepResult: ...
