pysrc.meta.allocator_benchmark.classification
=============================================

.. py:module:: pysrc.meta.allocator_benchmark.classification


Classes
-------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.classification.W2ClassificationInputs


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.classification.apply_w2_v2_classification_policy
   pysrc.meta.allocator_benchmark.classification.classify_w2_result


Module Contents
---------------

.. py:class:: W2ClassificationInputs

   .. py:attribute:: structural_failure_reasons
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: observed_instrument_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: minimum_instruments
      :type:  int
      :value: Ellipsis



   .. py:attribute:: cost_data_mode
      :type:  W2CostDataMode
      :value: Ellipsis



   .. py:attribute:: challenger_net_utility
      :type:  float
      :value: Ellipsis



   .. py:attribute:: static_net_utility
      :type:  float
      :value: Ellipsis



   .. py:attribute:: rolling_ic_net_utility
      :type:  float
      :value: Ellipsis



   .. py:attribute:: best_historical_net_utility
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: regime_gate_net_utility
      :type:  float
      :value: Ellipsis



   .. py:attribute:: challenger_coverage
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_coverage
      :type:  float
      :value: Ellipsis



   .. py:attribute:: challenger_turnover_adjusted_utility
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



   .. py:attribute:: max_single_instrument_utility_share_limit
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_single_quarter_utility_share_limit
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_single_regime_utility_share_limit
      :type:  float
      :value: Ellipsis



   .. py:attribute:: mixed_metric_deterioration
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: use_w2_v2_participation_gates
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: test_date_participation_rate
      :type:  float
      :value: Ellipsis



   .. py:attribute:: test_avg_selected_instruments_per_date
      :type:  float
      :value: Ellipsis



   .. py:attribute:: test_cross_section_selection_rate
      :type:  float
      :value: Ellipsis



.. py:function:: apply_w2_v2_classification_policy(outcome, *, cost_data_mode)

.. py:function:: classify_w2_result(inputs)

