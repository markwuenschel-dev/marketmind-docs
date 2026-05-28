pysrc.meta.w1_clean_rerun
=========================

.. py:module:: pysrc.meta.w1_clean_rerun


Attributes
----------

.. autoapisummary::

   pysrc.meta.w1_clean_rerun.ALERT_DUPLICATE_TASK_ID_IN_TASK_UNIVERSE
   pysrc.meta.w1_clean_rerun.ALERT_MISSING_TASK_ID
   pysrc.meta.w1_clean_rerun.ALERT_MISSING_QUERY_TARGET
   pysrc.meta.w1_clean_rerun.ALERT_MISSING_PIT_BOUNDARY
   pysrc.meta.w1_clean_rerun.ALERT_SUPPORT_END_AFTER_QUERY_START
   pysrc.meta.w1_clean_rerun.ALERT_TASK_POOL_SIZE_MISMATCH
   pysrc.meta.w1_clean_rerun.ALERT_TRAIN_EVAL_OVERLAP
   pysrc.meta.w1_clean_rerun.ALERT_DUPLICATE_EVAL_TASK_ID_WITHIN_FOLD
   pysrc.meta.w1_clean_rerun.ALERT_MISSING_TRAIN_TASK_IDS_BY_FOLD
   pysrc.meta.w1_clean_rerun.ALERT_MISSING_EVAL_TASK_IDS_BY_FOLD
   pysrc.meta.w1_clean_rerun.ALERT_INSUFFICIENT_TRAIN_TASKS
   pysrc.meta.w1_clean_rerun.ALERT_INSUFFICIENT_EVAL_TASKS
   pysrc.meta.w1_clean_rerun.ALERT_FOLD_ORDERING_VIOLATION
   pysrc.meta.w1_clean_rerun.ALERT_MISSING_BASELINE_SCORE
   pysrc.meta.w1_clean_rerun.ALERT_DUPLICATE_BASELINE_SCORE_FOR_TASK
   pysrc.meta.w1_clean_rerun.ALERT_BASELINE_SCORED_TRAIN_TASK
   pysrc.meta.w1_clean_rerun.ALERT_BASELINE_MISSING_EVAL_TASK
   pysrc.meta.w1_clean_rerun.ALERT_BASELINE_USED_QUERY_LABELS
   pysrc.meta.w1_clean_rerun.ALERT_BASELINE_SPLIT_MISMATCH
   pysrc.meta.w1_clean_rerun.ALERT_MISSING_BASELINE_PREDICTION_ARTIFACT
   pysrc.meta.w1_clean_rerun.ALERT_MISSING_CHALLENGER_SCORE
   pysrc.meta.w1_clean_rerun.ALERT_DUPLICATE_CHALLENGER_SCORE_FOR_TASK
   pysrc.meta.w1_clean_rerun.ALERT_CHALLENGER_SCORED_TRAIN_TASK
   pysrc.meta.w1_clean_rerun.ALERT_CHALLENGER_MISSING_EVAL_TASK
   pysrc.meta.w1_clean_rerun.ALERT_CHALLENGER_USED_QUERY_LABELS
   pysrc.meta.w1_clean_rerun.ALERT_CHALLENGER_USED_XGBOOST_OUTPUTS_UNDECLARED
   pysrc.meta.w1_clean_rerun.ALERT_CHALLENGER_SPLIT_MISMATCH
   pysrc.meta.w1_clean_rerun.ALERT_REPEATED_QUERY_SCORE_ARRAY_WITHOUT_TASK_SCALAR
   pysrc.meta.w1_clean_rerun.ALERT_MANY_TO_ONE_JOIN_EXPANSION
   pysrc.meta.w1_clean_rerun.ALERT_ONE_TO_MANY_JOIN_EXPANSION
   pysrc.meta.w1_clean_rerun.ALERT_DUPLICATE_TASK_ID_IN_EVAL
   pysrc.meta.w1_clean_rerun.ALERT_BASELINE_CHALLENGER_TASK_SET_MISMATCH
   pysrc.meta.w1_clean_rerun.ALERT_FINGERPRINT_MISMATCH
   pysrc.meta.w1_clean_rerun.ALERT_TASK_LEVEL_TABLE_INVALID
   pysrc.meta.w1_clean_rerun.ALERT_INSUFFICIENT_EVAL_TASKS_FOR_METRICS
   pysrc.meta.w1_clean_rerun.ALERT_ROW_LEVEL_METRICS_USED_AS_TASK_LEVEL
   pysrc.meta.w1_clean_rerun.ALERT_MISSING_REQUIRED_METRIC_INPUT
   pysrc.meta.w1_clean_rerun.ALERT_TASK_COUNT_CLAIM_MISMATCH
   pysrc.meta.w1_clean_rerun.NO_DECISION_INVALID_EVAL_SURFACE
   pysrc.meta.w1_clean_rerun.SUPERSEDED_INVALID_EVAL_ALIGNMENT
   pysrc.meta.w1_clean_rerun.W1_CLEAN_REPORT_SCHEMA_VERSION


