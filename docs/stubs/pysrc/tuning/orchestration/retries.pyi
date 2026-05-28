from typing import Any

"""
Retry utilities: exponential backoff with jitter for transient failures.
"""

T: Any
class MaxRetriesExceededError(RuntimeError):
    ...
class RetryPolicy:
    def __init__(self: Any, max_attempts: int = ..., initial_backoff: float = ..., max_backoff: float = ..., eta: float = ...) -> None: ...
def with_retries(fn: Callable[[], T], policy: RetryPolicy, retryable: type[Exception] = ...) -> T: ...
