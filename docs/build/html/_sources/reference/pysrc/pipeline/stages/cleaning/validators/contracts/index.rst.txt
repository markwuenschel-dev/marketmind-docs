pysrc.pipeline.stages.cleaning.validators.contracts
===================================================

.. py:module:: pysrc.pipeline.stages.cleaning.validators.contracts


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.validators.contracts.Bar
   pysrc.pipeline.stages.cleaning.validators.contracts.Tick
   pysrc.pipeline.stages.cleaning.validators.contracts.MarketDataFrameSchema


Module Contents
---------------

.. py:class:: Bar

   .. py:attribute:: timestamp
      :type:  pl.Datetime
      :value: Ellipsis



   .. py:attribute:: open
      :type:  float
      :value: Ellipsis



   .. py:attribute:: high
      :type:  float
      :value: Ellipsis



   .. py:attribute:: low
      :type:  float
      :value: Ellipsis



   .. py:attribute:: close
      :type:  float
      :value: Ellipsis



   .. py:attribute:: volume
      :type:  float
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  Mapping[str, Any]
      :value: Ellipsis



.. py:class:: Tick

   .. py:attribute:: timestamp
      :type:  pl.Datetime
      :value: Ellipsis



   .. py:attribute:: price
      :type:  float
      :value: Ellipsis



   .. py:attribute:: size
      :type:  float
      :value: Ellipsis



   .. py:attribute:: side
      :type:  str
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  Mapping[str, Any]
      :value: Ellipsis



.. py:class:: MarketDataFrameSchema

   .. py:attribute:: required_columns
      :type:  Mapping[str, pl.DataType]
      :value: Ellipsis



   .. py:attribute:: optional_columns
      :type:  Mapping[str, pl.DataType]
      :value: Ellipsis



   .. py:attribute:: strict
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: unknown_ok
      :type:  bool
      :value: Ellipsis



   .. py:method:: from_mapping(raw)


   .. py:method:: validate(df, *, strict = ..., unknown_ok = ...)


   .. py:method:: assert_valid(df, *, strict = ..., unknown_ok = ..., label = ...)


   .. py:method:: to_payload()