Exceptions
----------

.. autoapisummary::

   pysrc.meta.w1_clean_rerun.W1CleanRerunError


Functions
---------

.. autoapisummary::

   pysrc.meta.w1_clean_rerun.build_w1_clean_task_universe
   pysrc.meta.w1_clean_rerun.build_w1_clean_walk_forward_splits
   pysrc.meta.w1_clean_rerun.build_w1_clean_baseline_predictions
   pysrc.meta.w1_clean_rerun.build_w1_clean_challenger_predictions
   pysrc.meta.w1_clean_rerun.build_w1_clean_comparison_table
   pysrc.meta.w1_clean_rerun.audit_w1_task_level_comparison_rows
   pysrc.meta.w1_clean_rerun.build_w1_clean_metrics
   pysrc.meta.w1_clean_rerun.build_w1_clean_gate_report
   pysrc.meta.w1_clean_rerun.run_w1_clean_rerun
   pysrc.meta.w1_clean_rerun.run_default_w1_clean_rerun
   pysrc.meta.w1_clean_rerun.main


Module Contents
---------------

.. py:data:: ALERT_DUPLICATE_TASK_ID_IN_TASK_UNIVERSE
   :type:  Any

.. py:data:: ALERT_MISSING_TASK_ID
   :type:  Any

.. py:data:: ALERT_MISSING_QUERY_TARGET
   :type:  Any

.. py:data:: ALERT_MISSING_PIT_BOUNDARY
   :type:  Any

.. py:data:: ALERT_SUPPORT_END_AFTER_QUERY_START
   :type:  Any

.. py:data:: ALERT_TASK_POOL_SIZE_MISMATCH
   :type:  Any

.. py:data:: ALERT_TRAIN_EVAL_OVERLAP
   :type:  Any

.. py:data:: ALERT_DUPLICATE_EVAL_TASK_ID_WITHIN_FOLD
   :type:  Any

.. py:data:: ALERT_MISSING_TRAIN_TASK_IDS_BY_FOLD
   :type:  Any

.. py:data:: ALERT_MISSING_EVAL_TASK_IDS_BY_FOLD
   :type:  Any

.. py:data:: ALERT_INSUFFICIENT_TRAIN_TASKS
   :type:  Any

.. py:data:: ALERT_INSUFFICIENT_EVAL_TASKS
   :type:  Any

.. py:data:: ALERT_FOLD_ORDERING_VIOLATION
   :type:  Any

.. py:data:: ALERT_MISSING_BASELINE_SCORE
   :type:  Any

.. py:data:: ALERT_DUPLICATE_BASELINE_SCORE_FOR_TASK
   :type:  Any

.. py:data:: ALERT_BASELINE_SCORED_TRAIN_TASK
   :type:  Any

.. py:data:: ALERT_BASELINE_MISSING_EVAL_TASK
   :type:  Any

.. py:data:: ALERT_BASELINE_USED_QUERY_LABELS
   :type:  Any

.. py:data:: ALERT_BASELINE_SPLIT_MISMATCH
   :type:  Any

.. py:data:: ALERT_MISSING_BASELINE_PREDICTION_ARTIFACT
   :type:  Any

.. py:data:: ALERT_MISSING_CHALLENGER_SCORE
   :type:  Any

