from typing import Any

"""
MarketMind canonical tuning subsystem.

All external callers should import from this package.  Do not import from
sub-modules directly — the sub-module layout is an implementation detail.

Quick start::

    from pysrc.tuning import tune, TunerSpec, TuningResult

    result = tune(
        my_objective,
        {"lr": (1e-4, 1e-1), "depth": [3, 5, 7]},
        engine="random",
        direction="maximize",
        budget=20,
        seed=42,
    )
"""

...
