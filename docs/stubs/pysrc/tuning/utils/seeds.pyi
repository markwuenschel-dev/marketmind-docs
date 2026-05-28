from typing import Any

"""
Deterministic seed derivation for the tuning sub-system.

Produces reproducible integer seeds from a base seed and a namespace string via HMAC-SHA256.
"""

SEED_DIGEST_BYTES: Final[int] = ...
def derive_seed(base: int, namespace: str) -> int: ...