.. py:data:: ALERT_DUPLICATE_CHALLENGER_SCORE_FOR_TASK
   :type:  Any

.. py:data:: ALERT_CHALLENGER_SCORED_TRAIN_TASK
   :type:  Any

.. py:data:: ALERT_CHALLENGER_MISSING_EVAL_TASK
   :type:  Any

.. py:data:: ALERT_CHALLENGER_USED_QUERY_LABELS
   :type:  Any

.. py:data:: ALERT_CHALLENGER_USED_XGBOOST_OUTPUTS_UNDECLARED
   :type:  Any

.. py:data:: ALERT_CHALLENGER_SPLIT_MISMATCH
   :type:  Any

.. py:data:: ALERT_REPEATED_QUERY_SCORE_ARRAY_WITHOUT_TASK_SCALAR
   :type:  Any

.. py:data:: ALERT_MANY_TO_ONE_JOIN_EXPANSION
   :type:  Any

.. py:data:: ALERT_ONE_TO_MANY_JOIN_EXPANSION
   :type:  Any

.. py:data:: ALERT_DUPLICATE_TASK_ID_IN_EVAL
   :type:  Any

.. py:data:: ALERT_BASELINE_CHALLENGER_TASK_SET_MISMATCH
   :type:  Any

.. py:data:: ALERT_FINGERPRINT_MISMATCH
   :type:  Any

.. py:data:: ALERT_TASK_LEVEL_TABLE_INVALID
   :type:  Any

.. py:data:: ALERT_INSUFFICIENT_EVAL_TASKS_FOR_METRICS
   :type:  Any

.. py:data:: ALERT_ROW_LEVEL_METRICS_USED_AS_TASK_LEVEL
   :type:  Any

.. py:data:: ALERT_MISSING_REQUIRED_METRIC_INPUT
   :type:  Any

.. py:data:: ALERT_TASK_COUNT_CLAIM_MISMATCH
   :type:  Any

.. py:data:: NO_DECISION_INVALID_EVAL_SURFACE
   :type:  Any

.. py:data:: SUPERSEDED_INVALID_EVAL_ALIGNMENT
   :type:  Any

.. py:data:: W1_CLEAN_REPORT_SCHEMA_VERSION
   :type:  Any

.. py:exception:: W1CleanRerunError

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:function:: build_w1_clean_task_universe(*, tasks, task_query_targets, task_support_targets, data_fingerprint, cost_assumptions_fingerprint, splits_fingerprint, task_pool_hash, cost_per_bar, expected_task_pool_size = ...)

.. py:function:: build_w1_clean_walk_forward_splits(*, tasks, config)

.. py:function:: build_w1_clean_baseline_predictions(*, tasks, splits_doc, config, incumbent, task_query_targets, data_fingerprint, splits_fingerprint, cost_assumptions_fingerprint, task_pool_hash, prediction_time_utc)

.. py:function:: build_w1_clean_challenger_predictions(*, surface, splits_doc, challenger_model_id)

.. py:function:: build_w1_clean_comparison_table(*, task_universe_rows, splits_doc, baseline_doc, challenger_doc, expected_data_fingerprint, expected_splits_fingerprint, expected_cost_assumptions_fingerprint, expected_task_pool_hash)

.. py:function:: audit_w1_task_level_comparison_rows(*, rows, expected_eval_keys)

.. py:function:: build_w1_clean_metrics(*, comparison_rows, expected_eval_rows)

.. py:function:: build_w1_clean_gate_report(*, agent_1_audit, agent_2_audit, agent_3_audit, agent_4_audit, agent_5_audit, agent_6_audit, metrics_doc, declared_unique_eval_tasks, declared_task_universe_size, run_id, data_fingerprint, splits_fingerprint, cost_assumptions_fingerprint, task_pool_hash)

.. py:function:: run_w1_clean_rerun(*, output_dir = ..., pool_cfg = ..., seed = ..., timestamp_utc = ..., config = ..., challenger_model_id = ..., declared_task_universe_size = ...)

.. py:function:: run_default_w1_clean_rerun(*, output_root = ..., output_dir = ..., seed = ..., timestamp_utc = ...)

.. py:function:: main()

