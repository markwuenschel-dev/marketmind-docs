from typing import Any

logger: Any
pl: Any
pd: Any
dd: Any
class BatchPipeline:
    def __init__(self: Any, steps: List[PipelineStep], *, default_cfg: dict | None = ...) -> Any: ...
    def run(self: Any, data: Any, *, ctx: Optional[PipelineContext] = ..., distributed: Optional[str] = ..., collect: bool = ...) -> Any: ...
