pysrc.meta.rg09_harness
=======================

.. py:module:: pysrc.meta.rg09_harness


Attributes
----------

.. autoapisummary::

   pysrc.meta.rg09_harness.SUCCESSOR_IDS
   pysrc.meta.rg09_harness.NULL_DISTRIBUTION_INVALID_FAIL_CODE
   pysrc.meta.rg09_harness.FIXTURE_GEOMETRY_CONTRACT_FAIL_CODE
   pysrc.meta.rg09_harness.NULL_RANGE_TOLERANCE
   pysrc.meta.rg09_harness.REGIME_SEPARABILITY_DENOMINATOR_FLOOR


Classes
-------

.. autoapisummary::

   pysrc.meta.rg09_harness.RG09PilotConfig
   pysrc.meta.rg09_harness.RG09HarnessResult
   pysrc.meta.rg09_harness.RG09HarnessRunData


Functions
---------

.. autoapisummary::

   pysrc.meta.rg09_harness.validate_successor_request
   pysrc.meta.rg09_harness.load_rg09_config
   pysrc.meta.rg09_harness.run_rg09_harness_internal
   pysrc.meta.rg09_harness.run_rg09_harness
   pysrc.meta.rg09_harness.build_rg09_candidate_episode_groups


Module Contents
---------------

.. py:data:: SUCCESSOR_IDS
   :type:  Final[tuple[str, str, str]]
   :value: Ellipsis


.. py:data:: NULL_DISTRIBUTION_INVALID_FAIL_CODE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: FIXTURE_GEOMETRY_CONTRACT_FAIL_CODE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: NULL_RANGE_TOLERANCE
   :type:  Final[float]
   :value: Ellipsis


.. py:data:: REGIME_SEPARABILITY_DENOMINATOR_FLOOR
   :type:  Final[float]
   :value: Ellipsis


.. py:class:: RG09PilotConfig

   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: config_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: p_value_threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: null_draw_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: structural_separability_ratio_threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: structural_direction_score_threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: functional_harvey_t_threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: embargo_gap_bars_daily
      :type:  int
      :value: Ellipsis



   .. py:attribute:: embargo_gap_fraction_intraday
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_support_rows
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_query_rows
      :type:  int
      :value: Ellipsis



   .. py:attribute:: label_confidence_threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_admissible_episode_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_regime_transition_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_support_query_mass_per_regime
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_regime_class_count_per_fold
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_temporal_folds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_dwell_time_bars
      :type:  int
      :value: Ellipsis



   .. py:attribute:: label_horizon_bars
      :type:  int
      :value: Ellipsis



   .. py:attribute:: low_confidence_boundary_policy
      :type:  str
      :value: Ellipsis



   .. py:attribute:: functional_model_default
      :type:  str
      :value: Ellipsis



   .. py:attribute:: functional_model_fallback
      :type:  str
      :value: Ellipsis



   .. py:attribute:: null_seed_namespace
      :type:  str
      :value: Ellipsis



   .. py:attribute:: min_episode_regime_class_purity
      :type:  float
      :value: Ellipsis



   .. py:attribute:: episode_construction
      :type:  str
      :value: Ellipsis



   .. py:attribute:: threshold_ids
      :type:  dict[str, str]
      :value: Ellipsis



.. py:class:: RG09HarnessResult

   .. py:attribute:: output_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: decision
      :type:  str | None
      :value: Ellipsis



.. py:class:: RG09HarnessRunData

   .. py:attribute:: output_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: decision
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: config
      :type:  RG09PilotConfig
      :value: Ellipsis



   .. py:attribute:: summary
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: fixture_sha256
      :type:  str
      :value: Ellipsis



   .. py:attribute:: config_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: generation_timestamp
      :type:  str
      :value: Ellipsis



   .. py:attribute:: frame
      :type:  pd.DataFrame
      :value: Ellipsis



   .. py:attribute:: base_episodes
      :type:  pd.DataFrame
      :value: Ellipsis



   .. py:attribute:: exclusion_counts
      :type:  dict[str, int]
      :value: Ellipsis



   .. py:attribute:: gate_result
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: fixture_validation_fail_codes
      :type:  list[str]
      :value: Ellipsis



.. py:function:: validate_successor_request(requested_successor_ids)

.. py:function:: load_rg09_config(config_path)

.. py:function:: run_rg09_harness_internal(*, fixture_path, fixture_summary_path, fixture_metadata_path, config_path, output_dir, boundary_recovery = ...)

.. py:function:: run_rg09_harness(*, fixture_path, fixture_summary_path, fixture_metadata_path, config_path, output_dir, boundary_recovery = ...)

.. py:function:: build_rg09_candidate_episode_groups(frame, config, *, boundary_recovery = ...)

