from typing import Any

"""
Report assembly for the W2-SU signal-usability artifact.
"""

def build_signal_usability_report(*, panel: pd.DataFrame, config: SignalUsabilityConfig, run_id: str, created_at: str, missing_signal_reasons: Mapping[str, str], baselines: Mapping[str, Mapping[str, object]], models: Mapping[str, Mapping[str, object]], metrics: Mapping[str, object], split: Mapping[str, object], learnability_interpretation: Mapping[str, str], classification: Mapping[str, str]) -> dict[str, object]: ...
