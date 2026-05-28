from typing import Any

"""
preprocessor/core.py — public convenience API

Thin delegators to the graph engine via PreprocessorBuilder.
Public signatures preserved so existing callers do not break.

DO NOT add computational logic here.
Add ops to preprocessor/graph/ops.py and register them in the backend
registry instead.
"""

def load_ohlcv(path: Path, *, backend: Backend = ...) -> pl.DataFrame: ...
def add_returns(df: pl.DataFrame, column: str = ..., *, backend: Backend = ...) -> pl.DataFrame: ...
def add_sma(df: pl.DataFrame, column: str = ..., window: int = ..., *, backend: Backend = ...) -> pl.DataFrame: ...
def add_rsi(df: pl.DataFrame, column: str = ..., window: int = ..., *, backend: Backend = ...) -> pl.DataFrame: ...
def build_features(df: pl.DataFrame, *, sma_windows: list[int] | None = ..., rsi_window: int = ..., backend: Backend = ...) -> pl.DataFrame: ...
