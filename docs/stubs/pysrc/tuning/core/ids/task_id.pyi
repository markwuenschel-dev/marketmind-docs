from typing import Any

"""
Deterministic task ID generation.
"""

def make_task_id(job_id: str, candidate_id: str, fold_index: int) -> str: ...
