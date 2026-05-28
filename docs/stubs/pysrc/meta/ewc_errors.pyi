from typing import Any

"""
Typed failures for MLC-6 EWC forgetting harness (II-C evidence).
"""

class EWCValidationError(ValueError):
    def __init__(self: Any, message: str, *, details: dict[str, Any] | None = ...) -> None: ...
class ArtifactImmutabilityError(RuntimeError):
    def __init__(self: Any, message: str, *, path: str | None = ...) -> None: ...
class InsufficientTaskPoolError(RuntimeError):
    def __init__(self: Any, message: str, *, details: dict[str, Any] | None = ...) -> None: ...
class EWCDivergenceError(RuntimeError):
    def __init__(self: Any, message: str, *, details: dict[str, Any] | None = ...) -> None: ...
