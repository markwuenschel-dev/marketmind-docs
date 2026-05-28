from typing import Any

"""
ArtifactFactory: build artifact payload dicts from tuning results.
"""

def build_trial_artifact(job_id: str, candidate_id: str, params: dict[str, Any], scores: dict[str, float], spec_hash: str, determinism_tier: str) -> dict[str, Any]: ...
