from typing import Any

"""
GpuBatchExecutor: batches tasks for GPU inference (requires torch/cuda).
"""

class GpuBatchExecutor:
    def __init__(self: Any, device: str = ..., batch_size: int = ...) -> None: ...
    def map(self: Any, fn: Callable[[dict[str, Any]], dict[str, Any]], tasks: list[dict[str, Any]]) -> list[dict[str, Any]]: ...
