from typing import Any

"""
ModelStore: atomic persistence for serialised model checkpoints.
"""

class ModelStore:
    def __init__(self: Any) -> None: ...
    def save(self: Any, job_id: str, candidate_id: str, model: Any) -> None: ...
    def load(self: Any, job_id: str, candidate_id: str) -> Any | None: ...
