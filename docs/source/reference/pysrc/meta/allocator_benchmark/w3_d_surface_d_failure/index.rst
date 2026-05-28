pysrc.meta.allocator_benchmark.w3_d_surface_d_failure
=====================================================

.. py:module:: pysrc.meta.allocator_benchmark.w3_d_surface_d_failure


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.W3_D_OUTPUT_DIR
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.W3_D_AUDIT_SCHEMA_VERSION
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.W3_D_REPLAY_TOLERANCE
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.W3_D_SHARE_SUM_TOLERANCE
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.W3_B_CHILD_REPORT
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.W3_B_ROUTER_REPORT
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.W3_B_SUMMARY
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.W3_C_CHILD_REPORT
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.W3_C_CLOSEOUT_NOTES
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.FROZEN_W3B_SURFACE_BEST_TA_UTILITY
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.FROZEN_W3B_SURFACE_BEST_TA_UTILITY_DISPLAY
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.SURFACE_D_W3B_DIAGNOSTICS
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.W3_D_SURFACES
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.W3_D_CLASSIFICATIONS


Classes
-------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.W3DPrerequisiteStatus
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.W3DSurfaceDAuditResult


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.run_w3_d_surface_d_failure_audit
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.validate_w3_d_prerequisites
   pysrc.meta.allocator_benchmark.w3_d_surface_d_failure.aggregate_exported_surface_utility


Module Contents
---------------

.. py:data:: W3_D_OUTPUT_DIR
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: W3_D_AUDIT_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W3_D_REPLAY_TOLERANCE
   :type:  Final[float]
   :value: Ellipsis


.. py:data:: W3_D_SHARE_SUM_TOLERANCE
   :type:  Final[float]
   :value: Ellipsis


.. py:data:: W3_B_CHILD_REPORT
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: W3_B_ROUTER_REPORT
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: W3_B_SUMMARY
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: W3_C_CHILD_REPORT
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: W3_C_CLOSEOUT_NOTES
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: FROZEN_W3B_SURFACE_BEST_TA_UTILITY
   :type:  Final[dict[str, float]]
   :value: Ellipsis


.. py:data:: FROZEN_W3B_SURFACE_BEST_TA_UTILITY_DISPLAY
   :type:  Final[dict[str, float]]
   :value: Ellipsis


.. py:data:: SURFACE_D_W3B_DIAGNOSTICS
   :type:  Final[dict[str, float]]
   :value: Ellipsis


.. py:data:: W3_D_SURFACES
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:data:: W3_D_CLASSIFICATIONS
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:class:: W3DPrerequisiteStatus

   .. py:attribute:: missing
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: stale_schema
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



.. py:class:: W3DSurfaceDAuditResult

   .. py:attribute:: audit_json_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: audit_md_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: audit_report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: replay_required
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: replay_validation_passed
      :type:  bool
      :value: Ellipsis



.. py:function:: run_w3_d_surface_d_failure_audit(*, w3_b_dir = ..., w3_c_child_report_path = ..., w3_c_closeout_notes_path = ..., output_dir = ..., source_path = ..., source_panel = ..., w3_b_config = ..., utility_anchor = ..., skip_prerequisite_gate = ...)

.. py:function:: validate_w3_d_prerequisites(*, w3_b_dir, w3_c_child_report_path, w3_c_closeout_notes_path)

.. py:function:: aggregate_exported_surface_utility(frame, surface_id)

