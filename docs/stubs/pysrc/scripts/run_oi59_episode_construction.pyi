from typing import Any

"""
CLI entrypoint for OI-59 Experiment 4 episode-construction redesign.
"""

def run_oi59_episode_construction(*, fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, experiment2_report_path: Path, output_dir: Path, baseline_handoff_path: Path | None = ...) -> dict[str, Any]: ...
def cli(fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, experiment2_report_path: Path, baseline_handoff_path: Path | None, output_dir: Path | None) -> None: ...
