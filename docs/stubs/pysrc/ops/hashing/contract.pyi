from typing import Any

"""
py/ops/hashing/contract.py
═════════════════════════════
Canonical enum definitions for the MarketMind Hashing Contract (ADR-007 v1.1).

No hash call may exist in this codebase without declaring a HashPurpose.  This
module is the single source of truth for which algorithm, persistence tier, and
determinism tier is required for each purpose.  All downstream modules import
from here — never from each other.

IMPORT STABILITY GUARANTEE
  All names exported from this module are considered locked at v1.1.
  Adding new HashPurpose values requires a superseding ADR.
  Removing or renaming any value is a breaking change at the contract layer.

D-TIER TAXONOMY (canonical MarketMind definitions)
  D3 — Bitwise   : bit-for-bit identical across all runs, machines, and time.
  D2 — Semantic  : identical for identical inputs within a deployment.
  D1 — Topological: structural equivalence; no HashPurpose maps here.
  D0 — None/Debug: no guarantee; no HashPurpose may be D0.
"""

class DTier(enum.IntEnum):
    NONE: Any
    TOPOLOGICAL: Any
    SEMANTIC: Any
    BITWISE: Any
class PersistenceTier(enum.Enum):
    IMMUTABLE_CAS: Any
    DISTRIBUTED: Any
    LOCAL_PERSISTENT: Any
    EPHEMERAL: Any
class AlgoId(str, enum.Enum):
    BLAKE3_256: Any
    SHA256_JCS: Any
    XXH3_128: Any
    XXH3_64: Any
    SIP24: Any
    HMAC_SHA256: Any
    SIMHASH_128: Any
    MINHASH_128: Any
    RABIN_63: Any
class DomainPrefix(str, enum.Enum):
    CAS: Any
    MERKLE: Any
    AUDIT: Any
    ATTEST: Any
    CACHE: Any
    DIST: Any
    FRAME: Any
    SEED: Any
    LSH: Any
    ROLLING: Any
class HashPurposeMetadata:
    algo_id: AlgoId = ...
    d_tier: DTier = ...
    persistence_tier: PersistenceTier = ...
    domain_prefix: DomainPrefix = ...
    algo_version: str = ...
    canonicalizer_id: str = ...
    canonicalizer_version: str = ...
class HashPurpose(enum.Enum):
    CAS_ARTIFACT_ID: Any
    MERKLE_NODE_HASH: Any
    AUDIT_LOG_DIGEST: Any
    GATE_ATTESTATION: Any
    DISTRIBUTED_CACHE_KEY: Any
    LOCAL_PERSISTENT_CACHE_KEY: Any
    DATAFRAME_FINGERPRINT_FAST: Any
    EPHEMERAL_MAP_KEY: Any
    HASHDOS_TABLE_KEY: Any
    UNTRUSTED_INPUT_EPHEMERAL_KEY: Any
    SEED_DERIVATION: Any
    LSH_VECTOR_SIMHASH: Any
    LSH_SET_MINHASH: Any
    ROLLING_WINDOW_FINGERPRINT: Any
    CHUNK_BOUNDARY_DETECTION: Any
    def meta(self: Any) -> HashPurposeMetadata: ...
    def requires_d3(self: Any) -> bool: ...
    def is_persistent(self: Any) -> bool: ...
    def is_ahm_forbidden(self: Any) -> bool: ...
class SystemInvariant(enum.Enum):
    CANONICAL_UTF8: Any
    CANONICAL_BIG_ENDIAN: Any
    IEEE754_NORMALIZED: Any
    DOMAIN_SEPARATED_PREIMAGE: Any
    NO_RUNTIME_LAYOUT_DEPENDENCE: Any
    GOLDEN_VECTOR_REQUIRED: Any
    D3_BITWISE_REQUIRED: Any
class HashContractViolation(RuntimeError):
    def __init__(self: Any, invariant: SystemInvariant | str, detail: str) -> None: ...
class CanonicalValueRejected(ValueError):
    def __init__(self: Any, field: str, value: object, reason: str) -> None: ...
