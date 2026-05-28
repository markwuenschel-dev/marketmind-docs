pysrc.strategies.stat_arb.config
================================

.. py:module:: pysrc.strategies.stat_arb.config


Attributes
----------

.. autoapisummary::

   pysrc.strategies.stat_arb.config.PAIRS_DEFAULT


Classes
-------

.. autoapisummary::

   pysrc.strategies.stat_arb.config.HedgeEstimator
   pysrc.strategies.stat_arb.config.PairsConfig


Module Contents
---------------

.. py:class:: HedgeEstimator

   Bases: :py:obj:`str`, :py:obj:`Enum`


   str(object='') -> str
   str(bytes_or_buffer[, encoding[, errors]]) -> str

   Create a new string object from the given object. If encoding or
   errors is specified, then the object must expose a data buffer
   that will be decoded using the given encoding and error handler.
   Otherwise, returns the result of object.__str__() (if defined)
   or repr(object).
   encoding defaults to sys.getdefaultencoding().
   errors defaults to 'strict'.


   .. py:attribute:: OLS
      :type:  Any


   .. py:attribute:: KALMAN
      :type:  Any


.. py:class:: PairsConfig

   .. py:attribute:: method
      :type:  str
      :value: Ellipsis



   .. py:attribute:: entry_z
      :type:  float
      :value: Ellipsis



   .. py:attribute:: exit_z
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_hold_days
      :type:  int
      :value: Ellipsis



   .. py:attribute:: beta_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: half_life_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: zscore_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_half_life
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_half_life
      :type:  float
      :value: Ellipsis



   .. py:attribute:: hedge_estimator
      :type:  HedgeEstimator
      :value: Ellipsis



.. py:data:: PAIRS_DEFAULT
   :type:  Any

