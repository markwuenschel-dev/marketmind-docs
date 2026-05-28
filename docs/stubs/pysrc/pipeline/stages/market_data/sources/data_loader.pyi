from typing import Any

"""
Unified data loading across sources using factory pattern.
"""

pl: Any
pd: Any
logger: Any
async def fetch_raw(cfg: Any, *, symbols: Union[str, List[str]], start: str, end: str, concurrency_limit: int = ...) -> Union[pl.LazyFrame, Dict[str, Union[pl.LazyFrame, Exception]]]: ...
def build_loader(cfg: Any) -> Any: ...
