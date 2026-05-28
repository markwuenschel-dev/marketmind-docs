from typing import Any

"""
UTC-aware time utilities; never returns naive datetimes.

Centralises time access so tests can monkey-patch a single call site.
"""

def utc_now() -> datetime: ...
def monotonic_ns() -> int: ...
