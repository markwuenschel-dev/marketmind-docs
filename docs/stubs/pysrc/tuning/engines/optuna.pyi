from typing import Any

"""
Optuna-based hyperparameter search engine.

Migrates and canonicalises the legacy hyperparameter-search helper.
Uses ``space.to_optuna_space()`` to obtain the space definition and dispatches
each parameter to either ``trial.suggest_categorical`` (for lists with > 2 entries
or non-numeric values) or ``trial.suggest_float`` (for [low, high] continuous
ranges detected by the two-numeric-element convention in space.py).

Invariants:
- optuna is an optional dependency; its import is deferred to ``run()``.
  If unavailable, ``EngineNotAvailableError`` is raised with an actionable message.
- ``spec.direction`` is passed directly to ``optuna.create_study`` (optuna
  supports "maximize" and "minimize" natively).
- ``spec.seed`` seeds the TPE sampler if provided.
- ``spec.budget`` maps to ``n_trials``.
- No print() — structured logging only.
"""

logger: structlog.stdlib.BoundLogger = ...
def run(spec: TunerSpec, space: 'SearchSpace', objective_fn: Callable[[ParamPoint], float]) -> TuningResult: ...
class OptunaEngine:
    ...
