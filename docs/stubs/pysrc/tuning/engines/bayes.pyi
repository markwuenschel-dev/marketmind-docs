from typing import Any

"""
Bayesian optimisation engine using scikit-optimize (skopt).

Uses the functional ``skopt.gp_minimize`` API — not ``BayesSearchCV`` — because
the engine accepts a generic ``objective_fn(ParamPoint) -> float`` rather than an
sklearn estimator.

Invariants:
- skopt is an optional dependency; its import is deferred to the body of ``run()``.
  If unavailable, ``EngineNotAvailableError`` is raised with an actionable message.
  No module-level import of skopt (eliminates the soft-fail anti-pattern).
- skopt always *minimises*.  When ``spec.direction == "maximize"`` we negate the
  score for skopt and un-negate it in the returned TuningResult.
- ``spec.direction`` is preserved verbatim in TuningResult so downstream consumers
  see the sign-correct score.
- Param names are extracted from skopt named dimensions (``dim.name``), not from
  a non-existent ``space.param_names`` property.
- No print() — structured logging only.
"""

logger: structlog.stdlib.BoundLogger = ...
def run(spec: TunerSpec, space: 'SearchSpace', objective_fn: Callable[[ParamPoint], float]) -> TuningResult: ...
class BayesEngine:
    ...
