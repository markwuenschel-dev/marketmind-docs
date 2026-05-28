from typing import Any

"""
JobStateMachine: REGISTERING → RUNNING → COMPLETE / FAILED state transitions.
"""

class JobState(str, Enum):
    REGISTERING: Any
    RUNNING: Any
    COMPLETE: Any
    FAILED: Any
    CANCELLED: Any
class InvalidTransitionError(RuntimeError):
    ...
class JobStateMachine:
    def __init__(self: Any, job_id: str) -> None: ...
    def state(self: Any) -> JobState: ...
    def transition(self: Any, to: JobState) -> None: ...
