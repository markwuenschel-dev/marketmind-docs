from typing import Any

"""
Threshold gating for transfer report metrics.

Per spec §11.3, applies policy thresholds to metrics:
- spearman_rho: min threshold
- top_k_overlap: min threshold for each k value
- false_positive_rate: max threshold (optional)
"""

class ThresholdResult:
    valid: bool = ...
    violations: list[GateError] = ...
def apply_thresholds(transfer_report: dict[str, Any], policy: PolicyConfig) -> ThresholdResult: ...
def check_required_artifacts(artifact_types: set[str], mode: str, policy: PolicyConfig) -> list[GateError]: ...
