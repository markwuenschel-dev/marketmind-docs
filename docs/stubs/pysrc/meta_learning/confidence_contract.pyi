from typing import Any

"""
MLN-03 canonical ``confidence_scalar`` semantics (single source of truth).

Default semantics (Phase II)
---------------------------
``confidence_scalar`` is **post-sizing attenuation only**:

    live_position = base_position * confidence_scalar

with ``confidence_scalar ∈ [0, 1]``. It may **reduce** exposure (including full abstention at 0).
It **must not** increase exposure above the base position from ``allocation_weights`` / ``SizingFn``.

**No hidden leverage:** values above 1 are invalid. Any change to default semantics requires an ADR
and threshold governance (MLN-07).

Routing boundary (non-default)
------------------------------
Uncertainty-aware **routing / rejection** is a **Phase II-0 pilot hypothesis**, not default
architecture. **Fail action:** remain **attenuation-only** plus the simpler risk path. Promotion
requires **earned** reject-set evidence (negative EV after costs) and incumbent positive EV there;
if attenuation already captures the economic effect, **do not promote routing**.

Use :func:`is_routing_enabled` — default is **False** unless both explicit pilot opt-in and earned
evidence flags are true.

Artifact surface
-----------------
Phase II ``meta_validity_report.json`` (governed MLN-06 path) carries a ``confidence_calibration``
block (schema ``mln03.confidence_calibration.v1``) with ECE / calibration / recalibration /
routing-pilot separation. See :func:`insufficient_confidence_calibration_block` and
:func:`validate_confidence_calibration_artifact_block`.
"""

CONFIDENCE_SCALAR_MIN: Final[float] = ...
CONFIDENCE_SCALAR_MAX: Final[float] = ...
CONFIDENCE_CALIBRATION_SCHEMA_VERSION: Final[str] = ...
REPORTING_GATE_PASS: Final[str] = ...
REPORTING_GATE_FAIL: Final[str] = ...
REPORTING_GATE_INSUFFICIENT: Final[str] = ...
def validate_confidence_scalar(value: float | int) -> float: ...
def apply_confidence_attenuation(*, base_position: float | int, confidence_scalar: float | int) -> float: ...
def is_routing_enabled(*, pilot_explicit_opt_in: bool = ..., reject_set_negative_evidence_after_costs: bool = ...) -> bool: ...
def insufficient_confidence_calibration_block(*, reason: str) -> dict[str, Any]: ...
def synthetic_confidence_calibration_pass_block(*, ece_value: float, calibration_method: str = ..., reliability_reference: str = ...) -> dict[str, Any]: ...
def validate_confidence_calibration_artifact_block(obj: Mapping[str, Any]) -> None: ...
