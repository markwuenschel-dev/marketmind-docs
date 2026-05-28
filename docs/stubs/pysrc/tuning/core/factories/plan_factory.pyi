from typing import Any

"""
PlanFactory: build plan objects from IR + budget.
"""

def build_search_plan(ir: SearchIR, budget: ExecutionBudget, plan_hash: str) -> SearchPlan: ...
