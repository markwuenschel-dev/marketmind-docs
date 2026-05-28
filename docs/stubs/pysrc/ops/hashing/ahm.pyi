from typing import Any

"""
py/ops/hashing/ahm.py
═════════════════════════
Adaptive Hash Manager (AHM) — ephemeral-only runtime hash selection.

ADR-007 v1.1 §6.2 — AHM Boundary (PERMANENT CONSTRAINTS)

  The AHM is PERMITTED to:
    - Select XXH3-64  for HashPurpose.EPHEMERAL_MAP_KEY
    - Select SipHash-2-4 for HashPurpose.HASHDOS_TABLE_KEY
    - Select SipHash-2-4 for HashPurpose.UNTRUSTED_INPUT_EPHEMERAL_KEY
    - Observe hardware capabilities (AVX-512, NEON) for algorithmic tuning
      within the EPHEMERAL tier only.

  The AHM is PERMANENTLY FORBIDDEN from:
    - Producing CAS IDs (HashPurpose.CAS_ARTIFACT_ID)
    - Producing Merkle node hashes (HashPurpose.MERKLE_NODE_HASH)
    - Producing audit log digests (HashPurpose.AUDIT_LOG_DIGEST)
    - Producing gate attestation hashes (HashPurpose.GATE_ATTESTATION)
    - Producing distributed cache keys (HashPurpose.DISTRIBUTED_CACHE_KEY)
    - Downgrading LOCAL_PERSISTENT_CACHE_KEY to a non-XXH3-128 algorithm
    - Emitting any HashRef with a non-ephemeral persistence tier

  Violation raises HashContractViolation immediately.  The AHM does not
  'fall back' or 'degrade gracefully' — it fails hard.

ALLOWED ADAPTATIONS
  The AHM selects between:
    SipHash-2-4 vs XXH3-64 based on whether the input source is trusted:
      Trusted (internal, bounded-size): XXH3-64
      Untrusted (external, user-controlled): SipHash-2-4

  Input-size-based variant selection (SipHash only):
    |input| > 4×10⁹ entries → use SipHash-2-4-128 (128-bit output variant).
    This is a forward-compatibility hook; the 128-bit variant is NOT yet
    implemented in this module and raises NotImplementedError if triggered.

WHY AHM IS NOT A GENERAL-PURPOSE DISPATCH LAYER
  The AHM was an anti-pattern in earlier designs where it attempted to
  select BLAKE3 vs SHA-256 based on input size.  That design allowed a code
  path to silently produce XXH3-128 for a CAS surface.  The AHM is now
  strictly ephemeral — all non-ephemeral dispatch is handled by direct
  instantiation of the specific primitive class.

USAGE
    ahm = AHM(siphash_key=SipHashKey.generate())
    ref = ahm.hash_ephemeral(
        key_bytes, namespace="order_book.bids.v1",
        trusted=True,  # selects XXH3-64
    )
"""

class AHM:
    def __init__(self: Any, *, siphash_key: SipHashKey) -> None: ...
    def hash_ephemeral(self: Any, key_bytes: bytes, *, namespace: str, trusted: bool) -> HashRef | int: ...
    def hash_untrusted_input(self: Any, key_bytes: bytes, *, namespace: str) -> HashRef: ...
    def validate_purpose_scope(self: Any, purpose: HashPurpose) -> None: ...
