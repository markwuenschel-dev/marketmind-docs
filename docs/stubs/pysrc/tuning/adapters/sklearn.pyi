from typing import Any

"""
sklearn estimator adapter for the canonical tuning subsystem.

Migration path for the three retired functions:
- ``pysrc.tuning.grid_search.run_grid_search``
- ``pysrc.tuning.random_search.run_random_search``
- ``pysrc.tuning.bayesian_optimization.run_bayes_search``

All three are replaced by a single ``tune_estimator()`` function that delegates
to the canonical ``tune()`` engine.

Invariants:
- sklearn is required for this adapter; it is an explicit dependency.
  ``cross_val_score`` and ``clone`` are used from sklearn.
- ``best_model`` in the returned TuningResult is the estimator *refitted* on
  the full training data with the best parameters found.
- ``spec.direction`` governs score interpretation; all other engine behaviour
  is encapsulated by ``tune()``.
- No print() — structured logging only.
"""

logger: structlog.stdlib.BoundLogger = ...
def tune_estimator(estimator: Any, space: SearchSpace | dict[str, Any] | list[dict[str, Any]], X_train: Any, y_train: Any, *, engine: str = ..., direction: ObjectiveDirection = ..., budget: int = ..., cv: int = ..., scoring: str | None = ..., seed: int | None = ...) -> TuningResult: ...
