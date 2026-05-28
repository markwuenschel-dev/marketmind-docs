pysrc.strategies.pipeline_strategy
==================================

.. py:module:: pysrc.strategies.pipeline_strategy


Attributes
----------

.. autoapisummary::

   pysrc.strategies.pipeline_strategy.OptunaTrial
   pysrc.strategies.pipeline_strategy.LOG
   pysrc.strategies.pipeline_strategy.SignalOutput
   pysrc.strategies.pipeline_strategy.StrategySignal
   pysrc.strategies.pipeline_strategy.FEATURE_OP_REGISTRY_VERSION


Exceptions
----------

.. autoapisummary::

   pysrc.strategies.pipeline_strategy.PipelineError
   pysrc.strategies.pipeline_strategy.ValidationError
   pysrc.strategies.pipeline_strategy.MaterializationError


Classes
-------

.. autoapisummary::

   pysrc.strategies.pipeline_strategy.TradeIntent
   pysrc.strategies.pipeline_strategy.SignalEnvelope
   pysrc.strategies.pipeline_strategy.StrategyContext
   pysrc.strategies.pipeline_strategy.RegimeDetector
   pysrc.strategies.pipeline_strategy.RiskManager
   pysrc.strategies.pipeline_strategy.PositionSizer
   pysrc.strategies.pipeline_strategy.FeatureStep
   pysrc.strategies.pipeline_strategy.FeaturePlan
   pysrc.strategies.pipeline_strategy.StrategySpec
   pysrc.strategies.pipeline_strategy.StrategyRegistry
   pysrc.strategies.pipeline_strategy.PipelineStrategy
   pysrc.strategies.pipeline_strategy.BacktestConfig
   pysrc.strategies.pipeline_strategy.SweepResult
   pysrc.strategies.pipeline_strategy.DriftState
   pysrc.strategies.pipeline_strategy.ChampionChallenger
   pysrc.strategies.pipeline_strategy.NullRegime
   pysrc.strategies.pipeline_strategy.LinearSizer
   pysrc.strategies.pipeline_strategy.TurnoverLimiterRisk
   pysrc.strategies.pipeline_strategy.BlendSpec
   pysrc.strategies.pipeline_strategy.LegacyBaseStrategy


Functions
---------

.. autoapisummary::

   pysrc.strategies.pipeline_strategy.feature_op_registry_version
   pysrc.strategies.pipeline_strategy.feature_op
   pysrc.strategies.pipeline_strategy.op_pct_change
   pysrc.strategies.pipeline_strategy.op_roll_mean
   pysrc.strategies.pipeline_strategy.op_roll_std
   pysrc.strategies.pipeline_strategy.op_ema
   pysrc.strategies.pipeline_strategy.op_zscore
   pysrc.strategies.pipeline_strategy.materialize_features
   pysrc.strategies.pipeline_strategy.backtest_portfolio
   pysrc.strategies.pipeline_strategy.parameter_sweep
   pysrc.strategies.pipeline_strategy.optuna_tune
   pysrc.strategies.pipeline_strategy.detect_drift
   pysrc.strategies.pipeline_strategy.blend


Module Contents
---------------

.. py:data:: OptunaTrial
   :type:  Any

.. py:data:: LOG
   :type:  Any

.. py:exception:: PipelineError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: ValidationError

   Bases: :py:obj:`PipelineError`


   Common base class for all non-exit exceptions.


.. py:exception:: MaterializationError

   Bases: :py:obj:`PipelineError`


   Common base class for all non-exit exceptions.


.. py:class:: TradeIntent

   .. py:attribute:: weights
      :type:  Union[pd.Series, pd.DataFrame]
      :value: Ellipsis



   .. py:attribute:: raw
      :type:  Mapping[str, object]
      :value: Ellipsis



   .. py:attribute:: diagnostics
      :type:  Mapping[str, object]
      :value: Ellipsis



.. py:data:: SignalOutput
   :type:  Any

.. py:class:: SignalEnvelope

   Bases: :py:obj:`Protocol`


   .. py:method:: signal()


.. py:data:: StrategySignal
   :type:  Any

.. py:class:: StrategyContext

   .. py:attribute:: prices
      :type:  Union[pd.Series, pd.DataFrame]
      :value: Ellipsis



   .. py:attribute:: features
      :type:  Optional[Union[pd.DataFrame, PolarsDataFrame]]
      :value: Ellipsis



   .. py:attribute:: timestamps
      :type:  Optional[pd.Index]
      :value: Ellipsis



   .. py:attribute:: asset_names
      :type:  Optional[List[str]]
      :value: Ellipsis



   .. py:attribute:: backend
      :type:  str
      :value: Ellipsis



   .. py:attribute:: cache_dir
      :type:  Union[str, Path]
      :value: Ellipsis



   .. py:attribute:: random_state
      :type:  int
      :value: Ellipsis



   .. py:attribute:: pit_provenance
      :type:  PitMeta | None
      :value: Ellipsis



   .. py:method:: validate()


