pysrc.meta.w1_baseline_config
=============================

.. py:module:: pysrc.meta.w1_baseline_config


Attributes
----------

.. autoapisummary::

   pysrc.meta.w1_baseline_config.W1EvidenceSanityMode


Exceptions
----------

.. autoapisummary::

   pysrc.meta.w1_baseline_config.W1BaselineConfigError


Classes
-------

.. autoapisummary::

   pysrc.meta.w1_baseline_config.W1EvidenceSanityConfig
   pysrc.meta.w1_baseline_config.W1BaselineConfig


Module Contents
---------------

.. py:data:: W1EvidenceSanityMode
   :type:  Any

.. py:exception:: W1BaselineConfigError

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:class:: W1EvidenceSanityConfig

   .. py:attribute:: min_std_query_targets
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_std_support_targets
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_std_incumbent_preds_per_fold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_std_challenger_preds_per_fold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_distinct_query_target_values
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_distinct_support_target_values
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_fold_query_target_variance
      :type:  float
      :value: Ellipsis



   .. py:attribute:: require_heterogeneous_task_windows
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: require_fold_metrics_non_degenerate
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: min_abs_gross_ic
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_abs_net_sharpe
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_turnover
      :type:  float
      :value: Ellipsis



   .. py:attribute:: is_fixture_smoke_profile
      :type:  bool
      :value: Ellipsis



   .. py:method:: fixture_smoke()


.. py:class:: W1BaselineConfig

   .. py:attribute:: baseline_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: n_walk_forward_folds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: fold_length_bars
      :type:  int
      :value: Ellipsis



   .. py:attribute:: warmup_bars
      :type:  int
      :value: Ellipsis



   .. py:attribute:: regime_classes
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: min_tasks_per_class
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



   .. py:attribute:: artifact_dir
      :type:  str
      :value: Ellipsis



   .. py:attribute:: report_filename
      :type:  str
      :value: Ellipsis



   .. py:attribute:: example_filename
      :type:  str
      :value: Ellipsis



   .. py:attribute:: random_seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: evidence_sanity
      :type:  W1EvidenceSanityConfig
      :value: Ellipsis



   .. py:attribute:: evidence_sanity_mode
      :type:  W1EvidenceSanityMode
      :value: Ellipsis



   .. py:attribute:: min_unique_eval_tasks_per_fold
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_unique_train_tasks_before_fold
      :type:  int
      :value: Ellipsis



