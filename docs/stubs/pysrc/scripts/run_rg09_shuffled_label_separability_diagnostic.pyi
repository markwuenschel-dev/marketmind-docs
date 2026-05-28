from typing import Any

"""
CLI: real vs shuffled_label separability decomposition per fold (boundary-recovery lanes).
"""

SHUFFLED_LABEL_SEP_DIAG_FILENAME: Any
def run_rg09_shuffled_label_separability_diagnostic(*, fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_path: Path, boundary_recovery_mode: str) -> dict[str, Any]: ...
def cli(fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_path: Path | None, boundary_recovery_mode: str) -> None: ...
