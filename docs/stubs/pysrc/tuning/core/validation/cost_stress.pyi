from typing import Any

"""
Cost-stress testing: apply transaction-cost multipliers to returns.
"""

def apply_cost_stress(returns: pd.Series, positions: pd.DataFrame, stress_bps: float) -> pd.Series: ...
