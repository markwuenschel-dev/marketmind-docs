pysrc.meta.allocator_benchmark.w3_b_selected_decisions
======================================================

.. py:module:: pysrc.meta.allocator_benchmark.w3_b_selected_decisions


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3_B_SELECTED_DECISIONS_SCHEMA_VERSION
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3_B_SELECTED_DECISIONS_VALIDATION_SCHEMA_VERSION
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3_B_SELECTED_DECISIONS_RELATIVE_PATH
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3_B_ALL_CHILD_POLICY_DECISIONS_RELATIVE_PATH
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3_B_CHILD_POLICY_REPORT_RELATIVE_PATH
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3_B_LINEAGE_CORRECTION_RELATIVE_PATH
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3_B_SELECTED_DECISIONS_VALIDATION_RELATIVE_PATH
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3_B_ALL_CHILD_VALIDATION_RELATIVE_PATH
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3_B_SELECTED_DECISIONS_TOLERANCE
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3_B_ALL_CHILD_VALIDATION_SCHEMA_VERSION
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3B_SOURCE_DECISIONS_KIND
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.FROZEN_W3B_SURFACE_BEST_TA_UTILITY
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3_B_LEGACY_LINEAGE_SOURCE
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3_B_REPRODUCIBLE_LINEAGE_SOURCE
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3_B_SELECTED_DECISIONS_SURFACES
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.REQUIRED_SELECTED_DECISION_COLUMNS


Exceptions
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.SelectedDecisionsValidationError


Classes
-------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.SelectedDecisionsValidationResult
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.AllChildDecisionsValidationResult
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.W3BDecisionProvenance


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.selected_decisions_path
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.selected_decisions_validation_path
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.all_child_policy_decisions_path
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.child_policy_report_path
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.lineage_correction_path
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.all_child_validation_report_path
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.build_surface_selected_decisions_frame
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.write_selected_decisions_parquet
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.build_surface_all_child_policy_decisions_frame
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.write_all_child_policy_decisions_parquet
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.load_frozen_w3b_child_decisions
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.load_w3b_lineage_correction
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.resolve_w3b_surface_provenance
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.validate_all_child_policy_decisions_parquet
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.aggregate_surface_test_utility
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.validate_selected_decisions_parquet
   pysrc.meta.allocator_benchmark.w3_b_selected_decisions.assert_selected_decisions_valid


Module Contents
---------------

.. py:data:: W3_B_SELECTED_DECISIONS_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W3_B_SELECTED_DECISIONS_VALIDATION_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W3_B_SELECTED_DECISIONS_RELATIVE_PATH
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W3_B_ALL_CHILD_POLICY_DECISIONS_RELATIVE_PATH
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W3_B_CHILD_POLICY_REPORT_RELATIVE_PATH
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W3_B_LINEAGE_CORRECTION_RELATIVE_PATH
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W3_B_SELECTED_DECISIONS_VALIDATION_RELATIVE_PATH
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W3_B_ALL_CHILD_VALIDATION_RELATIVE_PATH
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W3_B_SELECTED_DECISIONS_TOLERANCE
   :type:  Final[float]
   :value: Ellipsis


.. py:data:: W3_B_ALL_CHILD_VALIDATION_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W3B_SOURCE_DECISIONS_KIND
   :type:  Any

.. py:data:: FROZEN_W3B_SURFACE_BEST_TA_UTILITY
   :type:  Final[dict[str, float]]
   :value: Ellipsis


.. py:data:: W3_B_LEGACY_LINEAGE_SOURCE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W3_B_REPRODUCIBLE_LINEAGE_SOURCE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W3_B_SELECTED_DECISIONS_SURFACES
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:data:: REQUIRED_SELECTED_DECISION_COLUMNS
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:exception:: SelectedDecisionsValidationError

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:class:: SelectedDecisionsValidationResult

   .. py:attribute:: report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: report_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: passed
      :type:  bool
      :value: Ellipsis



.. py:class:: AllChildDecisionsValidationResult

   .. py:attribute:: report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: report_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: passed
      :type:  bool
      :value: Ellipsis



.. py:class:: W3BDecisionProvenance

   .. py:attribute:: source_decisions_kind
      :type:  W3B_SOURCE_DECISIONS_KIND
      :value: Ellipsis



   .. py:attribute:: source_artifact_path
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: all_child_artifact_path
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: frozen_target_utility
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: legacy_frozen_value
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: lineage_source
      :type:  str
      :value: Ellipsis



   .. py:attribute:: lineage_correction_path
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: reconstructed_utility
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: selected_child_parity_passed
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: all_child_parity_passed
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: metrics_admissible
      :type:  bool
      :value: Ellipsis



   .. py:method:: to_dict()


.. py:function:: selected_decisions_path(w3_b_dir)

.. py:function:: selected_decisions_validation_path(w3_b_dir)

.. py:function:: all_child_policy_decisions_path(w3_b_dir)

.. py:function:: child_policy_report_path(w3_b_dir)

.. py:function:: lineage_correction_path(w3_b_dir)

.. py:function:: all_child_validation_report_path(w3_b_dir)

.. py:function:: build_surface_selected_decisions_frame(surface_id, child_decisions, *, active_table = ...)

.. py:function:: write_selected_decisions_parquet(output_path, surface_frames)

.. py:function:: build_surface_all_child_policy_decisions_frame(surface_id, child_decisions)

.. py:function:: write_all_child_policy_decisions_parquet(output_path, surface_frames)

.. py:function:: load_frozen_w3b_child_decisions(surface_id, w3_b_dir)

.. py:function:: load_w3b_lineage_correction(w3_b_dir)

.. py:function:: resolve_w3b_surface_provenance(surface_id, *, w3_b_dir, frozen_utilities = ...)

.. py:function:: validate_all_child_policy_decisions_parquet(all_child_path, *, selected_decisions_path, child_policy_report_path, frozen_utilities = ..., output_report_path = ...)

.. py:function:: aggregate_surface_test_utility(frame, surface_id)

.. py:function:: validate_selected_decisions_parquet(parquet_path, *, frozen_utilities = ..., output_report_path = ..., source_metadata = ...)

.. py:function:: assert_selected_decisions_valid(parquet_path, *, frozen_utilities = ..., source_metadata = ...)

