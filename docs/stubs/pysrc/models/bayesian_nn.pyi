from typing import Any

"""
Bayesian Neural Network models.

Provides probabilistic deep learning with uncertainty
quantification for risk-aware predictions.

TODO: Registry hook for BNN architectures.
TODO: Integration with tuning for hyperparameter search.
"""

class BayesianNN(ABC):
    def forward(self: Any, x: torch.Tensor) -> tuple[torch.Tensor, torch.Tensor]: ...
