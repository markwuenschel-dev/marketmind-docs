from typing import Any

"""
p2_runner.py

Orchestration helpers for the full P2 broad-reset pipeline.
"""

LOG: Any
def run_full_p2_pipeline(config: P2Config | None = ...) -> dict[str, Path]: ...
