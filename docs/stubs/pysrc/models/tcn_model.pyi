from typing import Any

"""
Temporal Convolutional Network models.

Provides TCN architectures for time-series modeling with
dilated convolutions and causal constraints.

TODO: Registry hook for TCN configurations.
TODO: Integration with ml/datasets for tensor preparation.
"""

class TCNModel(ABC):
    def forward(self: Any, x: torch.Tensor) -> torch.Tensor: ...
