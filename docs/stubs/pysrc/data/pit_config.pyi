from typing import Any

"""
Point-in-time (PIT) configuration: per-field policy (TTL, FillPolicy, MissingPolicy).

Phase I-A operates at daily granularity: TTL is expressed in integer days and staleness
is computed in days. Sub-day TTLs and quote-second resolution are out of scope for this phase.

Lookup order: exact field match -> namespace/glob match (e.g. price.*, fred.*) -> __default__.
resolve_field_config() returns a full config object per field, not just TTL.
"""

class FillPolicy(str, Enum):
    FORWARD: Any
    REJECT: Any
class MissingPolicy(str, Enum):
    WARN: Any
    FAIL: Any
class ResolvedFieldConfig:
    ttl_days: int = ...
    fill_policy: FillPolicy = ...
    missing_policy: MissingPolicy = ...
class FieldTTLConfig:
    default_config: ResolvedFieldConfig = ...
    field_configs: Dict[str, ResolvedFieldConfig] = ...
    namespace_configs: Dict[str, ResolvedFieldConfig] = ...
    def resolve_field_config(self: Any, field_name: str) -> ResolvedFieldConfig: ...
def resolve_field_config(field_name: str, config: FieldTTLConfig) -> ResolvedFieldConfig: ...
