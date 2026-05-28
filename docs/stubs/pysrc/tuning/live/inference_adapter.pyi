from typing import Any

"""
InferenceAdapter: translates live feature vectors into model predictions.
"""

class InferenceAdapter:
    def predict(self: Any, features: dict[str, Any], model_handle: Any) -> dict[str, Any]: ...
    def load_checkpoint(self: Any, artifact_hash: str) -> Any: ...
