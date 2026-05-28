pysrc.meta.w2_s1_baseline_only
==============================

.. py:module:: pysrc.meta.w2_s1_baseline_only


Attributes
----------

.. autoapisummary::

   pysrc.meta.w2_s1_baseline_only.LOG
   pysrc.meta.w2_s1_baseline_only.STATUS_PASS
   pysrc.meta.w2_s1_baseline_only.STATUS_FAIL
   pysrc.meta.w2_s1_baseline_only.STATUS_BLOCKED
   pysrc.meta.w2_s1_baseline_only.SIGNAL_FAMILY
   pysrc.meta.w2_s1_baseline_only.ASSET_CLASS
   pysrc.meta.w2_s1_baseline_only.ALERT_MISSING_BASELINE_SCORE
   pysrc.meta.w2_s1_baseline_only.ALERT_MISSING_QUERY_TARGET
   pysrc.meta.w2_s1_baseline_only.ALERT_TRAIN_EVAL_TIME_OVERLAP
   pysrc.meta.w2_s1_baseline_only.ALERT_TRAIN_EVAL_OPPORTUNITY_OVERLAP
   pysrc.meta.w2_s1_baseline_only.ALERT_MANY_TO_ONE_JOIN_EXPANSION
   pysrc.meta.w2_s1_baseline_only.ALERT_ONE_TO_MANY_JOIN_EXPANSION
   pysrc.meta.w2_s1_baseline_only.ALERT_DUPLICATE_OPPORTUNITY_ID
   pysrc.meta.w2_s1_baseline_only.ALERT_FINGERPRINT_MISMATCH
   pysrc.meta.w2_s1_baseline_only.ALERT_INSUFFICIENT_UNIQUE_TICKERS
   pysrc.meta.w2_s1_baseline_only.ALERT_INSUFFICIENT_EVAL_OPPORTUNITIES
   pysrc.meta.w2_s1_baseline_only.ALERT_INSUFFICIENT_REGIME_COVERAGE
   pysrc.meta.w2_s1_baseline_only.ALERT_PURGING_OR_EMBARGO_MISSING
   pysrc.meta.w2_s1_baseline_only.ALERT_MISSING_COST_FIELD
   pysrc.meta.w2_s1_baseline_only.ALERT_FEATURE_TIMESTAMP_AFTER_PIT_BOUNDARY
   pysrc.meta.w2_s1_baseline_only.ALERT_FEATURE_USES_QUERY_LABEL
   pysrc.meta.w2_s1_baseline_only.ALERT_LIGHTGBM_UNAVAILABLE


Classes
-------

.. autoapisummary::

   pysrc.meta.w2_s1_baseline_only.W2S1Config


Functions
---------

.. autoapisummary::

   pysrc.meta.w2_s1_baseline_only.run_w2_s1_baseline_only


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:data:: STATUS_PASS
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: STATUS_FAIL
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: STATUS_BLOCKED
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: SIGNAL_FAMILY
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ASSET_CLASS
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_MISSING_BASELINE_SCORE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_MISSING_QUERY_TARGET
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_TRAIN_EVAL_TIME_OVERLAP
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_TRAIN_EVAL_OPPORTUNITY_OVERLAP
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_MANY_TO_ONE_JOIN_EXPANSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_ONE_TO_MANY_JOIN_EXPANSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_DUPLICATE_OPPORTUNITY_ID
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_FINGERPRINT_MISMATCH
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_INSUFFICIENT_UNIQUE_TICKERS
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_INSUFFICIENT_EVAL_OPPORTUNITIES
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_INSUFFICIENT_REGIME_COVERAGE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_PURGING_OR_EMBARGO_MISSING
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_MISSING_COST_FIELD
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_FEATURE_TIMESTAMP_AFTER_PIT_BOUNDARY
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_FEATURE_USES_QUERY_LABEL
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_LIGHTGBM_UNAVAILABLE
   :type:  Final[str]
   :value: Ellipsis


.. py:class:: W2S1Config

   .. py:attribute:: output_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: design_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: fixture_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: fixture_summary_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: fixture_metadata_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: multi_manifest_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: download_manifest_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: signal_family
      :type:  str
      :value: Ellipsis



   .. py:attribute:: asset_class
      :type:  str
      :value: Ellipsis



   .. py:attribute:: horizon_bars
      :type:  int
      :value: Ellipsis



   .. py:attribute:: support_return_bars
      :type:  int
      :value: Ellipsis



   .. py:attribute:: support_vol_bars
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_folds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: embargo_days
      :type:  int
      :value: Ellipsis



   .. py:attribute:: spread_bps
      :type:  float
      :value: Ellipsis



   .. py:attribute:: slippage_bps
      :type:  float
      :value: Ellipsis



   .. py:attribute:: borrow_rate_ann
      :type:  float
      :value: Ellipsis



   .. py:attribute:: selection_k
      :type:  int
      :value: Ellipsis



   .. py:attribute:: top_k_grid
      :type:  tuple[int, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: timestamp_utc
      :type:  str
      :value: Ellipsis



   .. py:attribute:: max_rebalance_dates
      :type:  int | None
      :value: Ellipsis



   .. py:attribute:: xgb_random_state
      :type:  int
      :value: Ellipsis



   .. py:attribute:: xgb_n_estimators
      :type:  int
      :value: Ellipsis



   .. py:attribute:: xgb_max_depth
      :type:  int
      :value: Ellipsis



   .. py:attribute:: xgb_learning_rate
      :type:  float
      :value: Ellipsis



.. py:function:: run_w2_s1_baseline_only(cfg = ...)

