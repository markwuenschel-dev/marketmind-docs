from typing import Any

"""
CLI entrypoint for RG-09 pre-gate episode-feasibility diagnostics.
"""

def run_rg09_feasibility(*, fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_path: Path, boundary_recovery: RG09BoundaryRecoverySpec | None = ..., emit_overlap_sampled_diagnostic: bool = ..., overlap_diagnostic_sample_size: int = ...) -> dict[str, Any]: ...
def cli(fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_path: Path | None, boundary_recovery_mode: str | None, emit_overlap_sampled_diagnostic: bool, overlap_diagnostic_sample_size: int) -> None: ...
