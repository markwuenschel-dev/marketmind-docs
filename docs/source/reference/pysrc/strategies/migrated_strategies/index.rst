pysrc.strategies.migrated_strategies
====================================

.. py:module:: pysrc.strategies.migrated_strategies


Attributes
----------

.. autoapisummary::

   pysrc.strategies.migrated_strategies.LOG
   pysrc.strategies.migrated_strategies.DISABLE_CACHE
   pysrc.strategies.migrated_strategies.DISABLE_NUMBA


Classes
-------

.. autoapisummary::

   pysrc.strategies.migrated_strategies.RSIStrategy
   pysrc.strategies.migrated_strategies.MACDStrategy
   pysrc.strategies.migrated_strategies.BollingerBandsStrategy
   pysrc.strategies.migrated_strategies.MeanReversionStrategy
   pysrc.strategies.migrated_strategies.MovingAverageCrossoverStrategy
   pysrc.strategies.migrated_strategies.EnsemblePipelineStrategy


Functions
---------

.. autoapisummary::

   pysrc.strategies.migrated_strategies.clear_strategy_cache
   pysrc.strategies.migrated_strategies.create_ensemble


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:data:: DISABLE_CACHE
   :type:  Any

.. py:data:: DISABLE_NUMBA
   :type:  Any

.. py:function:: clear_strategy_cache()

.. py:class:: RSIStrategy(rsi_window = ..., upper = ..., lower = ..., neutral_zone = ..., clip = ..., zero_on_any_nan = ..., **kwargs)

   Bases: :py:obj:`PipelineStrategy`


   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


.. py:class:: MACDStrategy(fast = ..., slow = ..., signal = ..., use_histogram = ..., clip = ..., **kwargs)

   Bases: :py:obj:`PipelineStrategy`


   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


.. py:class:: BollingerBandsStrategy(period = ..., num_std = ..., mode = ..., clip = ..., **kwargs)

   Bases: :py:obj:`PipelineStrategy`


   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


.. py:class:: MeanReversionStrategy(period = ..., entry_threshold = ..., exit_threshold = ..., clip = ..., **kwargs)

   Bases: :py:obj:`PipelineStrategy`


   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


.. py:class:: MovingAverageCrossoverStrategy(short = ..., long = ..., ma_type = ..., use_momentum = ..., clip = ..., price_col = ..., **kwargs)

   Bases: :py:obj:`PipelineStrategy`


   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


.. py:class:: EnsemblePipelineStrategy(strategy_specs, weights = ..., combination_method = ..., adaptive_weights = ..., performance_window = ..., **kwargs)

   Bases: :py:obj:`PipelineStrategy`


   .. py:attribute:: ADAPTIVE_UPDATE_INTERVAL
      :type:  Final[int]
      :value: Ellipsis



   .. py:attribute:: MAX_FAILURES
      :type:  Final[int]
      :value: Ellipsis



   .. py:attribute:: MIN_WEIGHT_FLOOR
      :type:  Final[float]
      :value: Ellipsis



   .. py:method:: features_plan()


   .. py:method:: generate_signal(features)


.. py:function:: create_ensemble(ctx_or_configs, strategy_configs = ..., weights = ..., combination_method = ..., adaptive = ...)

