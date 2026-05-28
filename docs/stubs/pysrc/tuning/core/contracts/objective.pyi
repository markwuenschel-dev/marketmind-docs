from typing import Any

"""
ObjectiveProtocol: interface for objective/scoring functions.
"""

class ObjectiveProtocol(Protocol):
    def score(self: Any, ir: 'ObjectiveIR', returns: pd.Series) -> float: ...
    def is_feasible(self: Any, ir: 'ObjectiveIR', returns: pd.Series) -> bool: ...
