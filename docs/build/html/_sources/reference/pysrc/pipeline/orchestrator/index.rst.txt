pysrc.pipeline.orchestrator
===========================

.. py:module:: pysrc.pipeline.orchestrator


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.orchestrator.LOG


Classes
-------

.. autoapisummary::

   pysrc.pipeline.orchestrator.OrchestratorConfig


Functions
---------

.. autoapisummary::

   pysrc.pipeline.orchestrator.run_dataprep
   pysrc.pipeline.orchestrator.run_dataprep_from_path
   pysrc.pipeline.orchestrator.run_orchestration
   pysrc.pipeline.orchestrator.run


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:function:: run_dataprep(*args, **kwargs)

.. py:function:: run_dataprep_from_path(*args, **kwargs)

.. py:class:: OrchestratorConfig

   .. py:attribute:: input_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: fast_sma
      :type:  int
      :value: Ellipsis



   .. py:attribute:: slow_sma
      :type:  int
      :value: Ellipsis



   .. py:attribute:: bundle_dir
      :type:  Path | None
      :value: Ellipsis



.. py:function:: run_orchestration(config)

.. py:function:: run(strategy_id, ctx, strategy_kwargs, bundle_dir, *, pit_input = ..., knowledge_dates = ..., source_prices = ..., run_metadata = ..., strategy_instance = ..., run_id = ..., run_registry = ..., cas = ..., splits_manifest_override = ...)

