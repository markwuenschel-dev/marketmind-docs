pysrc.meta.allocator_benchmark.baselines
========================================

.. py:module:: pysrc.meta.allocator_benchmark.baselines


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.baselines.SignalInputRow
   pysrc.meta.allocator_benchmark.baselines.WeightedSignalRow
   pysrc.meta.allocator_benchmark.baselines.W2_SIGNAL_WEIGHTED_ROW_FIELDS


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.baselines.build_weighted_signal_rows
   pysrc.meta.allocator_benchmark.baselines.static_equal_weight_signal_allocator
   pysrc.meta.allocator_benchmark.baselines.rolling_ic_weighted_signal_allocator
   pysrc.meta.allocator_benchmark.baselines.best_historical_signal_allocator
   pysrc.meta.allocator_benchmark.baselines.regime_conditioned_signal_gate_allocator


Module Contents
---------------

.. py:data:: SignalInputRow
   :type:  Any

.. py:data:: WeightedSignalRow
   :type:  Any

.. py:data:: W2_SIGNAL_WEIGHTED_ROW_FIELDS
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:function:: build_weighted_signal_rows(rows, system_id, threshold = ...)

.. py:function:: static_equal_weight_signal_allocator(rows)

.. py:function:: rolling_ic_weighted_signal_allocator(rows)

.. py:function:: best_historical_signal_allocator(rows)

.. py:function:: regime_conditioned_signal_gate_allocator(rows, threshold = ...)

