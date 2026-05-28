from typing import Any

"""
LatencyBudget: enforces per-inference latency constraints.
"""

class LatencyBudgetExceededError(RuntimeError):
    ...
class LatencyBudget:
    def __init__(self: Any, budget_ms: int) -> None: ...
    def elapsed_ms(self: Any) -> float: ...
