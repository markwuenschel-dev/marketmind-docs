pysrc.pipeline.phase2_ii0c_runner
=================================

.. py:module:: pysrc.pipeline.phase2_ii0c_runner


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.phase2_ii0c_runner.PHASE2_II0C_EVIDENCE_SUBDIR
   pysrc.pipeline.phase2_ii0c_runner.II0C_DRY_RUN_SUMMARY_FILENAME
   pysrc.pipeline.phase2_ii0c_runner.II0C_DRY_RUN_SUMMARY_LEGACY_FILENAME
   pysrc.pipeline.phase2_ii0c_runner.II0C_PILOT_REPORT_FILENAME
   pysrc.pipeline.phase2_ii0c_runner.PHASE2_II0C_SUMMARY_FILENAME
   pysrc.pipeline.phase2_ii0c_runner.II0C_DRY_RUN_REPORT_SCHEMA
   pysrc.pipeline.phase2_ii0c_runner.II0C_PILOT_REPORT_SCHEMA
   pysrc.pipeline.phase2_ii0c_runner.PHASE2_II0C_SUMMARY_SCHEMA
   pysrc.pipeline.phase2_ii0c_runner.PHASE2_II0C_PHASE
   pysrc.pipeline.phase2_ii0c_runner.PHASE2_II0C_GATE_II_STATUS
   pysrc.pipeline.phase2_ii0c_runner.II0C_PILOT_SEMANTIC_OUTCOME_OK
   pysrc.pipeline.phase2_ii0c_runner.II0C_FAIL_CLOSED_CHECKS
   pysrc.pipeline.phase2_ii0c_runner.UNAVAILABLE_II0C_PROOF_SURFACES


Classes
-------

.. autoapisummary::

   pysrc.pipeline.phase2_ii0c_runner.II0CTaskProvider
   pysrc.pipeline.phase2_ii0c_runner.II0CEncoderProvider
   pysrc.pipeline.phase2_ii0c_runner.II0CComparisonProvider
   pysrc.pipeline.phase2_ii0c_runner.II0CGovernedArtifactEmitter
   pysrc.pipeline.phase2_ii0c_runner.Phase2II0CRunRequest
   pysrc.pipeline.phase2_ii0c_runner.Phase2II0CComparisonPack
   pysrc.pipeline.phase2_ii0c_runner.Phase2II0CProviders
   pysrc.pipeline.phase2_ii0c_runner.Phase2II0CRunResult
   pysrc.pipeline.phase2_ii0c_runner.II0CRunResult


Functions
---------

.. autoapisummary::

   pysrc.pipeline.phase2_ii0c_runner.default_ii0c_task_provider
   pysrc.pipeline.phase2_ii0c_runner.default_ii0c_encoder_provider
   pysrc.pipeline.phase2_ii0c_runner.default_ii0c_comparison_provider
   pysrc.pipeline.phase2_ii0c_runner.run_phase2_ii0c_pilot
   pysrc.pipeline.phase2_ii0c_runner.run_phase2_ii0c_dry_run


Module Contents
---------------

.. py:data:: PHASE2_II0C_EVIDENCE_SUBDIR
   :type:  Any

.. py:data:: II0C_DRY_RUN_SUMMARY_FILENAME
   :type:  Any

.. py:data:: II0C_DRY_RUN_SUMMARY_LEGACY_FILENAME
   :type:  Any

.. py:data:: II0C_PILOT_REPORT_FILENAME
   :type:  Any

.. py:data:: PHASE2_II0C_SUMMARY_FILENAME
   :type:  Any

.. py:data:: II0C_DRY_RUN_REPORT_SCHEMA
   :type:  Any

.. py:data:: II0C_PILOT_REPORT_SCHEMA
   :type:  Any

.. py:data:: PHASE2_II0C_SUMMARY_SCHEMA
   :type:  Any

.. py:data:: PHASE2_II0C_PHASE
   :type:  Any

.. py:data:: PHASE2_II0C_GATE_II_STATUS
   :type:  Any

.. py:data:: II0C_PILOT_SEMANTIC_OUTCOME_OK
   :type:  Any

.. py:data:: II0C_FAIL_CLOSED_CHECKS
   :type:  tuple[str, Ellipsis]
   :value: Ellipsis


.. py:data:: UNAVAILABLE_II0C_PROOF_SURFACES
   :type:  tuple[str, Ellipsis]
   :value: Ellipsis


