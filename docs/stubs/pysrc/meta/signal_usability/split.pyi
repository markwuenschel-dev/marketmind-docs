from typing import Any

"""
Temporal split helpers for W2-SU v1.
"""

def derive_temporal_split(panel: pd.DataFrame, config: SignalUsabilityConfig) -> dict[str, str]: ...
def apply_temporal_split(panel: pd.DataFrame, split: Mapping[str, str]) -> pd.DataFrame: ...
