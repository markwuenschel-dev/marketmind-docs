pysrc.backtesting.engine
========================

.. py:module:: pysrc.backtesting.engine


Classes
-------

.. autoapisummary::

   pysrc.backtesting.engine.BacktestResult


Functions
---------

.. autoapisummary::

   pysrc.backtesting.engine.add_signals
   pysrc.backtesting.engine.add_strategy_returns
   pysrc.backtesting.engine.compute_metrics
   pysrc.backtesting.engine.run_backtest


Module Contents
---------------

.. py:class:: BacktestResult

   .. py:attribute:: total_return
      :type:  float
      :value: Ellipsis



   .. py:attribute:: sharpe_ratio
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_drawdown
      :type:  float
      :value: Ellipsis



   .. py:attribute:: win_rate
      :type:  float
      :value: Ellipsis



   .. py:attribute:: num_trades
      :type:  int
      :value: Ellipsis



   .. py:method:: to_dict()


.. py:function:: add_signals(df, fast_col, slow_col)

.. py:function:: add_strategy_returns(df)

.. py:function:: compute_metrics(df)

.. py:function:: run_backtest(df, fast_sma = ..., slow_sma = ...)

