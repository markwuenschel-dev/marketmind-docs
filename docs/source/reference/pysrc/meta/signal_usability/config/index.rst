pysrc.meta.signal_usability.config
==================================

.. py:module:: pysrc.meta.signal_usability.config


Classes
-------

.. autoapisummary::

   pysrc.meta.signal_usability.config.SignalUsabilityConfig


Module Contents
---------------

.. py:class:: SignalUsabilityConfig

   .. py:attribute:: horizon
      :type:  int
      :value: Ellipsis



   .. py:attribute:: utility_floor
      :type:  float
      :value: Ellipsis



   .. py:attribute:: cost_per_turnover_unit
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_recent_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: recent_ic_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: recent_hit_rate_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: decay_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: output_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: timestamp_utc
      :type:  str
      :value: Ellipsis



   .. py:attribute:: minimum_eligible_rows
      :type:  int
      :value: Ellipsis



   .. py:attribute:: minimum_admissible_dates
      :type:  int
      :value: Ellipsis



   .. py:attribute:: minimum_real_instruments
      :type:  int
      :value: Ellipsis



   .. py:attribute:: data_mode
      :type:  Literal['real', 'fixture', 'synthetic']
      :value: Ellipsis



   .. py:attribute:: data_source_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: as_of_policy
      :type:  str
      :value: Ellipsis



   .. py:attribute:: requested_universe
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: train_fraction
      :type:  float
      :value: Ellipsis



   .. py:attribute:: validation_fraction
      :type:  float
      :value: Ellipsis



   .. py:attribute:: test_fraction
      :type:  float
      :value: Ellipsis



   .. py:attribute:: regime_gate_min_mean_utility
      :type:  float
      :value: Ellipsis



   .. py:attribute:: regime_gate_unseen_policy
      :type:  Literal['abstain']
      :value: Ellipsis



   .. py:attribute:: min_coverage_for_support
      :type:  float
      :value: Ellipsis



   .. py:attribute:: xgboost_probability_threshold
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: xgboost_n_estimators
      :type:  int
      :value: Ellipsis



   .. py:attribute:: xgboost_max_depth
      :type:  int
      :value: Ellipsis



   .. py:attribute:: xgboost_learning_rate
      :type:  float
      :value: Ellipsis



