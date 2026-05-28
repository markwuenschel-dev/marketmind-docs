from typing import Any

"""
Shadow mode: run a promoted candidate alongside the live strategy without affecting signals.
"""

def run_shadow_mode(candidate_id: str, job_id: str, duration_days: int, context: dict[str, Any]) -> dict[str, Any]: ...
