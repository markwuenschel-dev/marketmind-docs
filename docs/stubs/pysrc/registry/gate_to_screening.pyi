from typing import Any

"""
Map marketmind_gate ValidationResult (gate_id + status) to ScreeningStage + ReasonCode.

Phase I: explicit mapping for files_exist, json_valid, sharpe_threshold, max_drawdown.
Pass and fail paths use the same stage per gate so funnel analytics are correct
(INTAKE twice, LANE_0 twice, not LANE_0 four times).
"""

GATE_STAGE_MAP: dict[str, ScreeningStage] = ...
GATE_FAIL_REASON_MAP: dict[str, ReasonCode] = ...
def gate_result_to_stage_and_code(gate_id: str, passed: bool, reason: Optional[str] = ...) -> Tuple[ScreeningStage, Optional[ReasonCode]]: ...
