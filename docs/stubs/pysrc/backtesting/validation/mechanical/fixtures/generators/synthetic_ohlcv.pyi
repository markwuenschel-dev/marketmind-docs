from typing import Any

"""
py/backtesting/validation/mechanical/fixtures/generators/synthetic_ohlcv.py

Deterministic synthetic OHLCV generator for unit / integration tests.
Uses a seeded random walk so the same call always produces the same data.

Usage::

    from pysrc.backtesting.validation.mechanical.fixtures.generators.synthetic_ohlcv import (
        generate_ohlcv,
    )

    df = generate_ohlcv(n_rows=252, seed=42)
"""

def generate_ohlcv(n_rows: int = ..., *, start_price: float = ..., daily_vol: float = ..., start_date: date | None = ..., seed: int = ...) -> pl.DataFrame: ...
