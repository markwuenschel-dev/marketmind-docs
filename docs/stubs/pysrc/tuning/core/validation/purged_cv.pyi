from typing import Any

"""
Purged cross-validation: removes training samples that overlap the test window.
"""

def purge_training_index(train_idx: pd.DatetimeIndex, test_start: datetime, test_end: datetime, embargo_periods: int, bar_duration: timedelta) -> pd.DatetimeIndex: ...
def purged_splits(index: pd.DatetimeIndex, n_splits: int, embargo_periods: int, bar_duration: timedelta) -> list[tuple[pd.DatetimeIndex, pd.DatetimeIndex]]: ...
