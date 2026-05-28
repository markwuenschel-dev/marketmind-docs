from typing import Any

"""
Benchmark: measure OnlineFeatureBuffer push and snapshot throughput.
"""

def bench_online_buffer(capacity: int = ..., n_pushes: int = ...) -> dict[str, float]: ...
