from typing import Any

"""
CLI entrypoint for OI-59 Experiment 2 segmentation redesign.
"""

def run_oi59_segmentation_redesign(*, fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, baseline_reference_path: Path, output_dir: Path) -> dict[str, Any]: ...
def cli(fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, baseline_reference_path: Path, output_dir: Path | None) -> None: ...
