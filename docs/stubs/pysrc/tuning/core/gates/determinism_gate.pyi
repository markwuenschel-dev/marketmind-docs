from typing import Any

"""
Determinism gate: verify that a result carries the required determinism tier.
"""

def passes_determinism_gate(actual_tier: str, required_tier: str) -> tuple[bool, str]: ...
