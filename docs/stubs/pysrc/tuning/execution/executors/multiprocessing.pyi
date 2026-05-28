from typing import Any

"""
MultiprocessingExecutor: runs tasks in a process pool.
"""

class MultiprocessingExecutor:
    def __init__(self: Any, n_workers: int = ...) -> None: ...
    def map(self: Any, fn: Callable[[dict[str, Any]], dict[str, Any]], tasks: list[dict[str, Any]]) -> list[dict[str, Any]]: ...
