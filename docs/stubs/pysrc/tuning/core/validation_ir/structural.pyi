from typing import Any

"""
Structural IR validation: checks node counts, non-empty fields, type invariants.
"""

class StructuralValidationError(ValueError):
    ...
def validate_search_ir(ir: SearchIR) -> SearchIR: ...
def validate_task_ir(ir: TaskIR) -> TaskIR: ...
