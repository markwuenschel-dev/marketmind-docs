from typing import Any

"""
Typed failures for MLC-4 K-sweep evidence (II-C); no bare except swallowing.
"""

class KSweepValidationError(ValueError):
    def __init__(self: Any, message: str, *, details: dict[str, Any] | None = ...) -> None: ...
class InnerLoopDivergenceError(RuntimeError):
    def __init__(self: Any, message: str, *, details: dict[str, Any] | None = ...) -> None: ...
class ArtifactImmutabilityError(RuntimeError):
    def __init__(self: Any, message: str, *, path: str | None = ...) -> None: ...
