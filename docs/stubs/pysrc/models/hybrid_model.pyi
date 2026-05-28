from typing import Any

"""
Hybrid model architectures.

Combines multiple model types (e.g., LSTM + Transformer)
for ensemble-like behavior within a single model.

TODO: Registry hook for hybrid architectures.
TODO: Weight sharing and fusion strategy selection.
"""

class HybridModel(ABC):
    def forward(self: Any, x: torch.Tensor) -> torch.Tensor: ...
