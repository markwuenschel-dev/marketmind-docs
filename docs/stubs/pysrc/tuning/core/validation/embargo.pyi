from typing import Any

"""
Embargo logic: enforce a gap between training and test periods.
"""

def apply_embargo(train_end: datetime, embargo_periods: int, bar_duration: timedelta) -> datetime: ...
def trim_to_embargo(index: pd.DatetimeIndex, safe_start: datetime) -> pd.DatetimeIndex: ...