.. py:class:: RegimeDetector

   Bases: :py:obj:`Protocol`


   .. py:method:: gate(features)


.. py:class:: RiskManager

   Bases: :py:obj:`Protocol`


   .. py:method:: clamp(weights, prices, **kwargs)


.. py:class:: PositionSizer

   Bases: :py:obj:`Protocol`


   .. py:method:: size(signal, **kwargs)


.. py:class:: FeatureStep

   .. py:attribute:: op
      :type:  str
      :value: Ellipsis



   .. py:attribute:: inputs
      :type:  Tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: args
      :type:  Tuple[Any, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: kwargs
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: out
      :type:  str
      :value: Ellipsis



.. py:data:: FEATURE_OP_REGISTRY_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:function:: feature_op_registry_version()

.. py:class:: FeaturePlan

   .. py:attribute:: steps
      :type:  Tuple[FeatureStep, Ellipsis]
      :value: Ellipsis



   .. py:method:: from_steps(steps)


   .. py:method:: signature()


.. py:function:: feature_op(name)

.. py:function:: op_pct_change(df, col, periods = ..., out = ...)

.. py:function:: op_roll_mean(df, col, window, minp = ..., out = ...)

.. py:function:: op_roll_std(df, col, window, minp = ..., out = ...)

.. py:function:: op_ema(df, col, span, adjust = ..., out = ...)

.. py:function:: op_zscore(df, col, window, minp = ..., out = ...)

.. py:function:: materialize_features(ctx, plan, price_col = ...)

.. py:class:: StrategySpec

   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: params
      :type:  Mapping[str, Any]
      :value: Ellipsis



.. py:class:: StrategyRegistry

   .. py:method:: register(name, strat_cls)


   .. py:method:: get(name)


   .. py:method:: clear_for_test()


.. py:class:: PipelineStrategy(**params)

   .. py:attribute:: regime
      :type:  Optional[RegimeDetector]
      :value: Ellipsis



   .. py:attribute:: risk
      :type:  Optional[RiskManager]
      :value: Ellipsis



   .. py:attribute:: sizer
      :type:  Optional[PositionSizer]
      :value: Ellipsis



   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


   .. py:method:: generate_trade_intent(ctx)


.. py:class:: BacktestConfig

   .. py:attribute:: cost_per_unit_turnover
      :type:  float
      :value: Ellipsis



   .. py:attribute:: leverage_cap
      :type:  float
      :value: Ellipsis



   .. py:attribute:: initial_nav
      :type:  float
      :value: Ellipsis



.. py:function:: backtest_portfolio(prices, weights, cfg)

.. py:class:: SweepResult

   .. py:attribute:: params
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: score
      :type:  float
      :value: Ellipsis



   .. py:attribute:: details
      :type:  Mapping[str, Any]
      :value: Ellipsis



.. py:function:: parameter_sweep(strategy_cls, param_grid, ctx, *, prices = ..., backtest_cfg = ..., n_jobs = ...)

.. py:function:: optuna_tune(strategy_cls, sampler_spec, ctx, *, prices = ..., backtest_cfg = ..., n_trials = ...)

.. py:class:: DriftState

   .. py:attribute:: ref_mean
      :type:  float
      :value: Ellipsis



   .. py:attribute:: ref_std
      :type:  float
      :value: Ellipsis



.. py:function:: detect_drift(series, st, threshold = ..., sensitivity = ...)

.. py:class:: ChampionChallenger

   .. py:attribute:: strategy_cls
      :type:  type[PipelineStrategy]
      :value: Ellipsis



   .. py:attribute:: ctx
      :type:  StrategyContext
      :value: Ellipsis



   .. py:attribute:: prices
      :type:  pd.DataFrame
      :value: Ellipsis



   .. py:attribute:: backtest_cfg
      :type:  BacktestConfig
      :value: Ellipsis



   .. py:attribute:: champion_params
      :type:  Dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: history
      :type:  List[Tuple[str, Dict[str, Any], float]]
      :value: Ellipsis



   .. py:method:: evaluate(params)


   .. py:method:: step(challenger_params, improvement = ...)


.. py:class:: NullRegime

   .. py:method:: gate(features)


.. py:class:: LinearSizer(scale = ..., clip = ...)

   .. py:method:: size(signal, **_)


.. py:class:: TurnoverLimiterRisk(max_turnover = ...)

   .. py:method:: clamp(weights, prices, **_)


.. py:class:: BlendSpec

   .. py:attribute:: parts
      :type:  List[Tuple[float, PipelineStrategy]]
      :value: Ellipsis



   .. py:method:: normalize()


.. py:function:: blend(ctx, spec)

.. py:class:: LegacyBaseStrategy(legacy_impl, **params)

   Bases: :py:obj:`PipelineStrategy`


   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


