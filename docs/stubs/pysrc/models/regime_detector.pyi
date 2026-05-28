from typing import Any

"""
Market regime detection models.

Provides regime classification and change-point detection
for adaptive strategy behavior.

TODO: Registry hook for regime detector implementations.
TODO: Integration with BOCPD service for online detection.
"""

class RegimeDetector(ABC):
    def detect(self: Any, features: pd.DataFrame) -> pd.Series: ...
    def regime_change_prob(self: Any, window: pd.DataFrame) -> float: ...
