pysrc.meta.allocator_benchmark.w3_c_liquidity_child
===================================================

.. py:module:: pysrc.meta.allocator_benchmark.w3_c_liquidity_child


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.W3_C_LIQUIDITY_CHILD_DIR


Classes
-------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.W3CLiquidityChildRunResult


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.run_w3_c_liquidity_child_experiment
   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.run_w3_c_liquidity_child_policies
   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.attach_rolling_liquidity
   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.liquidity_score_multipliers
   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.apply_liquidity_score_penalty
   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.load_w3_b_frozen_baselines
   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.best_w3_c_liquidity_child_utility
   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.best_w3_b_ta_utility
   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.participation_from_policy_metrics
   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.participation_snapshot
   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.build_w3_c_tradeoff_report
   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.classify_w3_c
   pysrc.meta.allocator_benchmark.w3_c_liquidity_child.regenerate_w3_c_closeout_artifacts


Module Contents
---------------

.. py:data:: W3_C_LIQUIDITY_CHILD_DIR
   :type:  Final[Path]
   :value: Ellipsis


.. py:class:: W3CLiquidityChildRunResult

   .. py:attribute:: child_policy_report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: tradeoff_report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: summary_path
      :type:  Path
      :value: Ellipsis



.. py:function:: run_w3_c_liquidity_child_experiment(*, source_path = ..., source_panel = ..., output_dir = ..., config = ...)

.. py:function:: run_w3_c_liquidity_child_policies(rows, *, active_indicators, orientations, config, penalty_spec, w3_b_config = ..., w2_config = ...)

.. py:function:: attach_rolling_liquidity(table)

.. py:function:: liquidity_score_multipliers(table, spec)

.. py:function:: apply_liquidity_score_penalty(scores, table, spec)

.. py:function:: load_w3_b_frozen_baselines(path)

.. py:function:: best_w3_c_liquidity_child_utility(child_surface)

.. py:function:: best_w3_b_ta_utility(child_surface)

.. py:function:: participation_from_policy_metrics(metrics)

.. py:function:: participation_snapshot(decisions, policy_id)

.. py:function:: build_w3_c_tradeoff_report(child_surfaces, *, w3_b_baselines, penalty_spec, child_decisions_by_surface = ...)

.. py:function:: classify_w3_c(tradeoff)

.. py:function:: regenerate_w3_c_closeout_artifacts(*, report_path = ..., output_dir = ..., closeout_notes_path = ...)

