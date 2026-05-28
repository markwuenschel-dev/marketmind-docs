from typing import Any

"""
Pre-gate RG-09 episode-feasibility reporting without changing harness behavior.
"""

LOG: Any
FEASIBILITY_REPORT_FILENAME: Any
FEASIBILITY_REPORT_SCHEMA: Any
EXPECTED_H2_FIXTURE_RELATIVE_PATH: Any
EXPECTED_H2_FIXTURE_SHA256: Any
def build_episode_feasibility_report(*, fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_path: Path, boundary_recovery: RG09BoundaryRecoverySpec | None = ..., emit_overlap_sampled_diagnostic: bool = ..., overlap_diagnostic_sample_size: int = ...) -> dict[str, Any]: ...
