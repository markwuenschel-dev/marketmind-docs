from typing import Any

logger: Any
class SequenceStep(PlanStep):
    STEP_NAME: Any
    STEP_VERSION: Any
    def forbid_backend_imports() -> bool: ...
