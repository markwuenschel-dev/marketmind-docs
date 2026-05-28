from typing import Any

"""
CLI entrypoint for the RG-09 II-0A bounded falsification harness.
"""

def run_rg09_gate(*, fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_dir: Path, boundary_recovery: RG09BoundaryRecoverySpec | None = ...) -> RG09HarnessResult: ...
def cli(fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_dir: Path) -> None: ...
