from typing import Any

"""
Pareto front computation for multi-objective tuning.
"""

def is_pareto_efficient(scores: NDArray[np.float64]) -> NDArray[np.bool_]: ...
def pareto_front(candidates: list[dict[str, float]], objectives: list[str]) -> list[dict[str, float]]: ...
