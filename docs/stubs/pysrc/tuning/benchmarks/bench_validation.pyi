from typing import Any

"""
Benchmark: measure throughput of purged cross-validation split generation.
"""

def bench_purged_splits(n_obs: int = ..., n_splits: int = ..., embargo_periods: int = ...) -> dict[str, float]: ...
