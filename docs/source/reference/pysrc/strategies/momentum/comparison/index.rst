pysrc.strategies.momentum.comparison
====================================

.. py:module:: pysrc.strategies.momentum.comparison


Classes
-------

.. autoapisummary::

   pysrc.strategies.momentum.comparison.ComparisonRunResult


Functions
---------

.. autoapisummary::

   pysrc.strategies.momentum.comparison.run_variant_comparison


Module Contents
---------------

.. py:class:: ComparisonRunResult

   .. py:attribute:: bundle_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: comparison_run_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: variant_runs
      :type:  dict[str, RunResult]
      :value: Ellipsis



.. py:function:: run_variant_comparison(ctx, *, bundle_dir = ..., run_registry = ..., cas = ..., commission_bps = ..., slippage_bps = ..., cost_model_id = ..., purge_window = ..., embargo_window = ..., min_train_size = ...)

