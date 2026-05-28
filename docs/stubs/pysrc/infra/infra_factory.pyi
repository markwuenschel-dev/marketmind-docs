from typing import Any

"""
Lightweight, import-safe registry + factory for data sources.

- No import-time side effects (no top-level lookups or context managers).
- Thread-safe register/unregister.
- Exposes both a modern factory class and a legacy 'creator' callable.
"""

def register_source(name: str, creator: _Source) -> None: ...
def unregister_source(name: str) -> None: ...
def get_creator(source_type: str) -> Optional[_Source]: ...
def list_sources() -> list[str]: ...
class DataSourceFactory:
    def create(source_type: str, **kwargs: Any) -> Any: ...
creator: Any
