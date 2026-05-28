from typing import Any

"""
W1 clean evaluation-surface rerun pipeline.

This module rebuilds the governed W1 comparison as an explicit task-level surface:
one eval row per ``(fold_id, task_id)``, one scalar score per model per task, and
no reliance on post-hoc reconstruction from aggregate metrics.
"""

ALERT_DUPLICATE_TASK_ID_IN_TASK_UNIVERSE: Any
ALERT_MISSING_TASK_ID: Any
ALERT_MISSING_QUERY_TARGET: Any
ALERT_MISSING_PIT_BOUNDARY: Any
ALERT_SUPPORT_END_AFTER_QUERY_START: Any
ALERT_TASK_POOL_SIZE_MISMATCH: Any
ALERT_TRAIN_EVAL_OVERLAP: Any
ALERT_DUPLICATE_EVAL_TASK_ID_WITHIN_FOLD: Any
ALERT_MISSING_TRAIN_TASK_IDS_BY_FOLD: Any
ALERT_MISSING_EVAL_TASK_IDS_BY_FOLD: Any
ALERT_INSUFFICIENT_TRAIN_TASKS: Any
ALERT_INSUFFICIENT_EVAL_TASKS: Any
ALERT_FOLD_ORDERING_VIOLATION: Any
ALERT_MISSING_BASELINE_SCORE: Any
ALERT_DUPLICATE_BASELINE_SCORE_FOR_TASK: Any
ALERT_BASELINE_SCORED_TRAIN_TASK: Any
ALERT_BASELINE_MISSING_EVAL_TASK: Any
ALERT_BASELINE_USED_QUERY_LABELS: Any
ALERT_BASELINE_SPLIT_MISMATCH: Any
ALERT_MISSING_BASELINE_PREDICTION_ARTIFACT: Any
ALERT_MISSING_CHALLENGER_SCORE: Any
ALERT_DUPLICATE_CHALLENGER_SCORE_FOR_TASK: Any
ALERT_CHALLENGER_SCORED_TRAIN_TASK: Any
ALERT_CHALLENGER_MISSING_EVAL_TASK: Any
ALERT_CHALLENGER_USED_QUERY_LABELS: Any
ALERT_CHALLENGER_USED_XGBOOST_OUTPUTS_UNDECLARED: Any
ALERT_CHALLENGER_SPLIT_MISMATCH: Any
ALERT_REPEATED_QUERY_SCORE_ARRAY_WITHOUT_TASK_SCALAR: Any
ALERT_MANY_TO_ONE_JOIN_EXPANSION: Any
ALERT_ONE_TO_MANY_JOIN_EXPANSION: Any
ALERT_DUPLICATE_TASK_ID_IN_EVAL: Any
ALERT_BASELINE_CHALLENGER_TASK_SET_MISMATCH: Any
ALERT_FINGERPRINT_MISMATCH: Any
ALERT_TASK_LEVEL_TABLE_INVALID: Any
ALERT_INSUFFICIENT_EVAL_TASKS_FOR_METRICS: Any
ALERT_ROW_LEVEL_METRICS_USED_AS_TASK_LEVEL: Any
ALERT_MISSING_REQUIRED_METRIC_INPUT: Any
ALERT_TASK_COUNT_CLAIM_MISMATCH: Any
NO_DECISION_INVALID_EVAL_SURFACE: Any
SUPERSEDED_INVALID_EVAL_ALIGNMENT: Any
W1_CLEAN_REPORT_SCHEMA_VERSION: Any
class W1CleanRerunError(ValueError):
    ...
def build_w1_clean_task_universe(*, tasks: Sequence[MetaTask], task_query_targets: Mapping[str, float], task_support_targets: Mapping[str, float] | None, data_fingerprint: str, cost_assumptions_fingerprint: str, splits_fingerprint: str, task_pool_hash: str, cost_per_bar: float, expected_task_pool_size: int | None = ...) -> tuple[list[dict[str, object]], dict[str, object], dict[str, object]]: ...
def build_w1_clean_walk_forward_splits(*, tasks: Sequence[MetaTask], config: W1BaselineConfig) -> tuple[dict[str, object], dict[str, object], list[dict[str, object]]]: ...
def build_w1_clean_baseline_predictions(*, tasks: Sequence[MetaTask], splits_doc: Mapping[str, object], config: W1BaselineConfig, incumbent: Any, task_query_targets: Mapping[str, float], data_fingerprint: str, splits_fingerprint: str, cost_assumptions_fingerprint: str, task_pool_hash: str, prediction_time_utc: str) -> tuple[dict[str, object], dict[str, object]]: ...
def build_w1_clean_challenger_predictions(*, surface: W1ChallengerSurface, splits_doc: Mapping[str, object], challenger_model_id: str) -> tuple[dict[str, object], dict[str, object]]: ...
def build_w1_clean_comparison_table(*, task_universe_rows: Sequence[Mapping[str, object]], splits_doc: Mapping[str, object], baseline_doc: Mapping[str, object], challenger_doc: Mapping[str, object], expected_data_fingerprint: str, expected_splits_fingerprint: str, expected_cost_assumptions_fingerprint: str, expected_task_pool_hash: str) -> tuple[list[dict[str, object]], dict[str, object], list[dict[str, object]]]: ...
def audit_w1_task_level_comparison_rows(*, rows: Sequence[Mapping[str, object]], expected_eval_keys: Sequence[tuple[int, str]]) -> dict[str, object]: ...
def build_w1_clean_metrics(*, comparison_rows: Sequence[Mapping[str, object]], expected_eval_rows: int) -> tuple[dict[str, object], list[dict[str, object]], list[dict[str, object]], dict[str, object]]: ...
def build_w1_clean_gate_report(*, agent_1_audit: Mapping[str, object], agent_2_audit: Mapping[str, object], agent_3_audit: Mapping[str, object], agent_4_audit: Mapping[str, object], agent_5_audit: Mapping[str, object], agent_6_audit: Mapping[str, object], metrics_doc: Mapping[str, object], declared_unique_eval_tasks: int, declared_task_universe_size: int, run_id: str, data_fingerprint: str, splits_fingerprint: str, cost_assumptions_fingerprint: str, task_pool_hash: str) -> tuple[dict[str, object], str, dict[str, object], str]: ...
def run_w1_clean_rerun(*, output_dir: Path | None = ..., pool_cfg: W1RealPoolConfig | None = ..., seed: int = ..., timestamp_utc: str = ..., config: W1BaselineConfig | None = ..., challenger_model_id: str = ..., declared_task_universe_size: int = ...) -> dict[str, object]: ...
def run_default_w1_clean_rerun(*, output_root: Path | None = ..., output_dir: Path | None = ..., seed: int = ..., timestamp_utc: str = ...) -> dict[str, object]: ...
def main() -> None: ...
