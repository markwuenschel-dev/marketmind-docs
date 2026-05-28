from typing import Any

"""
Recovery: resume a partially-completed job from its last checkpoint.
"""

def recover_job(job_id: str, context: dict[str, Any]) -> dict[str, Any]: ...
