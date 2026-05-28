from typing import Any

"""
Weather and environmental data integration.

Provides typed contracts for meteorological data sources
including forecasts, historical observations, and climate indices.

TODO: Registry hook for weather data providers.
TODO: Integration with strategy features for weather signals.
"""

class WeatherDataSpec:
    station_id: str = ...
    variables: list[str] = ...
    frequency: str = ...
    date_range: tuple[str, str] = ...
class WeatherDataProvider(ABC):
    def fetch(self: Any, spec: WeatherDataSpec) -> Mapping[str, Any]: ...
