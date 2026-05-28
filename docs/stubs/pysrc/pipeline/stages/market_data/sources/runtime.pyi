from typing import Any

"""
Runtime helpers for network-backed market-data sources.
"""

T: Any
def async_retry(*, attempts: int, multiplier: float, min_delay: float, max_delay: float) -> Callable[[Callable[..., Awaitable[T]]], Callable[..., Awaitable[T]]]: ...
class APIDataSource(DataSource):
    def __init__(self: Any, config: dict[str, Any]) -> None: ...
    async def close(self: Any) -> None: ...
