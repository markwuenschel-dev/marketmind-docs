from typing import Any

"""
SpecFactory: build Spec objects from raw config dicts.
"""

def build_tuning_job_spec(raw: dict[str, Any], spec_hash: str) -> TuningJobSpec: ...
