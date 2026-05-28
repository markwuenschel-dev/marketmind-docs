from typing import Any

"""
CPCV: combinatorial purged cross-validation split generation.
"""

def cpcv_splits(index: pd.DatetimeIndex, n_splits: int, n_test_splits: int, embargo_periods: int, bar_duration: timedelta) -> list[tuple[pd.DatetimeIndex, pd.DatetimeIndex]]: ...
