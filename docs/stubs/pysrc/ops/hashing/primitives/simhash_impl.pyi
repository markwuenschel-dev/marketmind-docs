from typing import Any

"""
py/ops/hashing/primitives/simhash_impl.py
═════════════════════════════════════════════
SimHash-128 for dense vector approximate similarity (HashPurpose.LSH_VECTOR_SIMHASH).

ADR-007 v1.1 §5.7 — Statistical Bounds

  Hamming similarity → cosine similarity mapping:
    P(h(a) == h(b)) = 1 − θ(a,b)/π
    where θ(a,b) = arccos(a·b / (‖a‖·‖b‖))

  For a 128-bit SimHash:
    E[agreement] = 1 − θ/π
    Var[agreement] = θ(π−θ) / (128π²)
    StdErr at θ=45°: σ ≈ 0.044  (±4.4 percentage points, 1σ)

  ERROR BOUND REQUIREMENT:
    At ≥ 128 bits, worst-case std dev ≤ 0.0442 (ADR-007 v1.1 §5.7).
    64-bit SimHash produces std dev ≤ 0.0625 — INSUFFICIENT for production gates.
    Use 256 bits only if statistical gate requires σ ≤ 0.031.

PROJECTION SEED (ADR-007 v1.1 §5.7 §D — CORRECTED v1.1)
  Hyperplane seed: HMAC(master_seed, 'mm/simhash/v1' || u32be(dim) || u32be(bit_index))

  The dim field is MANDATORY.  Without it:
    A 500-dim and 501-dim space produce IDENTICAL hyperplane bytes for bit 0.
    This creates silent false-similarity: cosine(0.0) may be reported for unrelated vectors.

INPUT CANONICALIZATION (ADR-007 v1.1 §5.7 §C)
  Dense float64 input → int16 fixed-point:
    v_q = round(v * 2¹⁵)  clipped to [−2¹⁵, 2¹⁵ − 1]
  Wire format: u32be(dim) || i16be(v₀) || i16be(v₁) || ... || i16be(v_{d-1})
  NaN in any component → HARD REJECTION (CanonicalValueRejected).

PERFORMANCE BOUNDS
  SimHash at d=500:
    Hyperplane generation: ~12 μs (HMAC per bit, cached after first call)
    Hash of one vector:    ~16 μs
    Hamming distance:      ~1 ns  (XOR + popcount)
  Precompute hyperplane matrix per (master_seed, dim) pair.  Cache it.

BANNED
  Non-HMAC hyperplane seeds     : np.random.default_rng without HMAC seed is D2 only.
  Omitting dim from seed context : Silent false similarity as described above.
  Non-int16 quantization         : Floating-point comparison is not a hash operation.
  Using SimHash for identity CAS : LSH is approximate; never a content-addressed ID.
"""

class SimHash128:
    def __init__(self: Any, master_seed: bytes, dim: int) -> None: ...
    def quantize_vector(self: Any, vec: np.ndarray) -> np.ndarray: ...
    def encode_quantized_vector(self: Any, q_vec: np.ndarray) -> bytes: ...
    def hash_vector(self: Any, vec: np.ndarray) -> tuple[int, bytes]: ...
    def make_hashref(self: Any, raw_bytes: bytes) -> HashRef: ...
    def hamming_distance(a_int: int, b_int: int) -> int: ...
    def estimated_cosine_similarity(hamming: int, n_bits: int = ...) -> float: ...
