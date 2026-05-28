from typing import Any

"""
CLI: RG-09 broader empirical closure (II-0, non-promotable).
"""

LOG: Any
def run_rg09_empirical_closure_cli(*, fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_dir: Path, boundary_recovery: RG09BoundaryRecoverySpec | None = ...) -> int: ...
def cli(fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_dir: Path, boundary_recovery_mode: str | None) -> None: ...
