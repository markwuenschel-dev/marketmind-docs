from typing import Any

"""
DistributedExecutor: delegates to a registered distributed backend (Ray / Dask).
"""

class DistributedExecutor:
    def map(self: Any, fn: Callable[[dict[str, Any]], dict[str, Any]], tasks: list[dict[str, Any]]) -> list[dict[str, Any]]: ...
