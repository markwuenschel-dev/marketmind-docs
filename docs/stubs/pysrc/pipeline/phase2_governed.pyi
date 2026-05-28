from typing import Any

PHASE2_GOVERNED_EVIDENCE_SUBDIR: Any
PHASE2_GOVERNED_SUMMARY_FILENAME: Any
PHASE2_GOVERNED_SUMMARY_SCHEMA: Any
def emit_governed_phase2_orchestration_evidence(*, bundle_dir: Path, strategy_id: str, run_id: str, strategy_context: StrategyContext | None, source_prices: pd.DataFrame | None, features: pd.DataFrame | None, signals: Any, run_metadata: Mapping[str, Any] | None = ...) -> dict[str, Any]: ...
