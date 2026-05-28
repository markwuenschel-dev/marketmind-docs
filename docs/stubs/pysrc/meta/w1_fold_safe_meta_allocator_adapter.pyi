from typing import Any

"""
Protocol plumbing: fold-safe PIT-legal scores for W1 integration tests only.

This is **not** learned challenger state and must **never** satisfy W1 gate closure eligibility.
Use :class:`~pysrc.meta.w1_reptile_trained_meta_allocator_adapter.ReptileTrainedMetaAllocatorAdapter`
(or another checkpoint-backed implementation) for closure-eligible learned surfaces.
"""

class W1FoldSafeSupportOnlyMetaAllocator:
    state_fingerprint: str = ...
    def predict_query_scores(self: Any, task: MetaTask, *, fold_index: int) -> tuple[float, ...]: ...
