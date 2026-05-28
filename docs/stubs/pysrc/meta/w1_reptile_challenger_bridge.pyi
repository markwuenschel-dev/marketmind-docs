from typing import Any

"""
Bridge from a governed meta-allocator implementation to :class:`W1ChallengerSurface`.

Does **not** treat Reptile trainer smoke metrics as W1 scores. The allocator must expose
PIT-safe per-query scores via :class:`W1MetaAllocatorProtocol`.
"""

class W1ChallengerUnavailableError(Exception):
    def __init__(self: Any, message: str, *, details: dict[str, Any] | None = ...) -> None: ...
class W1MetaAllocatorProtocol(Protocol):
    def predict_query_scores(self: Any, task: MetaTask, *, fold_index: int) -> Sequence[float]: ...
def build_reptile_w1_challenger_surface(*, task_pool: Sequence[MetaTask], fold_plan: W1FoldPlan, trained_state: W1MetaAllocatorProtocol, task_pool_hash: str, data_fingerprint: str, splits_fingerprint: str, cost_assumptions_fingerprint: str, signal_set_version: str, created_at_utc: str, source: str = ..., model_family: str = ..., leakage_policy: str = ..., model_state_hash: str | None = ...) -> W1ChallengerSurface: ...
