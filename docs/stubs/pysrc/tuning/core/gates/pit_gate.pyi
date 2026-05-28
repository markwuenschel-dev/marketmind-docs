from typing import Any

"""
PIT gate: verify no future data leaked into the candidate's training window.
"""

def passes_pit_gate(task_ir: TaskIR, as_of: datetime) -> tuple[bool, str]: ...
