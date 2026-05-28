from typing import Any

"""
Cross-IR compatibility checks: ensure spec versions and hash references are consistent.
"""

class CompatibilityError(ValueError):
    ...
def check_search_validation_compatibility(search: SearchIR, validation: ValidationIR) -> None: ...
def check_search_objective_compatibility(search: SearchIR, objective: ObjectiveIR) -> None: ...
