pysrc.meta.indicators.config
============================

.. py:module:: pysrc.meta.indicators.config


Classes
-------

.. autoapisummary::

   pysrc.meta.indicators.config.IndicatorLibraryConfig
   pysrc.meta.indicators.config.W3BPandasTAConfig
   pysrc.meta.indicators.config.PenaltyMultiplierSpec
   pysrc.meta.indicators.config.W3CLiquidityChildConfig


Module Contents
---------------

.. py:class:: IndicatorLibraryConfig

   .. py:attribute:: lag_bars
      :type:  int
      :value: Ellipsis



   .. py:attribute:: redundancy_rank_corr_threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: panel_float32
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: save_long_indicator_rows
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: save_selected_rows_only
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: robust_indicator_scaling
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: robust_scale_iqr_multiplier
      :type:  float
      :value: Ellipsis



   .. py:attribute:: robust_scale_min_iqr
      :type:  float
      :value: Ellipsis



.. py:class:: W3BPandasTAConfig

   .. py:attribute:: output_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: surfaces
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: xgboost_train_row_cap
      :type:  int
      :value: Ellipsis



   .. py:attribute:: xgboost_predict_batch_rows
      :type:  int
      :value: Ellipsis



   .. py:attribute:: use_xgboost
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: loader_backend
      :type:  Literal['polars', 'pandas']
      :value: Ellipsis



   .. py:attribute:: workers
      :type:  int
      :value: Ellipsis



   .. py:attribute:: xgboost_n_jobs
      :type:  int
      :value: Ellipsis



   .. py:attribute:: seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: timestamp_utc
      :type:  str
      :value: Ellipsis



   .. py:attribute:: indicator_library
      :type:  IndicatorLibraryConfig
      :value: Ellipsis



.. py:class:: PenaltyMultiplierSpec

   .. py:attribute:: formula
      :type:  str
      :value: Ellipsis



   .. py:attribute:: reference_liquidity
      :type:  float
      :value: Ellipsis



   .. py:attribute:: penalty_term_cap
      :type:  float
      :value: Ellipsis



   .. py:attribute:: strength
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_multiplier
      :type:  float
      :value: Ellipsis



   .. py:attribute:: calibration
      :type:  dict[str, float]
      :value: Ellipsis



   .. py:method:: from_mapping(payload)


.. py:class:: W3CLiquidityChildConfig

   .. py:attribute:: output_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: surfaces
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: surface_d_audit_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: w3_b_report_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: penalty_multiplier_spec
      :type:  PenaltyMultiplierSpec | None
      :value: Ellipsis



   .. py:attribute:: xgboost_train_row_cap
      :type:  int
      :value: Ellipsis



   .. py:attribute:: xgboost_predict_batch_rows
      :type:  int
      :value: Ellipsis



   .. py:attribute:: use_xgboost
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: workers
      :type:  int
      :value: Ellipsis



   .. py:attribute:: xgboost_n_jobs
      :type:  int
      :value: Ellipsis



   .. py:attribute:: seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: timestamp_utc
      :type:  str
      :value: Ellipsis



   .. py:attribute:: indicator_library
      :type:  IndicatorLibraryConfig
      :value: Ellipsis



   .. py:method:: with_penalty_spec(spec)


   .. py:method:: require_penalty_spec()


