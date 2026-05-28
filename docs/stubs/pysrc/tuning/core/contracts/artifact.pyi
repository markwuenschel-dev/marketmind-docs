from typing import Any

"""
ArtifactProtocol: interface for content-addressed artifact writers/readers.
"""

class ArtifactWriterProtocol(Protocol):
    def write(self: Any, payload: dict[str, Any], metadata: dict[str, str]) -> str: ...
class ArtifactReaderProtocol(Protocol):
    def read(self: Any, cas_hash: str) -> dict[str, Any]: ...
    def exists(self: Any, cas_hash: str) -> bool: ...
