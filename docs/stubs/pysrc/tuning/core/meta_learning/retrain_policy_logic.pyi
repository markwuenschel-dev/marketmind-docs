from typing import Any

"""
Pure logic for evaluating whether a drift event should trigger retraining.
"""

def should_retrain(drift_score: float, threshold: float, last_retrain_at: datetime, cooldown_seconds: int, now: datetime) -> bool: ...
