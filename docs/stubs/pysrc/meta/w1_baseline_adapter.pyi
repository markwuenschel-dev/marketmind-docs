from typing import Any

"""
W1 bounded baseline → governed ``baseline_comparison.v1`` payload (integration-only).
"""

class W1AdapterError(ValueError):
    ...
def build_baseline_comparison(w1_result: W1BaselineResult, challenger_run_id: str, task_pool_hash: str) -> dict[str, Any]: ...
