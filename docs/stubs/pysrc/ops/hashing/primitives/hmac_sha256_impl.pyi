from typing import Any

"""
pysrc/ops/hashing/primitives/hmac_sha256_impl.py
═════════════════════════════════════════════════
HMAC-SHA256 for deterministic seed derivation (HashPurpose.SEED_DERIVATION).

ADR-007 v1.1 §5.6 — PRF Security
  HMAC-SHA256 is the ONLY construction with a formal PRF security proof that
  does not require collision resistance of SHA-256 (Bellare, Crypto 2006).
  PRF bound: ~2¹²⁸ safe derivations for single-block messages (|M| ≤ 55 bytes).

HIERARCHICAL SEED TREE (ADR-007 v1.1 §5.6 §A)
  Context string format:
    'mm/seed/v1|{level}|{field_1}|{field_2}|...'

  Separator '|' (0x7C) is FORBIDDEN in all field values.
  Numeric IDs serialize as u64be.

  Hierarchy:
    master  → run      ctx: 'mm/seed/v1|run|{run_id}'
    run     → fold     ctx: 'mm/seed/v1|fold|{run_id}|{fold_idx}'
    fold    → worker   ctx: 'mm/seed/v1|worker|{run_id}|{fold_idx}|{worker_id}'
    worker  → strategy ctx: 'mm/seed/v1|strategy|...|{strategy_id}'
    strategy→ asset    ctx: 'mm/seed/v1|asset|...|{asset_id}'

DERIVED SEED USAGE
  256-bit HMAC output → PCG-64 PRNG: numpy.random.Generator(PCG64(seed))
  MT19937 is PERMANENTLY BANNED:
    init_by_array does not uniformly distribute 256-bit material across
    the 19937-bit state.  High-order bits have disproportionate influence
    on early outputs.  This violates D3 Bitwise determinism for statistical tests.

MASTER KEY
  32-byte CSPRNG value stored in secrets manager (Vault / AWS SM).
  Loaded once at process startup and precomputed into inner/outer HMAC pads.
  NEVER in logs, config files, or git history.
  Domain-separated from all SipHash keys.

BANNED
  SHA-256(key || message)        : Length-extension vulnerable.
  HKDF for single-output         : RFC 5869 §3.3 permits skipping extract when IKM uniform.
  MT19937 seeded from HMAC       : init_by_array does not distribute 256-bit seeds uniformly.
  SecureRandom for reproducible  : Non-deterministic across runs.
"""

class HmacSha256Deriver:
    def __init__(self: Any, master_key: bytes, master_key_id: str) -> None: ...
    def derive_run_seed(self: Any, run_id: str) -> bytes: ...
    def derive_fold_seed(self: Any, run_id: str, fold_idx: int) -> bytes: ...
    def derive_worker_seed(self: Any, run_id: str, fold_idx: int, worker_id: str) -> bytes: ...
    def derive_strategy_seed(self: Any, run_id: str, fold_idx: int, worker_id: str, strategy_id: str) -> bytes: ...
    def derive_asset_seed(self: Any, run_id: str, fold_idx: int, worker_id: str, strategy_id: str, asset_id: str) -> bytes: ...
    def seed_to_rng(self: Any, seed_bytes: bytes) -> 'np.random.Generator': ...
    def make_hashref(self: Any, seed_bytes: bytes) -> HashRef: ...
