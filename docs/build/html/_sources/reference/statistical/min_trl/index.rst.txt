statistical.min_trl
===================

.. py:module:: statistical.min_trl


Classes
-------

.. autoapisummary::

   statistical.min_trl.MinTRLResult


Functions
---------

.. autoapisummary::

   statistical.min_trl.compute_min_trl


Module Contents
---------------

.. py:class:: MinTRLResult

   .. py:attribute:: years_needed
      :type:  float
      :value: Ellipsis



   .. py:attribute:: years_available
      :type:  float
      :value: Ellipsis



   .. py:attribute:: observed_sr
      :type:  float
      :value: Ellipsis



   .. py:attribute:: target_confidence
      :type:  float
      :value: Ellipsis



   .. py:attribute:: gate_result
      :type:  str
      :value: Ellipsis



   .. py:method:: from_dict(d)


.. py:function:: compute_min_trl(returns, *, target_confidence = ..., benchmark_sr = ..., periods_per_year = ...)

