pysrc.pipeline.core.pipeline_core_builder
=========================================

.. py:module:: pysrc.pipeline.core.pipeline_core_builder


Classes
-------

.. autoapisummary::

   pysrc.pipeline.core.pipeline_core_builder.PipelineBuilder
   pysrc.pipeline.core.pipeline_core_builder.Pipeline


Functions
---------

.. autoapisummary::

   pysrc.pipeline.core.pipeline_core_builder.choose_combo
   pysrc.pipeline.core.pipeline_core_builder.topo_order


Module Contents
---------------

.. py:function:: choose_combo(cfg, ctx, name = ...)

.. py:function:: topo_order(steps, order_cfg)

.. py:class:: PipelineBuilder(stage, config = ...)

   .. py:method:: for_stage(stage, config = ...)


   .. py:method:: from_preset_and_params(preset, params)


   .. py:method:: add_steps(steps)


   .. py:method:: build()


   .. py:method:: validate_contracts()


.. py:class:: Pipeline(steps, config)

   .. py:method:: fit_transform(df)


