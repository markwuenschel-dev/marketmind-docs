from typing import Any

"""
Graph Neural Network models.

Provides GNN architectures for relational data including
market graphs, supply chains, and correlation networks.

TODO: Registry hook for GNN architectures.
TODO: Graph construction utilities for market data.
"""

class GNNModel(ABC):
    def forward(self: Any, data: pyg_data.Data) -> torch.Tensor: ...
