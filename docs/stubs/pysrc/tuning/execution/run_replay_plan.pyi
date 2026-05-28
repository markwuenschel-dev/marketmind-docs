from typing import Any

"""
run_replay_plan: replay a completed tuning run from stored artifacts for D0 verification.
"""

def run_replay_plan(job_id: str, artifact_hash: str, context: dict[str, Any]) -> dict[str, Any]: ...