.. py:class:: II0CTaskProvider

   Bases: :py:obj:`Protocol`


.. py:class:: II0CEncoderProvider

   Bases: :py:obj:`Protocol`


.. py:class:: II0CComparisonProvider

   Bases: :py:obj:`Protocol`


.. py:class:: II0CGovernedArtifactEmitter

   Bases: :py:obj:`Protocol`


.. py:class:: Phase2II0CRunRequest

   .. py:attribute:: bundle_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: strategy_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: source_prices
      :type:  Any | None
      :value: Ellipsis



   .. py:attribute:: run_metadata
      :type:  Mapping[str, Any] | None
      :value: Ellipsis



.. py:class:: Phase2II0CComparisonPack

   .. py:attribute:: dataset_manifest
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: baseline_comparison
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: shared_comparison_context
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: cost_model
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: slippage_model
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: borrow_funding
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: latency_fill
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: inner_loop_gain_by_regime
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: harvey_t_statistic
      :type:  float | int
      :value: Ellipsis



   .. py:attribute:: encoder_coherence_score
      :type:  float | int
      :value: Ellipsis



   .. py:attribute:: crisis_episode_ic
      :type:  float | int
      :value: Ellipsis



   .. py:attribute:: forgetting_metric
      :type:  float | int
      :value: Ellipsis



   .. py:attribute:: plasticity_metric
      :type:  float | int
      :value: Ellipsis



   .. py:attribute:: entry_conditions
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: confidence_calibration
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: overall_result
      :type:  str
      :value: Ellipsis



   .. py:attribute:: run_seed_root
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: seed_derivations
      :type:  Sequence[tuple[str, str]]
      :value: Ellipsis



.. py:class:: Phase2II0CProviders

   .. py:attribute:: task_provider
      :type:  Callable[[Phase2II0CRunRequest], II0CMetaTaskPayload] | None
      :value: Ellipsis



   .. py:attribute:: encoder_provider
      :type:  Callable[[Phase2II0CRunRequest, II0CMetaTaskPayload], II0CEncoderTaskOutput] | None
      :value: Ellipsis



   .. py:attribute:: comparison_provider
      :type:  Callable[[Phase2II0CRunRequest, II0CMetaTaskPayload, II0CEncoderTaskOutput], Phase2II0CComparisonPack] | None
      :value: Ellipsis



.. py:class:: Phase2II0CRunResult

   .. py:attribute:: phase
      :type:  str
      :value: Ellipsis



   .. py:attribute:: scaffold
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: non_promotable
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: gate_ii_deferred
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: run_mode
      :type:  str
      :value: Ellipsis



   .. py:attribute:: pilot_semantic_outcome
      :type:  str
      :value: Ellipsis



   .. py:attribute:: governed_evidence_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: governed_artifact_summary
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: pilot_report_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: pilot_report
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: task
      :type:  TaskManifestTaskInput
      :value: Ellipsis



   .. py:attribute:: task_payload
      :type:  II0CMetaTaskPayload
      :value: Ellipsis



   .. py:attribute:: encoder_output
      :type:  II0CEncoderTaskOutput
      :value: Ellipsis



   .. py:attribute:: comparison_pack
      :type:  Phase2II0CComparisonPack
      :value: Ellipsis



.. py:class:: II0CRunResult

   .. py:attribute:: phase
      :type:  str
      :value: Ellipsis



   .. py:attribute:: non_promotable
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: scaffold_only
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: gate_ii_status
      :type:  str
      :value: Ellipsis



   .. py:attribute:: run_mode
      :type:  str
      :value: Ellipsis



   .. py:attribute:: dry_run_semantic_outcome
      :type:  str
      :value: Ellipsis



   .. py:attribute:: summary_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: governed_evidence_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: governed_result
      :type:  II0CGovernedArtifactResult
      :value: Ellipsis



   .. py:attribute:: summary
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:function:: default_ii0c_task_provider(*, seed, timestamp_utc)

.. py:function:: default_ii0c_encoder_provider(*, task_payload, seed)

.. py:function:: default_ii0c_comparison_provider(*, task_payload, seed)

.. py:function:: run_phase2_ii0c_pilot(request, *, providers = ...)

.. py:function:: run_phase2_ii0c_dry_run(*, output_dir, seed, timestamp_utc, task_provider = ..., encoder_provider = ..., comparison_provider = ..., artifact_emitter = ...)

