from typing import Any

"""
PartitionDispatcher: fan out a PartitionPlan into individual task submissions.
"""

TaskSubmitFn: Any
class PartitionDispatcher:
    def dispatch(self: Any, plan: PartitionPlan, submit_fn: TaskSubmitFn, candidate_id: str) -> int: ...
