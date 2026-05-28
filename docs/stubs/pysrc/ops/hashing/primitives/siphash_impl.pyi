from typing import Any

"""
py/ops/hashing/primitives/siphash_impl.py
═════════════════════════════════════════════
SipHash-2-4 for HashDoS-resistant map keys on adversarial inputs.

Covers HashPurpose values:
  HASHDOS_TABLE_KEY             (D2 Ephemeral)
  UNTRUSTED_INPUT_EPHEMERAL_KEY (D2 Ephemeral)

ADR-007 v1.1 §5.5 — PRF Security
  SipHash-2-4 is the ONLY variant with a formal PRF security claim.
  SipHash-1-3 has NO formal claim and is documented as 'a target for cryptanalysis.'

  PRF security bound: best known differential characteristic probability =
    2⁻²³⁶·³ (Dobraunig et al., SAC 2014) — far below 2⁻¹²⁸ exploitation threshold.

  Throughput delta vs SipHash-1-3:
    8-byte key:  +8 ns  (~35 ns vs ~27 ns)
    16-byte key: +11 ns (~45 ns vs ~34 ns)
    32-byte key: +14 ns (~60 ns vs ~46 ns)
  All deltas are negligible vs microsecond-scale network latency.

KEY LIFECYCLE (MANDATORY)
  Keys MUST be generated via os.urandom(16) at process startup.
  Keys MUST NOT be reused across process restarts if outputs are observable.
  Tables >4×10⁹ entries MUST use SipHash-2-4-128 (128-bit output variant).
  key_id UUID MUST appear in every HashRef envelope.

CRITICAL FOOTGUN — LITTLE-ENDIAN KEY ENCODING
  k0 and k1 are the LOW and HIGH 64 bits of the 128-bit key, each encoded
  as LITTLE-ENDIAN 64-bit integers.  This matches the SipHash reference
  implementation (veorq/SipHash).  Keys loaded as big-endian have k0/k1
  swapped — the most common cross-language SipHash bug.

BANNED
  SipHash-1-3             : No formal PRF claim.
  XXH3 for adversarial inputs : Non-cryptographic; O(n) degradation possible.
  Python dict default hash    : PYTHONHASHSEED-randomized; non-deterministic.
  Java HashMap.hashCode()     : Not PRF-secure.
  SipHash for persistent IDs  : 64-bit output + key rotation = ephemeral only.
"""

class SipHashKey:
    key_bytes: bytes = ...
    key_id: str = ...
    def k0(self: Any) -> int: ...
    def k1(self: Any) -> int: ...
    def generate(cls: Any) -> 'SipHashKey': ...
class SipHash24Hasher:
    def __init__(self: Any, key: SipHashKey) -> None: ...
    def key_id(self: Any) -> str: ...
    def hash_map_key(self: Any, key_bytes: bytes, *, namespace: str, purpose: HashPurpose = ...) -> HashRef: ...
    def hash_composite_key(self: Any, *fields: bytes, namespace: str, purpose: HashPurpose = ...) -> HashRef: ...
