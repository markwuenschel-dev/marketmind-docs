from typing import Any

logger: Any
def get_executor(backend: Literal['auto', 'polars', 'cudf', 'cpu', 'gpu'] = ...) -> Any: ...
