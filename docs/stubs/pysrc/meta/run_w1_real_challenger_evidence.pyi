from typing import Any

"""
Compute harness helpers for the governed W1 real lane + optional challenger surface.

Full YAML-driven evidence runs are not required for CI; integration tests exercise
:func:`~pysrc.meta.reptile_trainer_benchmark.run_real_w1_baseline_evidence` end-to-end.
"""

def w1_real_challenger_cache_key(*, task_pool_hash: str, model_state_hash: str, data_fingerprint: str, splits_fingerprint: str, cost_assumptions_fingerprint: str, code_version: str) -> str: ...
def main() -> None: ...
