from typing import Any

"""
Stable BLAKE3-style spec hashing using blake2b as portable substitute.
"""

def hash_spec(data: dict[str, Any]) -> str: ...
