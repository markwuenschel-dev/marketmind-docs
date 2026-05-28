from typing import Any

"""
PlannerProtocol: interface for IR → Plan lowering.
"""

class PlannerProtocol(Protocol):
    def lower(self: Any, ir: 'SearchIR') -> 'SearchPlan': ...
    def validate_plan(self: Any, plan: 'SearchPlan') -> bool: ...
