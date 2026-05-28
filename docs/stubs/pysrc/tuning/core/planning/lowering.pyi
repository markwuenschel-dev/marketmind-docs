from typing import Any

"""
Lowering: pure functions that transform validated IR into executable plans.
"""

def lower_search_ir(ir: SearchIR, budget: ExecutionBudget, plan_hash: str) -> SearchPlan: ...
