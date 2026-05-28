from typing import Any

"""
py/ops/hashing/primitives/rabin_impl.py
═══════════════════════════════════════════
Rabin GF(2⁶³) rolling fingerprint for content-defined chunking and
rolling window deduplication.

Covers HashPurpose values:
  ROLLING_WINDOW_FINGERPRINT  (D2 Ephemeral)
  CHUNK_BOUNDARY_DETECTION    (D2 Ephemeral)

ADR-007 v1.1 §5.9 — Algebraic Properties

  Rabin fingerprinting (Rabin 1981):
    φ(P) = P mod f(x)   in GF(2)[x] / f(x)
    where f(x) is the irreducible polynomial of degree 63.

  Rolling O(1) update:
    Given window [i, i+w), adding byte b_{i+w} and removing byte b_i:
      fingerprint_new = reduce_table[current >> 56]
                      XOR (current << 8)
                      XOR add_table[b_{i+w}]
                      XOR pop_table[b_i]

  Polynomial used (from Rabin 1981 Appendix):
    p(x) = x⁶³ + x + 1  (binary representation: 0x8000000000000003)
    This polynomial is VERIFIED irreducible.  Do not substitute without a
    new ADR and primality/irreducibility proof.

  Hash space: 2⁶³  (9.2×10¹⁸ distinct values)
  Collision probability per window: 2⁻⁶³ ≈ 1.08×10⁻¹⁹

TABLE SIZES
  REDUCE_TABLE: 256 entries × 8 bytes = 2 KiB
  POP_TABLE:    256 × W entries × 8 bytes (W = window size in bytes)
  Total: 2 + (256 × W / 1024) KiB

CROSS-BOUNDARY PROMOTION RULE (v1.1 — NEW)
  Any Rabin fingerprint that crosses a process trust boundary MUST be promoted
  to BLAKE3 via Merkle composition before transmission.
  Direct Rabin values MUST NEVER appear in HashRef envelopes at distributed tiers.

INITIALIZATION REQUIREMENT
  Polynomial irreducibility MUST be verified at startup (hard assertion).
  REDUCE_TABLE and POP_TABLE MUST be derived from the polynomial at init.
  They MUST NOT be hardcoded as literals.

BANNED
  Hardcoding REDUCE_TABLE or POP_TABLE     : Must be derived from polynomial at init.
  Using Rabin at persistent/immutable tiers: 63-bit output; collision probability too high.
  Using Rabin across process boundaries     : Use cross-boundary promotion rule instead.
  CRC32/Adler32 variants                   : Not Galois-field fingerprints; different semantics.
"""

RABIN_POLY: int = ...
RABIN_POLY_DEGREE: int = ...
class RabinRollingHasher:
    def __init__(self: Any, window_size: int, poly: int = ...) -> None: ...
    def reset(self: Any) -> None: ...
    def roll_byte(self: Any, incoming: int) -> int: ...
    def fingerprint(self: Any, data: bytes) -> int: ...
    def find_boundaries(self: Any, data: bytes, mask: int) -> Iterator[int]: ...
    def make_hashref(self: Any, fingerprint: int) -> HashRef: ...
