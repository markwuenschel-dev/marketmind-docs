pysrc.pipeline.stages.market_data.transforms
============================================

.. py:module:: pysrc.pipeline.stages.market_data.transforms


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.transforms.logger
   pysrc.pipeline.stages.market_data.transforms.TRANSFORM_STEPS
   pysrc.pipeline.stages.market_data.transforms.TRANSFORM_CONFIGS


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.transforms.ColumnRenameConfig
   pysrc.pipeline.stages.market_data.transforms.ColumnRenameStep
   pysrc.pipeline.stages.market_data.transforms.TypeCastConfig
   pysrc.pipeline.stages.market_data.transforms.TypeCastStep


Functions
---------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.transforms.build_steps
   pysrc.pipeline.stages.market_data.transforms.build_transform_steps


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:class:: ColumnRenameConfig

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: mapping
      :type:  Dict[str, str]
      :value: Ellipsis



.. py:class:: ColumnRenameStep(config)

   Bases: :py:obj:`PipelineStep`


   .. py:method:: apply(lf)


.. py:class:: TypeCastConfig

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: dtypes
      :type:  Dict[str, pl.DataType]
      :value: Ellipsis



.. py:class:: TypeCastStep(config)

   Bases: :py:obj:`PipelineStep`


   .. py:method:: apply(lf)


.. py:data:: TRANSFORM_STEPS
   :type:  Dict[str, Type[PipelineStep]]
   :value: Ellipsis


.. py:data:: TRANSFORM_CONFIGS
   :type:  Dict[str, Type[BaseModel]]
   :value: Ellipsis


.. py:function:: build_steps(configs, step_registry, config_registry)

.. py:function:: build_transform_steps(configs)

