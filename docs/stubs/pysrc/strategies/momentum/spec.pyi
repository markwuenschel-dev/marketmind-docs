from typing import Any

"""
Typed momentum strategy boundary (Programming Guidelines §3.3, §3.4).

Variant names and coerced parameter dict feed the canonical ``_PLAN_BUILDERS`` factory
table in ``MomentumStrategy``. Unknown keys are preserved for forward-compatible plans.
"""

MOMENTUM_VARIANTS: Final[frozenset[str]] = ...
def build_momentum_params(variant: str, params: Mapping[str, Any] | None = ...) -> dict[str, Any]: ...
