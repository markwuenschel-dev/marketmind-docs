from typing import Any

"""
RG-09 structural threshold calibration — null distribution and evidence artifact.

Computes the empirical null distribution for the structural separability ratio on
transition-anchored episodes and produces a governed calibration artifact for
Mark's review. Does NOT update the config; threshold changes require explicit approval
per THR-RG09-V02 governance.
"""

LOG: Any
CALIBRATION_SCHEMA_VERSION: Final[str] = ...
CALIBRATION_REPORT_FILENAME: Final[str] = ...
def compute_structural_null_distribution(episodes: pd.DataFrame, *, config: RG09PilotConfig, fixture_sha256: str, fold_id: int) -> dict[str, Any]: ...
def calibrate_structural_threshold(fold_distributions: list[dict[str, Any]], *, calibration_quantile: float = ...) -> dict[str, Any]: ...
def build_structural_calibration_report(*, fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_path: Path, calibration_quantile: float = ...) -> dict[str, Any]: ...
