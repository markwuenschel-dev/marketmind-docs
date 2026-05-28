from typing import Any

"""
Typed errors for governed execution-assumptions emission.
"""

class ExecutionAssumptionsError(ValueError):
    def __init__(self: Any, message: str, *, details: dict[str, Any] | None = ...) -> None: ...
class ExecutionAssumptionsFieldError(ExecutionAssumptionsError):
    ...
class ExecutionAssumptionsHashError(ExecutionAssumptionsError):
    ...
class ExecutionAssumptionsParityError(ExecutionAssumptionsError):
    ...
