from typing import Any

"""
Satellite and alternative data integration.

Provides typed contracts for non-traditional data sources
including satellite imagery, social sentiment, and IoT feeds.

TODO: Registry hook for alternative data providers.
TODO: Schema validation for satellite data formats.
"""

class SatelliteDataSpec:
    provider: str = ...
    region: str = ...
    date_range: tuple[str, str] = ...
    resolution: int = ...
class SatelliteDataProvider(ABC):
    def fetch(self: Any, spec: SatelliteDataSpec) -> Mapping[str, Any]: ...
