from typing import Any

"""
Typed determinism tier errors.
"""

class DeterminismError(ValueError):
    ...
class TierDowngradeError(DeterminismError):
    ...
class InvalidTierError(DeterminismError):
    ...
