from typing import Any

"""
Capacity constraints: scale scores by AUM capacity decay factor.
"""

def capacity_decay_factor(aum: float, half_capacity: float) -> float: ...
def apply_capacity_penalty(score: float, aum: float, half_capacity: float) -> float: ...
