from typing import Any

"""
Replay consistency: verify re-running a task with the same seed produces identical splits.
"""

def assert_splits_identical(splits_a: list[tuple[pd.DatetimeIndex, pd.DatetimeIndex]], splits_b: list[tuple[pd.DatetimeIndex, pd.DatetimeIndex]]) -> None: ...
