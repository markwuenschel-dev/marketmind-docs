pysrc.backtesting.api
=====================

.. py:module:: pysrc.backtesting.api


Classes
-------

.. autoapisummary::

   pysrc.backtesting.api.BacktestSpec
   pysrc.backtesting.api.BacktestResult
   pysrc.backtesting.api.BacktestAPI


Module Contents
---------------

.. py:class:: BacktestSpec

   .. py:attribute:: strategy_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: start_date
      :type:  str
      :value: Ellipsis



   .. py:attribute:: end_date
      :type:  str
      :value: Ellipsis



   .. py:attribute:: initial_capital
      :type:  Decimal
      :value: Ellipsis



   .. py:attribute:: config_overrides
      :type:  Mapping[str, Any] | None
      :value: Ellipsis



.. py:class:: BacktestResult

   .. py:attribute:: spec
      :type:  BacktestSpec
      :value: Ellipsis



   .. py:attribute:: equity_curve
      :type:  pd.Series
      :value: Ellipsis



   .. py:attribute:: trades
      :type:  pd.DataFrame
      :value: Ellipsis



   .. py:attribute:: metrics
      :type:  Mapping[str, float]
      :value: Ellipsis



   .. py:attribute:: artifact_path
      :type:  Path
      :value: Ellipsis



.. py:class:: BacktestAPI

   Bases: :py:obj:`ABC`


   .. py:method:: run(spec)


   .. py:method:: load(run_id)


   .. py:method:: compare(results, *, benchmark = ...)


