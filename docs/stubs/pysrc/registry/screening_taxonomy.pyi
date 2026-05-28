from typing import Any

"""
Screening taxonomy: stages, statuses, reason codes, and REASON_CODE_TO_FAMILY.

Contract: reason_family is always derived from REASON_CODE_TO_FAMILY; callers never
pass reason_family. Builders and producers look up via REASON_CODE_TO_FAMILY[reason_code].
"""

class ScreeningStage(str, Enum):
    INTAKE: Any
    LANE_0: Any
    LANE_1: Any
    LANE_2: Any
    PROMOTION: Any
class ScreeningStatus(str, Enum):
    ACCEPTED: Any
    REJECTED: Any
    ERROR: Any
    SKIPPED: Any
class ReasonFamily(str, Enum):
    SPEC: Any
    DATA: Any
    DUPLICATE: Any
    INVARIANT: Any
    STAT_VALIDITY: Any
    COST: Any
    STABILITY: Any
    PROMOTION: Any
    SYSTEM: Any
class ReasonCode(str, Enum):
    SPEC_INVALID: Any
    SCHEMA_VALIDATION_FAIL: Any
    DUPLICATE_SPEC_HASH: Any
    DATA_UNAVAILABLE: Any
    UNSUPPORTED_INPUT_DOMAIN: Any
    PROVENANCE_REFERENCE_MISSING: Any
    RESOURCE_BUDGET_EXCEEDED: Any
    INVARIANT_PRECHECK_FAIL: Any
    IC_BELOW_THRESHOLD: Any
    DSR_P_ABOVE_CUTOFF: Any
    PBO_ABOVE_CUTOFF: Any
    HARVEY_T_BELOW_CUTOFF: Any
    COST_MODEL_FAIL: Any
    LEAKAGE_INVARIANT_VIOLATION: Any
    FEATURE_STABILITY_FAIL: Any
    REGIME_COVERAGE_FAIL: Any
    ANTI_GOODHART_FAIL: Any
    BASELINE_REGRESSION: Any
    PROMOTION_VETO: Any
REASON_CODE_TO_FAMILY: Dict[ReasonCode, ReasonFamily] = ...
