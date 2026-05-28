pysrc.meta.allocator_benchmark.w4_b_learned_router
==================================================

.. py:module:: pysrc.meta.allocator_benchmark.w4_b_learned_router


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w4_b_learned_router.W4_B_OUTPUT_DIR
   pysrc.meta.allocator_benchmark.w4_b_learned_router.W4B_REPORT_SCHEMA_VERSION
   pysrc.meta.allocator_benchmark.w4_b_learned_router.W4B_PREDICTION_SCHEMA_VERSION
   pysrc.meta.allocator_benchmark.w4_b_learned_router.W4B_PRIMARY_BUNDLE
   pysrc.meta.allocator_benchmark.w4_b_learned_router.W4B_PRIMARY_SURFACE
   pysrc.meta.allocator_benchmark.w4_b_learned_router.W4B_STRESS_SURFACES
   pysrc.meta.allocator_benchmark.w4_b_learned_router.W4B_REPORT_NAME
   pysrc.meta.allocator_benchmark.w4_b_learned_router.W4B_PREDICTIONS_NAME
   pysrc.meta.allocator_benchmark.w4_b_learned_router.W4B_SUMMARY_NAME


Classes
-------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w4_b_learned_router.W4BLearnedRouterResult


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w4_b_learned_router.run_w4_b_learned_router
   pysrc.meta.allocator_benchmark.w4_b_learned_router.build_w4_b_date_level_frame
   pysrc.meta.allocator_benchmark.w4_b_learned_router.is_w4b_allowed_feature_name
   pysrc.meta.allocator_benchmark.w4_b_learned_router.w4b_target_column
   pysrc.meta.allocator_benchmark.w4_b_learned_router.w4b_target_matrix
   pysrc.meta.allocator_benchmark.w4_b_learned_router.compute_w4b_comparators
   pysrc.meta.allocator_benchmark.w4_b_learned_router.split_w4b_prediction_utility


Module Contents
---------------

.. py:data:: W4_B_OUTPUT_DIR
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: W4B_REPORT_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W4B_PREDICTION_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W4B_PRIMARY_BUNDLE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W4B_PRIMARY_SURFACE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W4B_STRESS_SURFACES
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:data:: W4B_REPORT_NAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W4B_PREDICTIONS_NAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W4B_SUMMARY_NAME
   :type:  Final[str]
   :value: Ellipsis


.. py:class:: W4BLearnedRouterResult

   .. py:attribute:: report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: predictions
      :type:  pd.DataFrame
      :value: Ellipsis



   .. py:attribute:: report_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: predictions_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: summary_path
      :type:  Path
      :value: Ellipsis



.. py:function:: run_w4_b_learned_router(*, input_dir = ..., output_dir = ..., primary_bundle = ..., primary_surface = ..., stress_surfaces = ..., include_xgboost = ..., include_elastic_net = ..., ridge_alpha = ..., random_seed = ..., xgboost_n_jobs = ..., progress = ...)

.. py:function:: build_w4_b_date_level_frame(supervision, *, bundle_id = ..., surface_id = ...)

.. py:function:: is_w4b_allowed_feature_name(name)

.. py:function:: w4b_target_column(child_id)

.. py:function:: w4b_target_matrix(rows, child_policy_ids)

.. py:function:: compute_w4b_comparators(date_frame, *, child_policy_ids, random_seed)

.. py:function:: split_w4b_prediction_utility(predictions, split, *, utility_column = ...)

