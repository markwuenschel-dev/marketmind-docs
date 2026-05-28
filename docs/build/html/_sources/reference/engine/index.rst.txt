engine
======

.. py:module:: engine


Attributes
----------

.. autoapisummary::

   engine.LOG


Classes
-------

.. autoapisummary::

   engine.BacktestResult
   engine.VectorizedBacktestEngine


Functions
---------

.. autoapisummary::

   engine.run_backtest


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

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


.. py:function:: run_backtest(df, fast_sma = ..., slow_sma = ...)

.. py:class:: VectorizedBacktestEngine

   .. py:method:: run(plan, data, store)


