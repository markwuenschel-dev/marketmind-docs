from typing import Any

"""
One-pass diagnostic: real vs shuffled_label separability on boundary-recovery episodes.
"""

DIAGNOSTIC_SCHEMA_VERSION: Any
def regime_separability_decomposition(episodes: pd.DataFrame) -> dict[str, Any]: ...
def candidate_segment_regime_class_purity(groups: list[pd.DataFrame], *, regime_class_column: str = ..., majority_label: bool = ...) -> dict[str, Any]: ...
def build_shuffled_label_separability_diagnostic(*, frame: pd.DataFrame, config: RG09PilotConfig, fixture_sha256: str, fold_construction: dict[str, Any] | None, require_strict_geometry: bool, boundary_recovery: RG09BoundaryRecoverySpec) -> dict[str, Any]: ...
