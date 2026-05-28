from typing import Any

"""
Pure deterministic sampler: draws candidates from a SearchSpace given a seed.
"""

def sample_uniform(space: SearchSpace, seed: int, n: int) -> list[dict[str, Any]]: ...
