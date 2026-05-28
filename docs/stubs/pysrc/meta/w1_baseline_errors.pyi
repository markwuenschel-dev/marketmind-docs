from typing import Any

"""
Typed errors for the WS-1 bounded baseline harness (II-C).
"""

class W1BaselineEvidenceError(ValueError):
    def __init__(self: Any, message: str, *, details: dict[str, Any] | None = ...) -> None: ...
class W1XGBoostDependencyError(W1BaselineEvidenceError):
    ...
