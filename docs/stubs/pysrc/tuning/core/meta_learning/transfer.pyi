from typing import Any

"""
Transfer learning: extract search priors from past experiment memory.
"""

def build_transfer_prior(memory: ExperimentMemory, space_hash: str, dim_names: tuple[str, ...]) -> SearchPrior | None: ...
