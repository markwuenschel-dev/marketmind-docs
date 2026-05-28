from typing import Any

"""
py/ops/hashing/primitives/minhash_impl.py
═════════════════════════════════════════════
MinHash-128 for sparse set approximate Jaccard similarity (HashPurpose.LSH_SET_MINHASH).

ADR-007 v1.1 §5.8 — Statistical Bounds

  Jaccard estimator via MinHash:
    E[Ĵ] = J(A, B)   (unbiased for any J ∈ [0, 1])
    Var[Ĵ] = J(1−J) / k    where k = 128 hash functions
    Worst-case stddev (at J=0.5): σ = 0.5 / √128 ≈ 0.0442

  Compared to SimHash:
    MinHash: O(|A|+|B|) time, optimal for sparse sets.
    SimHash: O(d) time, optimal for dense vectors.

  k=128 bound at various J:
    J=0.1:  σ = 0.0266   J=0.5:  σ = 0.0442   J=0.9:  σ = 0.0266

ELEMENT HASH SEEDS (ADR-007 v1.1 §5.8 §B)
  For each of the k=128 hash functions:
    seed_i = HMAC(master_seed, b'mm/minhash/v1' + u32be(i))

  Each element e is hashed with function i as:
    value_i(e) = SipHash-2-4(key=seed_i[:16], msg=canonical_bytes(e))

  Note: SipHash-2-4 is used here as a fast integer hash family, not for
  HashDoS resistance.  The key is the first 16 bytes of the HMAC-derived seed.
  key_id for the resulting HashRef references the master_seed's key_id,
  NOT an individual SipHash key — the seed rotation is implicit in the index.

INPUT CANONICALIZATION
  Input must be a set (deduplicated).  Multisets silently inflate Jaccard —
  caller must deduplicate before calling.
  Elements are sorted lexicographically before hashing to achieve determinism
  across set iteration orderings.
  Each element is encoded as UTF-8 bytes (strings) or passed as raw bytes.

BANNED
  Multiset inputs without deduplication.
  Non-HMAC hash function seeds.
  Using MinHash as an identity hash or a cache key.
  k < 128 for production gate thresholds.
"""

class MinHash128:
    K: Any
    def __init__(self: Any, master_seed: bytes, master_key_id: str) -> None: ...
    def hash_set(self: Any, elements: Iterable[str | bytes]) -> np.ndarray: ...
    def make_hashref(self: Any, signature: np.ndarray) -> HashRef: ...
    def jaccard_estimate(sig_a: np.ndarray, sig_b: np.ndarray) -> float: ...
