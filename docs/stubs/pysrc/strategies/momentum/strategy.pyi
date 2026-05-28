from typing import Any

"""
Governed momentum strategies on the canonical pipeline path (Programming Guidelines §3.4, §4.3).

Plans are produced only through the ``_PLAN_BUILDERS`` factory table. Signal generation
reads materialized features plus ``StrategyContext.pit_provenance`` when governed; it does
not open raw datasets.
"""

PlanBuilder: Any
class MomentumStrategy(PipelineStrategy):
    def __init__(self: Any, *, variant: str = ..., **params: Any) -> None: ...
    def features_plan(self: Any) -> FeaturePlan: ...
    def generate_signal(self: Any, features: pd.DataFrame | 'pl.DataFrame') -> AlphaIR: ...
    def generate_trade_intent(self: Any, ctx: StrategyContext) -> TradeIntent: ...
