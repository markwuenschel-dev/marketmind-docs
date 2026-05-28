from typing import Any

"""
Benchmark: measure throughput of the deterministic uniform sampler.
"""

def bench_sample_uniform(n_dims: int = ..., n_samples: int = ..., seed: int = ...) -> dict[str, float]: ...
