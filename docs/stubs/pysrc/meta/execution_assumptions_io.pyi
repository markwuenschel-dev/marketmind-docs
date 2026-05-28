from typing import Any

"""
Append-only I/O helpers for governed execution assumptions.
"""

def write_execution_assumptions(report: ExecutionAssumptionsReport, output_dir: str | Path | None = ...) -> Path: ...
def load_execution_assumptions(path: str | Path) -> dict[str, Any]: ...
