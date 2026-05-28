pysrc.meta.w1_baseline_types
============================

.. py:module:: pysrc.meta.w1_baseline_types


Attributes
----------

.. autoapisummary::

   pysrc.meta.w1_baseline_types.W1EvidenceLane


Classes
-------

.. autoapisummary::

   pysrc.meta.w1_baseline_types.W1FoldResult
   pysrc.meta.w1_baseline_types.W1AggregateMetrics
   pysrc.meta.w1_baseline_types.W1CostAssumptions
   pysrc.meta.w1_baseline_types.W1ThresholdReference
   pysrc.meta.w1_baseline_types.W1EvidenceSource
   pysrc.meta.w1_baseline_types.W1ComparisonFingerprints
   pysrc.meta.w1_baseline_types.W1BaselineResult


Module Contents
---------------

.. py:data:: W1EvidenceLane
   :type:  Any

.. py:class:: W1FoldResult

   .. py:attribute:: fold_index
      :type:  int
      :value: Ellipsis



   .. py:attribute:: fold_start
      :type:  str
      :value: Ellipsis



   .. py:attribute:: fold_end
      :type:  str
      :value: Ellipsis



   .. py:attribute:: net_sharpe
      :type:  float
      :value: Ellipsis



   .. py:attribute:: gross_ic
      :type:  float
      :value: Ellipsis



   .. py:attribute:: crisis_ic
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: max_drawdown
      :type:  float
      :value: Ellipsis



   .. py:attribute:: turnover
      :type:  float
      :value: Ellipsis



   .. py:attribute:: n_query_rows_scored
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_unique_tasks_scored
      :type:  int
      :value: Ellipsis



   .. py:attribute:: regime_breakdown
      :type:  dict[str, float | None]
      :value: Ellipsis



.. py:class:: W1AggregateMetrics

   .. py:attribute:: mean_net_sharpe
      :type:  float
      :value: Ellipsis



   .. py:attribute:: mean_net_sharpe_normal_null_p
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: mean_gross_ic
      :type:  float
      :value: Ellipsis



   .. py:attribute:: mean_crisis_ic
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: mean_max_drawdown
      :type:  float
      :value: Ellipsis



   .. py:attribute:: mean_turnover
      :type:  float
      :value: Ellipsis



   .. py:attribute:: n_folds_with_crisis
      :type:  int
      :value: Ellipsis



.. py:class:: W1CostAssumptions

   .. py:attribute:: spread_bps
      :type:  float
      :value: Ellipsis



   .. py:attribute:: slippage_bps
      :type:  float
      :value: Ellipsis



   .. py:attribute:: borrow_rate_ann
      :type:  float
      :value: Ellipsis



.. py:class:: W1ThresholdReference

   .. py:attribute:: id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: state
      :type:  str
      :value: Ellipsis



   .. py:attribute:: current_expression
      :type:  str
      :value: Ellipsis



.. py:class:: W1EvidenceSource

   .. py:attribute:: market_data_source
      :type:  str
      :value: Ellipsis



   .. py:attribute:: label_source
      :type:  str
      :value: Ellipsis



   .. py:attribute:: target_source
      :type:  str
      :value: Ellipsis



   .. py:attribute:: challenger_source
      :type:  str
      :value: Ellipsis



   .. py:attribute:: real_market_data_evidence
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: w1_gate_closure_eligible
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: pit_heterogeneity_governance_acknowledged
      :type:  bool
      :value: Ellipsis



   .. py:method:: as_dict()


.. py:class:: W1ComparisonFingerprints

   .. py:attribute:: data_fingerprint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: splits_fingerprint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: cost_assumptions_fingerprint
      :type:  str
      :value: Ellipsis



.. py:class:: W1BaselineResult

   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: baseline_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: run_timestamp_utc
      :type:  str
      :value: Ellipsis



   .. py:attribute:: n_folds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: fold_results
      :type:  tuple[W1FoldResult, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: aggregate
      :type:  W1AggregateMetrics
      :value: Ellipsis



   .. py:attribute:: cost_assumptions
      :type:  W1CostAssumptions
      :value: Ellipsis



   .. py:attribute:: threshold_references
      :type:  tuple[W1ThresholdReference, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: gate_ii_posture
      :type:  str
      :value: Ellipsis



   .. py:attribute:: promotion_note
      :type:  str
      :value: Ellipsis



   .. py:attribute:: content_hash
      :type:  dict[str, str]
      :value: Ellipsis



   .. py:attribute:: evidence_lane
      :type:  W1EvidenceLane
      :value: Ellipsis



   .. py:attribute:: row_level_fold_results
      :type:  tuple[W1FoldResult, Ellipsis] | None
      :value: Ellipsis



   .. py:attribute:: row_level_aggregate
      :type:  W1AggregateMetrics | None
      :value: Ellipsis



   .. py:attribute:: challenger_aggregate
      :type:  W1AggregateMetrics | None
      :value: Ellipsis



   .. py:attribute:: challenger_fold_results
      :type:  tuple[W1FoldResult, Ellipsis] | None
      :value: Ellipsis



   .. py:attribute:: challenger_row_level_aggregate
      :type:  W1AggregateMetrics | None
      :value: Ellipsis



   .. py:attribute:: challenger_row_level_fold_results
      :type:  tuple[W1FoldResult, Ellipsis] | None
      :value: Ellipsis



   .. py:attribute:: incumbent_model_config
      :type:  dict[str, Any] | None
      :value: Ellipsis



   .. py:attribute:: evidence_source
      :type:  W1EvidenceSource | None
      :value: Ellipsis



   .. py:attribute:: target_provenance
      :type:  dict[str, Any] | None
      :value: Ellipsis



   .. py:attribute:: comparison_fingerprints
      :type:  W1ComparisonFingerprints | None
      :value: Ellipsis



   .. py:attribute:: pit_boundary_policy
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: heterogeneous_task_pits_supported
      :type:  bool | None
      :value: Ellipsis



   .. py:attribute:: challenger_surface_summary
      :type:  dict[str, Any] | None
      :value: Ellipsis



   .. py:attribute:: challenger_surface_content_hash
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: evidence_sanity_report
      :type:  dict[str, Any] | None
      :value: Ellipsis



