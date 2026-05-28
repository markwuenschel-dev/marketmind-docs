from typing import Any

"""
Point-in-time leakage checks for validation splits.
"""

class LeakageDetectedError(ValueError):
    ...
def assert_no_future_in_train(train_idx: pd.DatetimeIndex, test_start: datetime) -> None: ...
