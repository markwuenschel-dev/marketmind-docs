from typing import Any

"""
Multi-fidelity search: successive halving and Hyperband bracket logic.
"""

def successive_halving_brackets(max_trials: int, min_budget: int, max_budget: int, eta: int = ...) -> list[tuple[int, int]]: ...
