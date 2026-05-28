from typing import Any

"""
Typed failures for MLC-5 proxy–IC alignment evidence (II-C).
"""

class ProxyAlignmentValidationError(ValueError):
    def __init__(self: Any, message: str, *, details: dict[str, Any] | None = ...) -> None: ...
class ArtifactImmutabilityError(RuntimeError):
    def __init__(self: Any, message: str, *, path: str | None = ...) -> None: ...
class InsufficientTaskPoolError(RuntimeError):
    def __init__(self: Any, message: str, *, details: dict[str, Any] | None = ...) -> None: ...
class ProxyArmDivergenceError(RuntimeError):
    def __init__(self: Any, message: str, *, details: dict[str, Any] | None = ...) -> None: ...
