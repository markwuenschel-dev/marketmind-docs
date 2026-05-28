from typing import Any

"""
task_factory: constructs TaskIR objects from primitive inputs.
"""

def build_task_ir(task_id: str, job_id: str, candidate_id: str, fold: FoldBoundary, params: dict[str, object], feature_hash: str, spec_hash: str, determinism_tier: str = ...) -> TaskIR: ...
