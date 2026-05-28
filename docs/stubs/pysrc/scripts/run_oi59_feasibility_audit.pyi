from typing import Any

"""
CLI entrypoint for the OI-59 corrected-surface feasibility audit.
"""

def run_oi59_feasibility_audit(*, fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_json_path: Path, output_markdown_path: Path) -> dict[str, Any]: ...
def cli(fixture_path: Path, fixture_summary_path: Path, fixture_metadata_path: Path, config_path: Path, output_dir: Path | None) -> None: ...
