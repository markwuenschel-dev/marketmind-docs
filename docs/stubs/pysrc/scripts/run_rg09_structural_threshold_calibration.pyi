from typing import Any

"""
CLI entrypoint for RG-09 structural threshold calibration artifact.
"""

LOG: Any
def cli(fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_path: Path, calibration_quantile: float) -> None: ...
