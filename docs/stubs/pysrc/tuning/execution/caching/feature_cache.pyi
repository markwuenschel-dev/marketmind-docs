from typing import Any

"""
FeatureCache: keyed cache for pre-computed feature matrices.
"""

class FeatureCache:
    def __init__(self: Any) -> None: ...
    def get(self: Any, feature_hash: str, symbol: str, as_of: str) -> Any | None: ...
    def put(self: Any, feature_hash: str, symbol: str, as_of: str, data: Any) -> None: ...
