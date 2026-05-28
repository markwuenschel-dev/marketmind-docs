pysrc.meta.rg09_artifacts
=========================

.. py:module:: pysrc.meta.rg09_artifacts


Attributes
----------

.. autoapisummary::

   pysrc.meta.rg09_artifacts.GATE_RESULT_FILENAME
   pysrc.meta.rg09_artifacts.RG09_SURFACE_MANIFEST_FILENAME
   pysrc.meta.rg09_artifacts.TASK_MANIFEST_FILENAME
   pysrc.meta.rg09_artifacts.DIAGNOSTICS_FILENAME
   pysrc.meta.rg09_artifacts.MACHINE_MANIFEST_FILENAME
   pysrc.meta.rg09_artifacts.PRODUCER_VERSION
   pysrc.meta.rg09_artifacts.ASSUMPTION_IDS


Functions
---------

.. autoapisummary::

   pysrc.meta.rg09_artifacts.build_task_manifest
   pysrc.meta.rg09_artifacts.build_gate_result
   pysrc.meta.rg09_artifacts.build_diagnostics
   pysrc.meta.rg09_artifacts.build_machine_manifest
   pysrc.meta.rg09_artifacts.write_rg09_artifacts


Module Contents
---------------

.. py:data:: GATE_RESULT_FILENAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: RG09_SURFACE_MANIFEST_FILENAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: TASK_MANIFEST_FILENAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: DIAGNOSTICS_FILENAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: MACHINE_MANIFEST_FILENAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: PRODUCER_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ASSUMPTION_IDS
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:function:: build_task_manifest(*, fixture_sha256, summary, admissible_row_count, admissible_episode_count, exclusion_counts)

.. py:function:: build_gate_result(*, decision, decision_reason, gate_executed, fixture_sha256, fixture_config_version, generation_timestamp, evidence, fail_codes, successor_hypotheses, hypothesis_id = ...)

.. py:function:: build_diagnostics(*, summary, exclusion_counts, null_summaries, admissible_episode_count, threshold_governance_preflight = ...)

.. py:function:: build_machine_manifest(*, version, output_dir, fixture_sha256, decision, producer_version, changes, tests, risks)

.. py:function:: write_rg09_artifacts(output_dir, *, gate_result, task_manifest, diagnostics, machine_manifest)

