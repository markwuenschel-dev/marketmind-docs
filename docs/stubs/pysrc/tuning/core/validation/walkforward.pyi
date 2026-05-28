from typing import Any

"""
Walk-forward cross-validation split generator.
"""

def walkforward_splits(ir: ValidationIR, start: datetime, end: datetime, bar_duration: timedelta) -> list[FoldBoundary]: ...
