from typing import Any

"""
ValidatorProtocol: interface for cross-validation strategies.
"""

class ValidatorProtocol(Protocol):
    def splits(self: Any, ir: 'ValidationIR', data: pd.Index) -> list[tuple[pd.Index, pd.Index]]: ...
    def n_splits(self: Any, ir: 'ValidationIR') -> int: ...
