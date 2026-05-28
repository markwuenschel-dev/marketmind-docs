from typing import Any

"""
Pure time-series segmentation logic for task partitioning.
"""

def split_walkforward(start: datetime, end: datetime, n_splits: int, embargo_bars: int, bar_duration: timedelta) -> list[FoldBoundary]: ...
