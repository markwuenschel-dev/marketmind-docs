pysrc.strategies.momentum.entry
===============================

.. py:module:: pysrc.strategies.momentum.entry


Classes
-------

.. autoapisummary::

   pysrc.strategies.momentum.entry.OrchestratorHooks
   pysrc.strategies.momentum.entry.RunResult


Functions
---------

.. autoapisummary::

   pysrc.strategies.momentum.entry.run


Module Contents
---------------

.. py:class:: OrchestratorHooks

   Bases: :py:obj:`Protocol`


   .. py:method:: apply_crash_override(*, trade_intent, alpha_ir, ctx, strategy)


   .. py:method:: apply_cost_gate(*, trade_intent, alpha_ir, ctx, strategy, execution_assumptions_path, bundle_dir)


.. py:class:: RunResult

   .. py:attribute:: trade_intent
      :type:  TradeIntent
      :value: Ellipsis



   .. py:attribute:: alpha_ir
      :type:  AlphaIR
      :value: Ellipsis



   .. py:attribute:: bundle_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: artifacts
      :type:  dict[str, Path]
      :value: Ellipsis



.. py:function:: run(ctx, *, variant = ..., orchestrator_hooks = ..., bundle_dir = ..., run_id = ..., run_registry = ..., cas = ..., enable_crash_override = ..., strategy = ..., **params)

