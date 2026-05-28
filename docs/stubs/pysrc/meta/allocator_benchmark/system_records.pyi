from typing import Any

"""
System-record population for W2-v1 allocator benchmark reports.
"""

W2_V1_CHALLENGER_SKIP_REASON: Any
def build_w2_v1_baseline_system_records(decision_rows: pd.DataFrame) -> dict[str, dict[str, object]]: ...
def build_w2_v1_challenger_system_records() -> dict[str, dict[str, object]]: ...
def build_w2_system_record(*, system_id: str, system_type: str, metrics: dict[str, object], status: str, reason: str) -> dict[str, object]: ...
