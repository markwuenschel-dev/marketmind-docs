pysrc.strategies.adaptive_strategy_engine
=========================================

.. py:module:: pysrc.strategies.adaptive_strategy_engine


Attributes
----------

.. autoapisummary::

   pysrc.strategies.adaptive_strategy_engine.LOG


Classes
-------

.. autoapisummary::

   pysrc.strategies.adaptive_strategy_engine.DriftState
   pysrc.strategies.adaptive_strategy_engine.EvolutionEvent
   pysrc.strategies.adaptive_strategy_engine.EvolutionCallback
   pysrc.strategies.adaptive_strategy_engine.AdaptiveParameterSpace
   pysrc.strategies.adaptive_strategy_engine.MultiFrameDriftState
   pysrc.strategies.adaptive_strategy_engine.MultiTimeframeDriftMonitor
   pysrc.strategies.adaptive_strategy_engine.StrategyEnsemble
   pysrc.strategies.adaptive_strategy_engine.SelfEvolvingAdapter
   pysrc.strategies.adaptive_strategy_engine.LoggingEvolutionCallback
   pysrc.strategies.adaptive_strategy_engine.FileEvolutionCallback


Functions
---------

.. autoapisummary::

   pysrc.strategies.adaptive_strategy_engine.create_evolving_system


Module Contents
---------------

.. py:class:: DriftState

   .. py:attribute:: ref_mean
      :type:  float
      :value: Ellipsis



   .. py:attribute:: ref_std
      :type:  float
      :value: Ellipsis



.. py:data:: LOG
   :type:  Any

.. py:class:: EvolutionEvent

   .. py:attribute:: timestamp
      :type:  pd.Timestamp
      :value: Ellipsis



   .. py:attribute:: event_type
      :type:  str
      :value: Ellipsis



   .. py:attribute:: strategy_name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: old_params
      :type:  Dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: new_params
      :type:  Dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: performance_delta
      :type:  float
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  Dict[str, Any]
      :value: Ellipsis



.. py:class:: EvolutionCallback

   Bases: :py:obj:`Protocol`


   .. py:method:: on_evolution_event(event)


.. py:class:: AdaptiveParameterSpace(base_space, adaptation_rate = ..., memory_length = ...)

   .. py:method:: update(params, score)


   .. py:method:: evolve_space()


.. py:class:: MultiFrameDriftState

   .. py:attribute:: short_term
      :type:  Optional[DriftState]
      :value: Ellipsis



   .. py:attribute:: medium_term
      :type:  Optional[DriftState]
      :value: Ellipsis



   .. py:attribute:: long_term
      :type:  Optional[DriftState]
      :value: Ellipsis



.. py:class:: MultiTimeframeDriftMonitor(short_window = ..., medium_window = ..., long_window = ..., sensitivity = ...)

   .. py:method:: check_drift(returns)


.. py:class:: StrategyEnsemble(strategies, rebalance_frequency = ...)

   .. py:method:: update_performance(strategy_name, score)


   .. py:method:: should_rebalance()


   .. py:method:: rebalance_weights()


.. py:class:: SelfEvolvingAdapter(strategies, ctx, prices, evolution_frequency = ..., optimization_trials = ..., min_history_for_evolution = ..., backtest_cfg = ..., callbacks = ...)

   .. py:method:: generate_trade_intent()


   .. py:method:: get_evolution_summary()


   .. py:method:: force_evolution(strategy_name = ...)


.. py:class:: LoggingEvolutionCallback

   .. py:method:: on_evolution_event(event)


.. py:class:: FileEvolutionCallback(filepath)

   .. py:method:: on_evolution_event(event)


.. py:function:: create_evolving_system(price_data)

