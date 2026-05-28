from typing import Any

"""
RFC8785 JCS canonicalization and SHA-256 hashing.

This module implements content hashing per the spec §7:
    content_hash = "sha256:" + sha256( RFC8785_JCS(artifact_json) ).hexdigest()

RFC8785 requirements:
- Sort object keys lexicographically
- No whitespace
- UTF-8 encoding
- Reject NaN, Infinity
- Normalize -0 → 0
- Consistent number serialization
"""

def canonicalize(data: dict[str, Any] | list[Any]) -> bytes: ...
def compute_content_hash(json_data: dict[str, Any] | list[Any]) -> str: ...
