from typing import Any

"""
Legacy YAML grid adapter for the canonical tuning subsystem.

Migration path for the legacy list-of-dicts hyperparameter-search helpers.

These functions consumed a list-of-dicts YAML format and either yielded raw
param dicts or built a flat categorical dict for optuna.  This adapter replaces
both with a single conversion function that produces a canonical SearchSpace.

The list-of-dicts format is:
    [{"lr": [0.01, 0.001]}, {"depth": [3, 5, 7]}, ...]

Each element is a dict mapping a parameter name to its list of candidate values.
Parameter names must be unique across the list.

Invariants:
- This is a pure conversion function — no engine logic, no side effects.
- Delegating to ``normalize_space()`` ensures that validation rules (unique
  param names, valid value types) are enforced in one place.
- No print() — structured logging only.
"""

logger: structlog.stdlib.BoundLogger = ...
def parse_yaml_grid(grid: List[Dict[str, Any]]) -> SearchSpace: ...
