from typing import Any

"""
W1 ranking-vs-expression decomposition diagnostics.

This module consumes only the canonical task-level comparison table and separates
ranking quality from portfolio-expression quality without altering the governed
W1 gate or model-comparison decision.
"""

ALERT_MISSING_BASELINE_SCORE_FOR_DECOMPOSITION: Any
ALERT_MISSING_CHALLENGER_SCORE_FOR_DECOMPOSITION: Any
ALERT_MISSING_QUERY_GROSS_UTILITY_FOR_DECOMPOSITION: Any
ALERT_MISSING_QUERY_NET_UTILITY_FOR_DECOMPOSITION: Any
ALERT_MISSING_QUERY_TURNOVER_FOR_DECOMPOSITION: Any
ALERT_MISSING_FOLD_ID_FOR_DECOMPOSITION: Any
ALERT_MISSING_TASK_ID_FOR_DECOMPOSITION: Any
ALERT_MISSING_REGIME_CLASS_FOR_DECOMPOSITION: Any
ALERT_INVALID_WEIGHT_SUM_FOR_DECOMPOSITION: Any
W1_RANKING_EXPRESSION_DECOMPOSITION_SCHEMA_VERSION: Any
DEFAULT_THRESHOLD_PERCENTILES: Any
DEFAULT_TOP_K_VALUES: Any
DEFAULT_COST_PENALTY_LAMBDAS: Any
DEFAULT_BUCKET_LABELS: Any
DEFAULT_DECILE_LABELS: Any
TARGET_SURFACES: Any
DEFAULT_TRANSFORMS: Any
def build_w1_ranking_vs_expression_decomposition(*, comparison_rows: Sequence[Mapping[str, object]], run_identity: Mapping[str, object], threshold_percentiles: Sequence[float] = ..., top_k_values: Sequence[int] = ..., cost_penalty_lambdas: Sequence[float] = ...) -> tuple[dict[str, object], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], list[dict[str, object]], str, dict[str, object]]: ...
