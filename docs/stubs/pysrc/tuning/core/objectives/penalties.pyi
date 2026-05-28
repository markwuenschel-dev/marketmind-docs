from typing import Any

"""
Penalty functions applied to objective scores for constraint satisfaction.
"""

def turnover_penalty(returns: pd.Series, positions: pd.DataFrame, cap: float) -> float: ...
def drawdown_penalty(returns: pd.Series, max_allowed: float) -> float: ...
