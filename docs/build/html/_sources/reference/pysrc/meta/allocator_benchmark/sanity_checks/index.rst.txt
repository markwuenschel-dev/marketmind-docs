pysrc.meta.allocator_benchmark.sanity_checks
============================================

.. py:module:: pysrc.meta.allocator_benchmark.sanity_checks


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.sanity_checks.W2_V2_SANITY_OUTPUT_DIR
   pysrc.meta.allocator_benchmark.sanity_checks.W2_V2_SANITY_REPORT_NAME
   pysrc.meta.allocator_benchmark.sanity_checks.W2_V2_SANITY_SUMMARY_NAME
   pysrc.meta.allocator_benchmark.sanity_checks.W2_V2_DEFAULT_SANITY_SEEDS
   pysrc.meta.allocator_benchmark.sanity_checks.W2_V2_DEFAULT_COST_MULTIPLIERS
   pysrc.meta.allocator_benchmark.sanity_checks.W2_V2_DEFAULT_TOP_K_VALUES


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.sanity_checks.run_w2_v2_sanity_checks
   pysrc.meta.allocator_benchmark.sanity_checks.build_w2_v2_sanity_payload


Module Contents
---------------

.. py:data:: W2_V2_SANITY_OUTPUT_DIR
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: W2_V2_SANITY_REPORT_NAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W2_V2_SANITY_SUMMARY_NAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W2_V2_DEFAULT_SANITY_SEEDS
   :type:  Final[tuple[int, Ellipsis]]
   :value: Ellipsis


.. py:data:: W2_V2_DEFAULT_COST_MULTIPLIERS
   :type:  Final[tuple[float, Ellipsis]]
   :value: Ellipsis


.. py:data:: W2_V2_DEFAULT_TOP_K_VALUES
   :type:  Final[tuple[int, Ellipsis]]
   :value: Ellipsis


.. py:function:: run_w2_v2_sanity_checks(*, freeze_manifest_path = ..., baseline_report_path = ..., signal_rows_path = ..., accepted_w2_v2_report_path = ..., output_dir = ..., seeds = ..., cost_multipliers = ..., top_k_values = ..., expected_baseline_report_hash = ...)

.. py:function:: build_w2_v2_sanity_payload(*, default_decision_rows, baseline_records, config, seed_decision_rows, primary_seed, cost_multipliers = ..., top_k_values = ..., source_metadata = ...)

