from typing import Any

"""
Model training coordinator.

Provides standardized training loops with early stopping,
checkpointing, and deterministic seeding.

TODO: Registry hook for training strategies.
TODO: Integration with artifact registry for checkpoint storage.
"""

class TrainConfig:
    epochs: int = ...
    batch_size: int = ...
    learning_rate: float = ...
    early_stop_patience: int = ...
    seed: int = ...
class ModelTrainer(ABC):
    def train(self: Any, model: nn.Module, config: TrainConfig, *, on_epoch: Callable[[int, float], None] | None = ...) -> nn.Module: ...
