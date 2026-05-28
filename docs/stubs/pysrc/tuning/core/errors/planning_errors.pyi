from typing import Any

"""
Typed planning and IR-lowering errors.
"""

class PlanningError(RuntimeError):
    ...
class LoweringError(PlanningError):
    ...
class InfeasiblePlanError(PlanningError):
    ...
