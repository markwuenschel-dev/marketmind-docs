from typing import Any

"""
CLI entrypoint for RG-09 one-axis geometry sensitivity diagnostics.
"""

def run_rg09_geometry_sensitivity(*, fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_path: Path, support_values: list[int] | None = ..., query_values: list[int] | None = ..., dwell_values: list[int] | None = ...) -> dict[str, Any]: ...
def cli(fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_path: Path | None, support_values: str | None, query_values: str | None, dwell_values: str | None) -> None: ...
