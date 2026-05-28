pysrc.meta.allocator_benchmark.w4_a_router_opportunity
======================================================

.. py:module:: pysrc.meta.allocator_benchmark.w4_a_router_opportunity


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4_A_OUTPUT_DIR
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4A_SUPERVISION_SCHEMA_VERSION
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4A_REPORT_SCHEMA_VERSION
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4A_VALIDATION_SCHEMA_VERSION
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4A_PRIMARY_BUNDLE
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4A_SENSITIVITY_BUNDLE
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4A_GATE_SURFACE
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4A_SURFACES_PRIMARY
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4A_SURFACES_SENSITIVITY
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4A_RELATIVE_GAP_MIN
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4A_CAPTURE_CEILING_MAX
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4A_ROW_UPLIFT_MIN
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4A_ORACLE_VS_BEST_CHILD_MIN_GAP
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4ADecisionProvenance


Classes
-------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.W4ARouterOpportunityResult


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.run_w4_a_router_opportunity_audit
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.build_router_supervision_dataset
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.oracle_router_by_row
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.compute_router_opportunity_metrics
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.evaluate_w4b_gate
   pysrc.meta.allocator_benchmark.w4_a_router_opportunity.validate_router_supervision_dataset


Module Contents
---------------

.. py:data:: W4_A_OUTPUT_DIR
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: W4A_SUPERVISION_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W4A_REPORT_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W4A_VALIDATION_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W4A_PRIMARY_BUNDLE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W4A_SENSITIVITY_BUNDLE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W4A_GATE_SURFACE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W4A_SURFACES_PRIMARY
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:data:: W4A_SURFACES_SENSITIVITY
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:data:: W4A_RELATIVE_GAP_MIN
   :type:  Final[float]
   :value: Ellipsis


.. py:data:: W4A_CAPTURE_CEILING_MAX
   :type:  Final[float]
   :value: Ellipsis


.. py:data:: W4A_ROW_UPLIFT_MIN
   :type:  Final[float]
   :value: Ellipsis


.. py:data:: W4A_ORACLE_VS_BEST_CHILD_MIN_GAP
   :type:  Final[float]
   :value: Ellipsis


.. py:data:: W4ADecisionProvenance
   :type:  Any

.. py:class:: W4ARouterOpportunityResult

   .. py:attribute:: report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: validation
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: report_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: validation_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: summary_path
      :type:  Path
      :value: Ellipsis



.. py:function:: run_w4_a_router_opportunity_audit(*, source_path = ..., source_panel = ..., output_dir = ..., w3b_config = ..., w3a_config = ..., w3b_artifact_dir = ..., allow_rerun_diagnostics = ..., bundles = ..., surfaces_by_bundle = ..., progress = ...)

.. py:function:: build_router_supervision_dataset(child_decisions, *, bundle_id, surface_id, panel_context = ..., child_policy_ids = ...)

.. py:function:: oracle_router_by_row(child_decisions)

.. py:function:: compute_router_opportunity_metrics(child_decisions, *, child_policy_ids, w2_config)

.. py:function:: evaluate_w4b_gate(primary_bundle, *, validation_passed, surface_b_provenance = ...)

.. py:function:: validate_router_supervision_dataset(supervision, *, child_decisions, metrics, bundle_id, surface_id)

