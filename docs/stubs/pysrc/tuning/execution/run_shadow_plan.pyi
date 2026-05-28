from typing import Any

"""
run_shadow_plan: run a candidate in shadow mode alongside the live strategy.
"""

def run_shadow_plan(candidate_id: str, live_strategy_id: str, context: dict[str, Any]) -> dict[str, Any]: ...
