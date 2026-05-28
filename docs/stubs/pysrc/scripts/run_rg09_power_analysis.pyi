from typing import Any

"""
CLI: advisory-only RG-09 power analysis.
"""

def run_rg09_power_analysis_cli(*, baseline_run_dir: Path, comparison_run_dirs: list[Path], output_dir: Path) -> int: ...
def cli(baseline_run_dir: Path, comparison_run_dirs: tuple[Path, ...], output_dir: Path) -> None: ...
