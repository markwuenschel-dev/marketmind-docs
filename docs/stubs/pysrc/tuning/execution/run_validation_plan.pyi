from typing import Any

"""
run_validation_plan: execute cross-validation for a set of candidates.
"""

def run_validation_plan(ir: ValidationIR, candidates: list[dict[str, Any]], context: dict[str, Any]) -> list[dict[str, Any]]: ...
