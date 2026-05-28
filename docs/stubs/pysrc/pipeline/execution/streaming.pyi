from typing import Any

pl: Any
pd: Any
class StreamingPipeline:
    def __init__(self: Any, steps: Sequence[Any], config: Optional[Dict[str, Any]] = ...) -> Any: ...
    async def run(self: Any, data_stream: AsyncIterator[Any], context: Any) -> AsyncIterator[Any]: ...
