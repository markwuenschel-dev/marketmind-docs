from typing import Any

"""
Typed errors for the W2 allocator benchmark contract.
"""

class W2AllocatorBenchmarkError(ValueError):
    ...
class W2AllocatorBenchmarkConfigError(W2AllocatorBenchmarkError):
    ...
class W2AllocatorBenchmarkSchemaError(W2AllocatorBenchmarkError):
    ...
