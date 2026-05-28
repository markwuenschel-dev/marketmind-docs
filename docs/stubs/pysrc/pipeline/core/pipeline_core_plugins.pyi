from typing import Any

"""
Loads stage-specific plugins via importlib.metadata entry points.
"""

def load_stage_plugins(stage: str, group_prefix: str = ...) -> Any: ...
def discover_all_plugins(stages: Iterable[str], group_prefix: str = ...) -> Any: ...
