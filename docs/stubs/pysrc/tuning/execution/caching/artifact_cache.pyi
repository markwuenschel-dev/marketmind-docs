from typing import Any

"""
ArtifactCache: thin read-through cache for artifact payloads by CAS hash.
"""

class ArtifactCache:
    def __init__(self: Any) -> None: ...
    def get(self: Any, cas_hash: str) -> Any | None: ...
    def put(self: Any, cas_hash: str, payload: Any) -> None: ...
