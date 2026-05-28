from typing import Any

"""
TaskBuilder: assembles TaskIR objects from search candidates and fold boundaries.
"""

class TaskBuilder:
    def build(self: Any, task_id: str, job_id: str, candidate_id: str, fold: FoldBoundary, params: dict[str, object], feature_hash: str, spec_hash: str, determinism_tier: str = ...) -> TaskIR: ...
