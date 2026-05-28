pysrc.domain.portfolio.service
==============================

.. py:module:: pysrc.domain.portfolio.service


Classes
-------

.. autoapisummary::

   pysrc.domain.portfolio.service.Position
   pysrc.domain.portfolio.service.PortfolioSnapshot
   pysrc.domain.portfolio.service.ConstraintValidator
   pysrc.domain.portfolio.service.PortfolioService


Module Contents
---------------

.. py:class:: Position

   .. py:attribute:: symbol
      :type:  str
      :value: Ellipsis



   .. py:attribute:: quantity
      :type:  Decimal
      :value: Ellipsis



   .. py:attribute:: entry_price
      :type:  Decimal
      :value: Ellipsis



.. py:class:: PortfolioSnapshot

   .. py:attribute:: timestamp
      :type:  pd.Timestamp
      :value: Ellipsis



   .. py:attribute:: positions
      :type:  Mapping[str, Position]
      :value: Ellipsis



   .. py:attribute:: cash
      :type:  Decimal
      :value: Ellipsis



   .. py:attribute:: base_currency
      :type:  str
      :value: Ellipsis



.. py:class:: ConstraintValidator

   Bases: :py:obj:`Protocol`


   .. py:method:: validate(snapshot, proposed)


.. py:class:: PortfolioService

   Bases: :py:obj:`ABC`


   .. py:method:: construct(signals, capital, *, as_of = ...)


   .. py:method:: rebalance(current, target_weights, *, constraints = ...)


