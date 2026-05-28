from typing import Any

"""
End-to-end instrument-decision row builder for the W2 Agent A bridge.
"""

FORWARD_RETURN_REQUIRED_COLUMNS: tuple[str, ...] = ...
def build_instrument_decision_rows(weighted_signal_rows: pd.DataFrame, forward_return_rows: pd.DataFrame | None = ..., config: W2AllocatorBenchmarkConfig | None = ...) -> pd.DataFrame: ...
