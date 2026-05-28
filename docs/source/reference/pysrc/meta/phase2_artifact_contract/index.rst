pysrc.meta.phase2_artifact_contract
===================================

.. py:module:: pysrc.meta.phase2_artifact_contract


Attributes
----------

.. autoapisummary::

   pysrc.meta.phase2_artifact_contract.PHASE2_ARTIFACT_CONTRACT_VERSION
   pysrc.meta.phase2_artifact_contract.PHASE2_GOVERNED_PHASE
   pysrc.meta.phase2_artifact_contract.PROMOTABLE_CLAIM_EMITTED
   pysrc.meta.phase2_artifact_contract.GOVERNED_ARTIFACT_CONTRACT
   pysrc.meta.phase2_artifact_contract.CONTENT_HASH_ALGORITHM
   pysrc.meta.phase2_artifact_contract.CONTENT_HASH_CANONICALIZATION
   pysrc.meta.phase2_artifact_contract.GOVERNED_SIGNAL_SURFACE_KIND
   pysrc.meta.phase2_artifact_contract.ENTRY_CONDITION_KEYS
   pysrc.meta.phase2_artifact_contract.SCHEMA_FILES
   pysrc.meta.phase2_artifact_contract.VALID_OVERALL_RESULTS
   pysrc.meta.phase2_artifact_contract.W1_CHALLENGER_SURFACE_SUMMARY_REQUIRED_KEYS_V1


Exceptions
----------

.. autoapisummary::

   pysrc.meta.phase2_artifact_contract.PhaseIIArtifactError


Classes
-------

.. autoapisummary::

   pysrc.meta.phase2_artifact_contract.PhaseIIRunContext


Functions
---------

.. autoapisummary::

   pysrc.meta.phase2_artifact_contract.pit_compliance_from_dataset_manifest
   pysrc.meta.phase2_artifact_contract.canonical_json_bytes
   pysrc.meta.phase2_artifact_contract.canonical_content_hash
   pysrc.meta.phase2_artifact_contract.derive_phase2_task_pool_identity_hash
   pysrc.meta.phase2_artifact_contract.derive_phase2_task_pool_identity_hash_from_manifest_rows
   pysrc.meta.phase2_artifact_contract.canonical_artifact_content_hash
   pysrc.meta.phase2_artifact_contract.validate_artifact_content_hash
   pysrc.meta.phase2_artifact_contract.validate_phase2_artifact_triple
   pysrc.meta.phase2_artifact_contract.emit_phase2_artifacts


Module Contents
---------------

.. py:data:: PHASE2_ARTIFACT_CONTRACT_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: PHASE2_GOVERNED_PHASE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: PROMOTABLE_CLAIM_EMITTED
   :type:  Final[bool]
   :value: Ellipsis


.. py:data:: GOVERNED_ARTIFACT_CONTRACT
   :type:  Final[bool]
   :value: Ellipsis


.. py:data:: CONTENT_HASH_ALGORITHM
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: CONTENT_HASH_CANONICALIZATION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: GOVERNED_SIGNAL_SURFACE_KIND
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ENTRY_CONDITION_KEYS
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:data:: SCHEMA_FILES
   :type:  Final[dict[str, str]]
   :value: Ellipsis


.. py:data:: VALID_OVERALL_RESULTS
   :type:  Final[frozenset[str]]
   :value: Ellipsis


.. py:exception:: PhaseIIArtifactError(message, *, details = ...)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:function:: pit_compliance_from_dataset_manifest(data)

.. py:function:: canonical_json_bytes(payload)

.. py:function:: canonical_content_hash(payload)

.. py:function:: derive_phase2_task_pool_identity_hash(tasks)

.. py:function:: derive_phase2_task_pool_identity_hash_from_manifest_rows(tasks)

.. py:function:: canonical_artifact_content_hash(payload)

.. py:function:: validate_artifact_content_hash(payload, *, label)

.. py:data:: W1_CHALLENGER_SURFACE_SUMMARY_REQUIRED_KEYS_V1
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:function:: validate_phase2_artifact_triple(*, task_doc, meta_doc, exec_doc)

.. py:class:: PhaseIIRunContext

   .. py:attribute:: output_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: timestamp_utc
      :type:  str
      :value: Ellipsis



   .. py:attribute:: tasks
      :type:  Sequence[TaskManifestTaskInput]
      :value: Ellipsis



   .. py:attribute:: dataset_manifest
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



   .. py:attribute:: baseline_comparison
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



   .. py:attribute:: shared_comparison_context
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: task_manifest_result
      :type:  TaskManifestReport | None
      :value: Ellipsis



   .. py:attribute:: execution_assumptions_result
      :type:  ExecutionAssumptionsReport | None
      :value: Ellipsis



   .. py:attribute:: w1_baseline_result
      :type:  W1BaselineResult | None
      :value: Ellipsis



   .. py:attribute:: entry_conditions
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: threshold_references
      :type:  Sequence[Mapping[str, Any]]
      :value: Ellipsis



   .. py:attribute:: run_seed_root
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: seed_derivations
      :type:  Sequence[tuple[str, str]]
      :value: Ellipsis



   .. py:attribute:: confidence_calibration
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: overall_result
      :type:  str
      :value: Ellipsis



   .. py:attribute:: inference_boundary_audit
      :type:  Mapping[str, Any] | None
      :value: Ellipsis



.. py:function:: emit_phase2_artifacts(run_context)

