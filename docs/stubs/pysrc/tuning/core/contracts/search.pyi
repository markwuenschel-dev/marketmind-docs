from typing import Any

"""
SearchProtocol: interface for search algorithm implementations.
"""

class SearchProtocol(Protocol):
    def propose(self: Any, ir: 'SearchIR', n: int) -> list[dict[str, object]]: ...
    def update(self: Any, ir: 'SearchIR', result: dict[str, float]) -> 'SearchIR': ...
    def best(self: Any, ir: 'SearchIR') -> dict[str, object]: ...
