from typing import Any

"""
py/ops/hashing/primitives/sha256_jcs.py
═══════════════════════════════════════════
SHA-256 over RFC 8785 JCS bytes for gate-facing attestation.

Covers HashPurpose:
  GATE_ATTESTATION  → domain: attest.v1:jcs-sha256

ADR-007 v1.1 §5.2 — Dual-Domain Contract
  MarketMind runs a dual-domain identity model:
    cas.v1:b3-256      → BLAKE3-256   (immutable artifact identity)
    attest.v1:jcs-sha256 → SHA-256/JCS (gate-facing verifiable attestation)

  These are NOT interchangeable.  CAS identity is content-addressable truth.
  Attestation is verifiable interoperability proof for the gate pipeline.

  Every artifact with a CAS identity MUST ALSO have an attestation hash.
  Both are stored in bundle_manifest.json as {cas, attest} per artifact role.

GATE WIRE FORMAT
  The gate pipeline consumes attestation as "sha256:<hex>" — NOT the full
  HashRef envelope.  The to_gate_content_hash() function in this module is
  the ONLY permitted conversion.  Callers must never hand-slice the prefix.

BANNED
  BLAKE3 for GATE_ATTESTATION : Gate pipeline pinned to SHA-256.
  Bare SHA-256(bytes)          : JCS canonicalization is mandatory before SHA-256.
  SHA-256 for CAS_ARTIFACT_ID : SHA-256 has no Merkle parallelism.
"""

class Sha256JcsHasher:
    def hash_gate_attestation(self: Any, artifact_obj: Any) -> HashRef: ...
    def hash_gate_attestation_from_jcs_bytes(self: Any, jcs_bytes: bytes) -> HashRef: ...
    def to_gate_content_hash(self: Any, attest_ref: HashRef) -> str: ...
SHA256_JCS: Sha256JcsHasher = ...
