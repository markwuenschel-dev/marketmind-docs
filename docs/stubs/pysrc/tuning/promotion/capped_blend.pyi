from typing import Any

"""
Capped blend: allocate up to blend_cap weight to a new candidate alongside the live strategy.
"""

def run_capped_blend(candidate_id: str, job_id: str, blend_cap: float, context: dict[str, Any]) -> dict[str, Any]: ...
