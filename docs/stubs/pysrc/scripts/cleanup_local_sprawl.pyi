from typing import Any

"""
Local housekeeping for worktree/cache/build sprawl.

This script is intentionally local-only: it removes untracked local folders that should
not be committed and can be regenerated.
"""

TARGETS: Any
VENV_TARGETS: Any
W3_PHASE_II_ROOT: Any
def main() -> int: ...
