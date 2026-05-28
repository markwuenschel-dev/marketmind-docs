from typing import Any

"""
Translates incoming API calls into orchestration commands.

Layer rule: Shell only — no computation; orchestration is imported lazily.
"""

def submit_tuning_job(req: TuningJobRequest) -> TuningJobResponse: ...
def get_job_status(job_id: str) -> SearchStatusResponse: ...
def submit_promotion(req: PromotionRequest) -> PromotionResponse: ...
