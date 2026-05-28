from typing import Any

"""
py/ops/hashing/primitives/blake3_impl.py
════════════════════════════════════════════
BLAKE3-256 implementation for all immutable and distributed identity surfaces.

Covers HashPurpose values:
  CAS_ARTIFACT_ID          → domain: cas.v1:b3-256
  MERKLE_NODE_HASH         → domain: merkle.v1:b3-256
  AUDIT_LOG_DIGEST         → domain: audit.v1:b3-256
  DISTRIBUTED_CACHE_KEY    → domain: dist.v1:b3-256

ADR-007 v1.1 §5.1 — Mathematical Bounds
  Collision resistance : 128-bit (birthday bound on 256-bit output)
  At n=10^12 artifacts : P(collision) ≈ 4.32×10⁻⁵⁴
  Length-extension     : Inherent via ROOT flag + feed-forward XOR of block counter
  Throughput ≥4 KiB    : ~6.9 GiB/s single-threaded (AVX-512), ~92 GB/s multi-core
  Throughput <4 KiB    : SHA-256 is 30–50% faster; BLAKE3 still REQUIRED for CAS

LIBRARY REQUIREMENTS
  Python: blake3 PyPI package (C extension, not pure-Python).
          Import: import blake3
          Pin:    blake3 >= 0.3.3
  Java:   JNI binding to C reference implementation.
          Pure-Java BLAKE3 is ~14× slower and NOT permitted for any CAS surface.

DETERMINISM
  All purposes in this module are D3 Bitwise.  Cross-language byte-equivalence
  is guaranteed by the official BLAKE3 team test vectors.
  Golden vectors: tests/golden/adr007/blake3/vectors.py

BANNED
  SHA-256 for CAS       : Merkle parallelism absent; length-extension vulnerable.
  XXH3-128 for CAS      : Non-cryptographic; collision construction in microseconds.
  BLAKE2b for CAS       : No structural parallelism; BLAKE3 strictly supersedes.
  Bare hex digests      : All outputs must be wrapped in HashRef envelopes.
  AHM selection         : AHM PERMANENTLY FORBIDDEN from producing CAS/Merkle/Audit IDs.
"""

class Blake3Hasher:
    def hash_artifact_id(self: Any, artifact_bytes: bytes) -> HashRef: ...
    def hash_merkle_node(self: Any, left_digest_hex: str, right_digest_hex: str, *, depth: int) -> HashRef: ...
    def hash_audit_log_entry(self: Any, entry_bytes: bytes, *, sequence_number: int) -> HashRef: ...
    def hash_distributed_cache_key(self: Any, key_material: bytes, *, namespace: str) -> HashRef: ...
    def incremental_hasher(self: Any) -> 'Blake3IncrementalHasher': ...
class Blake3IncrementalHasher:
    def __init__(self: Any) -> None: ...
    def update(self: Any, chunk: bytes) -> None: ...
    def finalize_cas_id(self: Any) -> HashRef: ...
BLAKE3: Blake3Hasher = ...
