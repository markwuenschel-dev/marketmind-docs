from typing import Any

"""
CompositeScore: weighted combination of metrics plus penalty terms.
"""

def composite_score(metrics: dict[str, float], weights: dict[str, float], penalty_terms: list[float] | None = ...) -> float: ...
