from typing import Any

"""
Regime-conditioned splits: group fold observations by detected regimes.
"""

def regime_conditioned_splits(index: pd.DatetimeIndex, segments: tuple[RegimeSegment, ...], bar_duration: timedelta) -> dict[str, pd.DatetimeIndex]: ...
