from typing import Any

"""
Random-sampling search engine.

Draws ``spec.budget`` candidate points from SearchSpace using the standard-library
``random.Random`` seeded from ``spec.seed``.  No sklearn dependency.

Invariants:
- spec.seed is the single source of reproducibility; we construct random.Random(seed)
  locally so global RNG state is never touched.
- spec.direction is the single source of truth for best-score tracking.
- Every evaluation produces a TrialRecord.
- No print() — structured logging only.
"""

logger: structlog.stdlib.BoundLogger = ...
def run(spec: TunerSpec, space: 'SearchSpace', objective_fn: Callable[[ParamPoint], float]) -> TuningResult: ...
class RandomEngine:
    ...
