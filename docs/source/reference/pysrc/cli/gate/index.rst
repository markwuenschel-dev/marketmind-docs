pysrc.cli.gate
==============

.. py:module:: pysrc.cli.gate


Attributes
----------

.. autoapisummary::

   pysrc.cli.gate.GATE_SCHEMA_VERSION
   pysrc.cli.gate.GATE_CLI_VERSION
   pysrc.cli.gate.INVALID_INPUT_REASON_CODES
   pysrc.cli.gate.REQUIRED_BUNDLE_FILES
   pysrc.cli.gate.OPTIONAL_BUNDLE_FILES
   pysrc.cli.gate.PLAN_REQUIRED_FIELDS
   pysrc.cli.gate.ENV_REQUIRED_FIELDS
   pysrc.cli.gate.DATASET_REQUIRED_FIELDS
   pysrc.cli.gate.PREPROCESSING_REQUIRED_FIELDS
   pysrc.cli.gate.SPLITS_REQUIRED_FIELDS
   pysrc.cli.gate.DATA_LINEAGE_GATE
   pysrc.cli.gate.STAT_VALIDITY_REQUIRED_KEYS
   pysrc.cli.gate.STAT_VALIDITY_GATE_VALUES
   pysrc.cli.gate.STAT_VALIDITY_STRUCTURED_SECTIONS
   pysrc.cli.gate.EXECUTION_ASSUMPTIONS_REQUIRED_KEYS
   pysrc.cli.gate.EXECUTION_ASSUMPTIONS_COST_KEYS


Classes
-------

.. autoapisummary::

   pysrc.cli.gate.ExitCode
   pysrc.cli.gate.GateResult
   pysrc.cli.gate.ReasonCode
   pysrc.cli.gate.GateCheck
   pysrc.cli.gate.GateReport
   pysrc.cli.gate.DataLineageGate


Functions
---------

.. autoapisummary::

   pysrc.cli.gate.resolve_gate_output_path
   pysrc.cli.gate.write_gate_report
   pysrc.cli.gate.emit_gate_failure_report
   pysrc.cli.gate.validate_bundle_exists
   pysrc.cli.gate.validate_required_files
   pysrc.cli.gate.validate_plan_identity
   pysrc.cli.gate.validate_env_fingerprint
   pysrc.cli.gate.validate_dataset_manifest
   pysrc.cli.gate.validate_preprocessing_report
   pysrc.cli.gate.validate_splits_manifest
   pysrc.cli.gate.validate_leakage_invariants
   pysrc.cli.gate.validate_splits_integrity
   pysrc.cli.gate.validate_stat_validity_report
   pysrc.cli.gate.validate_execution_assumptions
   pysrc.cli.gate.validate_bundle
   pysrc.cli.gate.main


Module Contents
---------------

.. py:data:: GATE_SCHEMA_VERSION
   :type:  Any

.. py:data:: GATE_CLI_VERSION
   :type:  Any

.. py:class:: ExitCode

   Bases: :py:obj:`Enum`


   .. py:attribute:: PASS
      :type:  Any


   .. py:attribute:: FAIL
      :type:  Any


   .. py:attribute:: INVALID_INPUT
      :type:  Any


   .. py:attribute:: INTERNAL_ERROR
      :type:  Any


.. py:class:: GateResult

   Bases: :py:obj:`Enum`


   .. py:attribute:: PASS
      :type:  Any


   .. py:attribute:: FAIL
      :type:  Any


