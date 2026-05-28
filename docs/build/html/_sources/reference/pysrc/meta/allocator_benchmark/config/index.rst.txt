pysrc.meta.allocator_benchmark.config
=====================================

.. py:module:: pysrc.meta.allocator_benchmark.config


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.config.W2CostDataMode
   pysrc.meta.allocator_benchmark.config.W2AllocationWeighting


Classes
-------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.config.W2AllocatorBenchmarkConfig


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.config.compute_w2_top_k_default


Module Contents
---------------

.. py:data:: W2CostDataMode
   :type:  Any

.. py:data:: W2AllocationWeighting
   :type:  Any

.. py:function:: compute_w2_top_k_default(observed_instrument_count)

.. py:class:: W2AllocatorBenchmarkConfig

   .. py:attribute:: horizon
      :type:  int
      :value: Ellipsis



   .. py:attribute:: cost_per_turnover_unit
      :type:  float
      :value: Ellipsis



   .. py:attribute:: minimum_instruments
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_coverage
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_single_instrument_utility_share
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_single_quarter_utility_share
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_single_regime_utility_share
      :type:  float
      :value: Ellipsis



   .. py:attribute:: shorts_allowed
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: max_gross_exposure
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_single_instrument_weight
      :type:  float
      :value: Ellipsis



   .. py:attribute:: abstention_allowed
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: score_threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: score_higher_is_better
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: allocation_weighting
      :type:  W2AllocationWeighting
      :value: Ellipsis



   .. py:attribute:: top_k_policy
      :type:  str
      :value: Ellipsis



   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: output_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: timestamp_utc
      :type:  str
      :value: Ellipsis



   .. py:method:: to_report_config()


