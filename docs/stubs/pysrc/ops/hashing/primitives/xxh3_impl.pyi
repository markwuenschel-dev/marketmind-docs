from typing import Any

"""
py/ops/hashing/primitives/xxh3_impl.py
══════════════════════════════════════════
XXH3 hasher for local-persistent cache keys, DataFrame fingerprints,
and ephemeral in-memory maps.

Covers HashPurpose values:
  LOCAL_PERSISTENT_CACHE_KEY   → XXH3-128  (D3 Bitwise)
  DATAFRAME_FINGERPRINT_FAST   → XXH3-128  (D3 Bitwise, local-machine only until CanonicalFrame locked)
  EPHEMERAL_MAP_KEY            → XXH3-64   (D2 Semantic)

ADR-007 v1.1 §5.3 / §5.4 — Birthday Bound Analysis

  XXH3-64:
    At n=10⁶  keys: P(collision) ≈ 2.71×10⁻⁸  (SAFE for ephemeral)
    At n=10⁸  keys: P(collision) ≈ 2.71×10⁻⁴  (BORDERLINE — ephemeral session max)
    At n=10⁹  keys: P(collision) ≈ 2.71×10⁻²  (UNACCEPTABLE — 1-in-37 false match)
    → BANNED for LOCAL_PERSISTENT_CACHE_KEY.

  XXH3-128:
    At n=10⁹  keys: P(collision) ≈ 1.47×10⁻²¹ (SAFE at any production scale)
    At n=10¹² keys: P(collision) ≈ 1.47×10⁻¹⁵ (SAFE post-Phase III)
    → REQUIRED for LOCAL_PERSISTENT_CACHE_KEY.

  DISTRIBUTED_CACHE_KEY → BLAKE3-256 ONLY.  XXH3-128 is BANNED for
  distributed surfaces regardless of cardinality.

LIBRARY REQUIREMENTS
  python-xxhash >= 3.0.0  (pre-3.0.0 used little-endian digest())
  Pin in pyproject.toml / requirements: xxhash>=3.0.0

EQUALITY FALLBACK LAW (ADR-007 v1.1 §6.4)
  Non-cryptographic hashes.  Every cache entry backed by XXH3 MUST store
  payload_bytes or aux_check.  See envelope.verify_cache_hit().

BANNED
  XXH3-64  for LOCAL_PERSISTENT_CACHE_KEY
  XXH3-128 for DISTRIBUTED_CACHE_KEY
  Legacy xxHash32 / xxHash64 variants
  SipHash for trusted hot-path maps
"""

class XXH3Hasher:
    def hash_local_persistent_key(self: Any, key_bytes: bytes, *, namespace: str) -> HashRef: ...
    def hash_dataframe_fingerprint(self: Any, df: 'pd.DataFrame', *, sort_key: list[str], namespace: str = ...) -> HashRef: ...
    def hash_ephemeral_key(self: Any, key_bytes: bytes, *, namespace: str) -> int: ...
    def hash_ephemeral_key_hex(self: Any, key_bytes: bytes, *, namespace: str) -> str: ...
XXH3: XXH3Hasher = ...
