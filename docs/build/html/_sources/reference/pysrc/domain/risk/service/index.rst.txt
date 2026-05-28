pysrc.domain.risk.service
=========================

.. py:module:: pysrc.domain.risk.service


Classes
-------

.. autoapisummary::

   pysrc.domain.risk.service.RiskMetrics
   pysrc.domain.risk.service.RiskLimit
   pysrc.domain.risk.service.RiskService


Module Contents
---------------

.. py:class:: RiskMetrics

   .. py:attribute:: var_95
      :type:  Decimal
      :value: Ellipsis



   .. py:attribute:: cvar_95
      :type:  Decimal
      :value: Ellipsis



   .. py:attribute:: max_drawdown
      :type:  Decimal
      :value: Ellipsis



   .. py:attribute:: beta
      :type:  Decimal
      :value: Ellipsis



   .. py:attribute:: volatility
      :type:  Decimal
      :value: Ellipsis



.. py:class:: RiskLimit

   .. py:attribute:: metric
      :type:  str
      :value: Ellipsis



   .. py:attribute:: threshold
      :type:  Decimal
      :value: Ellipsis



   .. py:attribute:: hard
      :type:  bool
      :value: Ellipsis



.. py:class:: RiskService

   Bases: :py:obj:`ABC`


   .. py:method:: calculate(portfolio, *, lookback = ...)


   .. py:method:: validate_limits(portfolio, limits, *, as_of = ...)


   .. py:method:: exposure(portfolio, *, by_sector = ..., by_factor = ...)