.. py:class:: ReasonCode

   Bases: :py:obj:`Enum`


   .. py:attribute:: VALID
      :type:  Any


   .. py:attribute:: UNKNOWN_SCHEMA_VERSION
      :type:  Any


   .. py:attribute:: MISSING_SCHEMA_VERSION
      :type:  Any


   .. py:attribute:: INVALID_SCHEMA_VERSION
      :type:  Any


   .. py:attribute:: MISSING_FILE
      :type:  Any


   .. py:attribute:: MALFORMED_JSON
      :type:  Any


   .. py:attribute:: INVALID_STRUCTURE
      :type:  Any


   .. py:attribute:: MISSING_PLAN_HASH
      :type:  Any


   .. py:attribute:: HASH_MISMATCH
      :type:  Any


   .. py:attribute:: MISSING_REQUIRED_FIELD
      :type:  Any


   .. py:attribute:: INVALID_SPLITS
      :type:  Any


   .. py:attribute:: LEAKAGE_DETECTED
      :type:  Any


   .. py:attribute:: PURGE_VIOLATION
      :type:  Any


   .. py:attribute:: EMBARGO_VIOLATION
      :type:  Any


   .. py:attribute:: INVALID_CONFIG
      :type:  Any


   .. py:attribute:: STAT_VALIDITY_INVALID_STRUCTURE
      :type:  Any


   .. py:attribute:: STAT_VALIDITY_GATE_FAIL
      :type:  Any


   .. py:attribute:: COST_ASSUMPTION_MISSING
      :type:  Any


   .. py:attribute:: COST_GATE_REJECTED
      :type:  Any


   .. py:attribute:: ZERO_COST_ASSUMED
      :type:  Any


   .. py:attribute:: EXECUTION_ASSUMPTIONS_INVALID_STRUCTURE
      :type:  Any


   .. py:attribute:: PIT_NON_COMPLIANT
      :type:  Any


   .. py:attribute:: MISSING_KNOWLEDGE_TIME_COLUMN
      :type:  Any


   .. py:attribute:: CONTENT_HASH_MISMATCH
      :type:  Any


   .. py:attribute:: STALE_DOWNLOAD_WARNING
      :type:  Any


   .. py:attribute:: INVALID_DETERMINISM_TIER
      :type:  Any


   .. py:attribute:: INVALID_REPRODUCIBILITY_METADATA
      :type:  Any


.. py:data:: INVALID_INPUT_REASON_CODES
   :type:  Any

.. py:class:: GateCheck

   .. py:attribute:: gate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: result
      :type:  str
      :value: Ellipsis



   .. py:attribute:: reason_code
      :type:  str
      :value: Ellipsis



   .. py:attribute:: message
      :type:  str
      :value: Ellipsis



   .. py:attribute:: evidence
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:method:: to_dict()


.. py:class:: GateReport

   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: bundle_path
      :type:  str
      :value: Ellipsis



   .. py:attribute:: timestamp
      :type:  str
      :value: Ellipsis



   .. py:attribute:: overall_result
      :type:  str
      :value: Ellipsis



   .. py:attribute:: gates
      :type:  list[dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:method:: add_check(check)


   .. py:method:: to_dict()


   .. py:method:: to_json(path)


.. py:function:: resolve_gate_output_path(output_path, bundle_path)

.. py:function:: write_gate_report(report, output_path, bundle_path)

.. py:function:: emit_gate_failure_report(bundle_path, *, gate_id, reason_code, message, evidence = ..., output_path = ...)

.. py:data:: REQUIRED_BUNDLE_FILES
   :type:  Any

.. py:data:: OPTIONAL_BUNDLE_FILES
   :type:  Any

.. py:data:: PLAN_REQUIRED_FIELDS
   :type:  Any

.. py:data:: ENV_REQUIRED_FIELDS
   :type:  Any

.. py:data:: DATASET_REQUIRED_FIELDS
   :type:  Any

.. py:data:: PREPROCESSING_REQUIRED_FIELDS
   :type:  Any

.. py:data:: SPLITS_REQUIRED_FIELDS
   :type:  Any

.. py:function:: validate_bundle_exists(bundle_path, report)

.. py:function:: validate_required_files(bundle_path, report)

.. py:function:: validate_plan_identity(bundle_path, report, expected_plan_hash = ...)

.. py:function:: validate_env_fingerprint(bundle_path, report)

.. py:function:: validate_dataset_manifest(bundle_path, report)

.. py:class:: DataLineageGate(*, max_download_age_days = ...)

   .. py:method:: validate(bundle_path, report)


.. py:data:: DATA_LINEAGE_GATE
   :type:  Any

.. py:function:: validate_preprocessing_report(bundle_path, report)

.. py:function:: validate_splits_manifest(bundle_path, report)

.. py:function:: validate_leakage_invariants(bundle_path, report)

.. py:function:: validate_splits_integrity(bundle_path, report)

.. py:data:: STAT_VALIDITY_REQUIRED_KEYS
   :type:  Any

.. py:data:: STAT_VALIDITY_GATE_VALUES
   :type:  Any

.. py:data:: STAT_VALIDITY_STRUCTURED_SECTIONS
   :type:  Any

.. py:function:: validate_stat_validity_report(bundle_path, report)

.. py:data:: EXECUTION_ASSUMPTIONS_REQUIRED_KEYS
   :type:  Any

.. py:data:: EXECUTION_ASSUMPTIONS_COST_KEYS
   :type:  Any

.. py:function:: validate_execution_assumptions(bundle_path, report)

.. py:function:: validate_bundle(bundle_path, output_path = ..., expected_plan_hash = ...)

.. py:function:: main(argv = ...)

