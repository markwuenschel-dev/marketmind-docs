from typing import Any

"""
Rollback: revert the live strategy to a prior artifact snapshot.
"""

def run_rollback(job_id: str, target_artifact_hash: str, context: dict[str, Any]) -> dict[str, Any]: ...
