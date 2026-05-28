from typing import Any

"""
Append-only I/O helpers for governed task manifests.
"""

def write_task_manifest(report: TaskManifestReport, output_dir: str | Path | None = ...) -> Path: ...
def load_task_manifest(path: str | Path) -> dict[str, Any]: ...
