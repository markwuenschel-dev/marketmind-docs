from typing import Any

"""
TaskProtocol: interface for tuning task construction.
"""

class TaskProtocol(Protocol):
    def build(self: Any, spec_hash: str, partition: dict[str, object]) -> 'TaskIR': ...
    def key(self: Any, task_ir: 'TaskIR') -> str: ...
