from typing import Any

"""
LocalExecutor: runs tasks sequentially in the current process.
"""

class LocalExecutor:
    def map(self: Any, fn: Callable[[dict[str, Any]], dict[str, Any]], tasks: list[dict[str, Any]]) -> list[dict[str, Any]]: ...
