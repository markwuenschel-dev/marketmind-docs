from typing import Any

"""
Schema-level IR checks: verify that spec hashes and version strings are well-formed.
"""

class SchemaCheckError(ValueError):
    ...
def validate_spec_hash(spec_hash: str) -> str: ...
def validate_metadata(meta: IRMetadata) -> IRMetadata: ...
