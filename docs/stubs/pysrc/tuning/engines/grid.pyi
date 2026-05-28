from typing import Any

"""
Pure cartesian-grid search engine.

No sklearn dependency — this module enumerates SearchSpace.iter_grid() exhaustively
and evaluates the objective function for every parameter combination.  The seed
field on TunerSpec is ignored because grid search is deterministic by construction.

Invariants:
- spec.direction is the single source of truth for best-score tracking.
- Every evaluation produces a TrialRecord; none are silently skipped.
- No print() — structured logging only.
"""

logger: structlog.stdlib.BoundLogger = ...
def run(spec: TunerSpec, space: 'SearchSpace', objective_fn: Callable[[ParamPoint], float]) -> TuningResult: ...
class GridEngine:
    ...
