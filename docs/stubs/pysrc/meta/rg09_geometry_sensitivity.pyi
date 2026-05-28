from typing import Any

"""
One-axis RG-09 precondition sensitivity diagnostics on the current task recipe.
"""

LOG: Any
GEOMETRY_SENSITIVITY_REPORT_FILENAME: Any
GEOMETRY_SENSITIVITY_REPORT_SCHEMA: Any
def build_geometry_sensitivity_report(*, fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_path: Path, support_values: list[int] | None = ..., query_values: list[int] | None = ..., dwell_values: list[int] | None = ...) -> dict[str, Any]: ...
