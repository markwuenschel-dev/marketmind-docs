from typing import Any

"""
DataView: the single point-in-time (PIT) front door for mutable data access.

- as_of() uses snapshot semantics: one row per symbol as known at knowledge_date.
- Visible rows satisfy valid_time <= T and knowledge_time <= T.
- Phase I-A operates at daily granularity: canonical temporal columns are normalized to date;
  sub-day TTLs and intraday restatement ordering are out of scope for this phase.
- Non-bitemporal input fails closed. Symbol identity is validated at registration time.
"""

class DataView:
    def __init__(self: Any, universe: Optional[Universe] = ..., pit_config: Optional[FieldTTLConfig] = ..., *, pit_required: bool = ...) -> None: ...
    def register_source(self: Any, df: pd.DataFrame, *, valid_time_col: str = ..., knowledge_time_col: str = ..., seed_fixture_membership: bool = ...) -> None: ...
    def as_of(self: Any, symbols: Sequence[str], fields: Sequence[str], knowledge_date: date) -> pd.DataFrame: ...
    def universe_as_of(self: Any, knowledge_date: date, filters: Optional[Any] = ...) -> Set[str]: ...
