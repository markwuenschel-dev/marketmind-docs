from typing import Any

"""
Governed universe membership: relist-safe append-only event model.

Phase I-A operates at daily granularity (event_date is a date). Sub-day TTLs and
intraday restatement ordering are out of scope for this phase.

Membership is never inferred from price or store presence. A symbol is active at T iff
the latest membership event at or before T is a listing/activation event. Delist excludes
on and after delist_date. Same-date tie-break: when multiple events share the same
event_date, delist wins over list so that "exclude on and after delist_date" is deterministic.

Phase I convenience: FIXTURE_SEED is temporary; not the long-term governed security-master.
"""

class MembershipReasonCode(str, Enum):
    FIXTURE_SEED: Any
    GOVERNED: Any
    MANUAL: Any
    RELIST: Any
class Universe:
    def __init__(self: Any) -> None: ...
    def register(self: Any, symbol: str, list_date: date, *, reason_code: MembershipReasonCode = ...) -> None: ...
    def delist(self: Any, symbol: str, delist_date: date, *, reason_code: MembershipReasonCode = ...) -> None: ...
    def has_listing(self: Any, symbol: str) -> bool: ...
    def effective_state_at(self: Any, symbol: str, as_of_date: date) -> Tuple[bool, Optional[_Event]]: ...
    def members_as_of(self: Any, as_of_date: date) -> Set[str]: ...
