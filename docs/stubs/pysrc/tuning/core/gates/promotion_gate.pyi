from typing import Any

"""
Promotion gate: composite check that a candidate is safe to promote.
"""

def evaluate_promotion_gate(dsr: float, t_stat: float, pit_ok: bool, determinism_ok: bool, dsr_threshold: float = ..., t_stat_min: float = ...) -> tuple[bool, dict[str, bool]]: ...
