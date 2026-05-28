from typing import Any

"""
Evolutionary search primitives: selection, crossover, and mutation.
"""

def tournament_select(population: list[tuple[dict[str, Any], float]], k: int, seed: int) -> dict[str, Any]: ...
def uniform_crossover(parent_a: dict[str, Any], parent_b: dict[str, Any], seed: int) -> dict[str, Any]: ...
