pysrc.tuning.config.schemas.search_space
========================================

.. py:module:: pysrc.tuning.config.schemas.search_space


Classes
-------

.. autoapisummary::

   pysrc.tuning.config.schemas.search_space.DimensionConfig
   pysrc.tuning.config.schemas.search_space.SearchSpaceConfig


Module Contents
---------------

.. py:class:: DimensionConfig

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: kind
      :type:  Literal['real', 'int', 'categorical', 'log_real']
      :value: Ellipsis



   .. py:attribute:: low
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: high
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: choices
      :type:  list[Any] | None
      :value: Ellipsis



   .. py:attribute:: prior
      :type:  Literal['uniform', 'log-uniform']
      :value: Ellipsis



.. py:class:: SearchSpaceConfig

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: model_type
      :type:  str
      :value: Ellipsis



   .. py:attribute:: dimensions
      :type:  list[DimensionConfig]
      :value: Ellipsis



   .. py:attribute:: fixed
      :type:  dict[str, Any]
      :value: Ellipsis



