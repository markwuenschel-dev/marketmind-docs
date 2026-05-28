pysrc.preprocessor.graph.backends.polars
========================================

.. py:module:: pysrc.preprocessor.graph.backends.polars


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.graph.backends.polars.logger
   pysrc.preprocessor.graph.backends.polars.get_lowering
   pysrc.preprocessor.graph.backends.polars.Engine


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.graph.backends.polars.PolarsExecutor


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.graph.backends.polars.get
   pysrc.preprocessor.graph.backends.polars.register
   pysrc.preprocessor.graph.backends.polars.list_ops
   pysrc.preprocessor.graph.backends.polars.scaling_robust_polars
   pysrc.preprocessor.graph.backends.polars.feature_returns_polars
   pysrc.preprocessor.graph.backends.polars.feature_sma_polars
   pysrc.preprocessor.graph.backends.polars.feature_rsi_polars
   pysrc.preprocessor.graph.backends.polars.technical_sma_polars
   pysrc.preprocessor.graph.backends.polars.stats_rolling_std_polars
   pysrc.preprocessor.graph.backends.polars.scaling_zscore_roll_polars
   pysrc.preprocessor.graph.backends.polars.technical_ema_polars
   pysrc.preprocessor.graph.backends.polars.technical_rsi_polars
   pysrc.preprocessor.graph.backends.polars.technical_macd_line_signal_polars
   pysrc.preprocessor.graph.backends.polars.technical_bollinger_polars
   pysrc.preprocessor.graph.backends.polars.technical_atr_polars
   pysrc.preprocessor.graph.backends.polars.technical_obv_polars
   pysrc.preprocessor.graph.backends.polars.technical_vwap_polars
   pysrc.preprocessor.graph.backends.polars.data_load_csv_polars


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:data:: get_lowering
   :type:  Any

.. py:data:: Engine
   :type:  Any

.. py:function:: get(*args)

.. py:function:: register(*args, **kwargs)

.. py:function:: list_ops(*args)

.. py:function:: scaling_robust_polars(ir, lf, *, group_by = ...)

.. py:function:: feature_returns_polars(ir, lf, *, group_by = ...)

.. py:function:: feature_sma_polars(ir, lf, *, group_by = ...)

.. py:function:: feature_rsi_polars(ir, lf, *, group_by = ...)

.. py:function:: technical_sma_polars(ir, lf, *, group_by = ...)

.. py:function:: stats_rolling_std_polars(ir, lf, *, group_by = ...)

.. py:function:: scaling_zscore_roll_polars(ir, lf, *, group_by = ...)

.. py:function:: technical_ema_polars(ir, lf, *, group_by = ...)

.. py:function:: technical_rsi_polars(ir, lf, *, group_by = ...)

.. py:function:: technical_macd_line_signal_polars(ir, lf, *, group_by = ...)

.. py:function:: technical_bollinger_polars(ir, lf, *, group_by = ...)

.. py:function:: technical_atr_polars(ir, lf, *, group_by = ...)

.. py:function:: technical_obv_polars(ir, lf, *, group_by = ...)

.. py:function:: technical_vwap_polars(ir, lf, *, group_by = ...)

.. py:function:: data_load_csv_polars(ir, lf, *, group_by = ...)

.. py:class:: PolarsExecutor(engine_pref = ..., to_torch = ...)

   Bases: :py:obj:`Executor`


   .. py:method:: execute(compiled_plan, df)


