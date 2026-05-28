from typing import Any

"""
Bayesian optimisation primitives: acquisition function utilities.
"""

class BayesOptError(RuntimeError):
    ...
def expected_improvement(mu: float, sigma: float, best_so_far: float, xi: float = ...) -> float: ...
