from typing import Any

"""
Ensemble model coordination.

Provides model composition strategies including stacking,
blending, and weighted averaging for prediction combination.

TODO: Registry hook for ensemble strategies.
TODO: Integration with model registry for member selection.
"""

class EnsembleStrategy(ABC):
    def combine(self: Any, predictions: Sequence[torch.Tensor]) -> torch.Tensor: ...
class EnsembleModel(ABC):
    def add_member(self: Any, model: nn.Module, weight: float = ...) -> None: ...
    def forward(self: Any, x: torch.Tensor) -> torch.Tensor: ...
