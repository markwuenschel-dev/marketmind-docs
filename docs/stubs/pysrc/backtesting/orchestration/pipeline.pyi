from typing import Any

"""
Deprecated backtesting orchestration entry.

This module previously housed the Phase 0 ``BacktestPipeline`` stub.
It now exists solely as a compatibility shim that forwards to the
backtest suite runner in ``pysrc.backtesting.orchestration.suite_runner``.
"""

class BacktestPipeline(BacktestSuiteRunner):
    def __init__(self: Any, config: dict[str, Any] | None = ...) -> None: ...
