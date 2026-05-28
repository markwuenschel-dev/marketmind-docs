from typing import Any

"""
Transformer models for time-series.

Provides attention-based architectures including Informer,
Autoformer, and standard Transformers for financial forecasting.

TODO: Registry hook for transformer variants.
TODO: Integration with positional encoding for time features.
"""

class TransformerModel(ABC):
    def forward(self: Any, x: torch.Tensor, mask: torch.Tensor | None = ...) -> torch.Tensor: ...
