pysrc.pipeline.stages.market_data.compliance
============================================

.. py:module:: pysrc.pipeline.stages.market_data.compliance


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.compliance.logger
   pysrc.pipeline.stages.market_data.compliance.COMPLIANCE_STEPS
   pysrc.pipeline.stages.market_data.compliance.COMPLIANCE_CONFIGS


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.compliance.AnonymizationConfig
   pysrc.pipeline.stages.market_data.compliance.DataAnonymizationStep
   pysrc.pipeline.stages.market_data.compliance.RegulatoryFilterConfig
   pysrc.pipeline.stages.market_data.compliance.RegulatoryFilterStep


Functions
---------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.compliance.get_hash_func
   pysrc.pipeline.stages.market_data.compliance.build_compliance_steps


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:class:: AnonymizationConfig

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: sensitive_columns
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: hash_algorithm
      :type:  str
      :value: Ellipsis



   .. py:attribute:: salt
      :type:  Optional[str]
      :value: Ellipsis



.. py:function:: get_hash_func(algo, salt = ...)

.. py:class:: DataAnonymizationStep(config)

   Bases: :py:obj:`PipelineStep`


   .. py:method:: apply(lf)


.. py:class:: RegulatoryFilterConfig

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: restricted_symbols
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: min_volume_threshold
      :type:  Optional[float]
      :value: Ellipsis



.. py:class:: RegulatoryFilterStep(config)

   Bases: :py:obj:`PipelineStep`


   .. py:method:: apply(lf)


.. py:data:: COMPLIANCE_STEPS
   :type:  Dict[str, Type[PipelineStep]]
   :value: Ellipsis


.. py:data:: COMPLIANCE_CONFIGS
   :type:  Dict[str, Type[BaseModel]]
   :value: Ellipsis


.. py:function:: build_compliance_steps(configs)

