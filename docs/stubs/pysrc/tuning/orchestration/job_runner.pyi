from typing import Any

"""
JobRunner: top-level coordinator that drives a tuning job from submission to completion.
"""

class JobRunner:
    def run(self: Any, job_id: str, config: dict[str, Any]) -> None: ...
    def cancel(self: Any, job_id: str) -> None: ...
