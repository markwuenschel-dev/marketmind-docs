from typing import Any

"""
Deterministic task key generation from job/candidate/fold identifiers.
"""

def make_task_key(job_id: str, candidate_id: str, fold_index: int) -> str: ...
def make_candidate_key(job_id: str, param_hash: str) -> str: ...
