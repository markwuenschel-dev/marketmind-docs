from typing import Any

"""
SearchSpaceFactory: build SearchSpaceSpec from config dicts.
"""

def build_dimension_spec(raw: dict[str, Any]) -> DimensionSpec: ...
def build_search_space_spec(raw: dict[str, Any], spec_hash: str) -> SearchSpaceSpec: ...
