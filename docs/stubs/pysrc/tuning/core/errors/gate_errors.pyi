from typing import Any

"""
Typed gate evaluation errors.
"""

class GateError(RuntimeError):
    ...
class GateFailedError(GateError):
    def __init__(self: Any, gate_name: str, reason: str) -> None: ...
class GateConfigError(GateError):
    ...
