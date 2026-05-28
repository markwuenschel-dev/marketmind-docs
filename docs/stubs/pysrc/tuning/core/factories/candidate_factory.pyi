from typing import Any

"""
CandidateFactory: enumerate candidate hyperparameter sets from a SearchSpaceSpec.
"""

def enumerate_grid(space: SearchSpaceSpec, seed: int) -> list[dict[str, object]]: ...
