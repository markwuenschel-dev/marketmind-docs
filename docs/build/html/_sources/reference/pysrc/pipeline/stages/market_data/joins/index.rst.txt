pysrc.pipeline.stages.market_data.joins
=======================================

.. py:module:: pysrc.pipeline.stages.market_data.joins


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.joins.logger
   pysrc.pipeline.stages.market_data.joins.SOURCE_REGISTRY
   pysrc.pipeline.stages.market_data.joins.AGG_MAP
   pysrc.pipeline.stages.market_data.joins.JOIN_STEPS
   pysrc.pipeline.stages.market_data.joins.JOIN_CONFIGS


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.joins.JoinSpec
   pysrc.pipeline.stages.market_data.joins.MultiSourceJoinConfig
   pysrc.pipeline.stages.market_data.joins.MultiSourceJoinStep
   pysrc.pipeline.stages.market_data.joins.ResampleConfig
   pysrc.pipeline.stages.market_data.joins.ResampleStep


Functions
---------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.joins.build_join_steps


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:data:: SOURCE_REGISTRY
   :type:  Dict[str, LazyFrame]
   :value: Ellipsis


.. py:class:: JoinSpec

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: source_name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: on
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: how
      :type:  str
      :value: Ellipsis



   .. py:attribute:: suffix
      :type:  Optional[str]
      :value: Ellipsis



.. py:class:: MultiSourceJoinConfig

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: joins
      :type:  List[JoinSpec]
      :value: Ellipsis



.. py:class:: MultiSourceJoinStep(config)

   Bases: :py:obj:`PipelineStep`


   .. py:method:: apply(lf)


.. py:data:: AGG_MAP
   :type:  Dict[str, Callable]
   :value: Ellipsis


.. py:class:: ResampleConfig

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: freq
      :type:  str
      :value: Ellipsis



   .. py:attribute:: group_by
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: agg
      :type:  Dict[str, str]
      :value: Ellipsis



   .. py:attribute:: timestamp_col
      :type:  str
      :value: Ellipsis



.. py:class:: ResampleStep(config)

   Bases: :py:obj:`PipelineStep`


   .. py:method:: apply(lf)


.. py:data:: JOIN_STEPS
   :type:  Dict[str, Type[PipelineStep]]
   :value: Ellipsis


.. py:data:: JOIN_CONFIGS
   :type:  Dict[str, Type[BaseModel]]
   :value: Ellipsis


.. py:function:: build_join_steps(configs)

