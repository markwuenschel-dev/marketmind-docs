from typing import Any

"""
Pure objective-function adapter for the canonical tuning subsystem.

Migration path for ``pysrc.autotune.api.autotune`` and ``AutoTuner.run()``.

The old autotune API returned a non-canonical ``{"params": ..., "score": ...}``
dict.  This adapter accepts the same flexible input types as the old callers
and returns a canonical ``TuningResult``.

Invariants:
- No engine logic lives here — this is a thin boundary-translation layer.
- All search mechanics are delegated to ``tune()`` from ``pysrc.tuning.api``.
- No print() — structured logging only.
"""

logger: structlog.stdlib.BoundLogger = ...
def tune_objective(objective_fn: Callable[[ParamPoint], float], space: Union[SearchSpace, Dict[str, Any], List[Dict[str, Any]]], *, engine: str = ..., direction: ObjectiveDirection = ..., budget: int = ..., seed: Optional[int] = ...) -> TuningResult: ...
