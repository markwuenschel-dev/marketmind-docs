from typing import Any

"""
Rollback gate: determine whether a live strategy should be rolled back.
"""

def should_rollback(live_sharpe: float, baseline_sharpe: float, min_relative_ratio: float = ..., consecutive_drawdown_bars: int = ..., max_consecutive_drawdown: int = ...) -> tuple[bool, str]: ...
