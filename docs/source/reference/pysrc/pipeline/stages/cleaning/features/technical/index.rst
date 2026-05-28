pysrc.pipeline.stages.cleaning.features.technical
=================================================

.. py:module:: pysrc.pipeline.stages.cleaning.features.technical


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.features.technical.RSIParams
   pysrc.pipeline.stages.cleaning.features.technical.RSINormalizerStep
   pysrc.pipeline.stages.cleaning.features.technical.MACDParams
   pysrc.pipeline.stages.cleaning.features.technical.MACDNormalizerStep
   pysrc.pipeline.stages.cleaning.features.technical.ATRParams
   pysrc.pipeline.stages.cleaning.features.technical.ATRNormalizerStep
   pysrc.pipeline.stages.cleaning.features.technical.VWAPParams
   pysrc.pipeline.stages.cleaning.features.technical.VWAPNormalizerStep


Module Contents
---------------

.. py:class:: RSIParams

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: output_column
      :type:  str
      :value: Ellipsis



   .. py:attribute:: close_column
      :type:  str
      :value: Ellipsis



   .. py:attribute:: fillna_method
      :type:  str
      :value: Ellipsis



.. py:class:: RSINormalizerStep

   Bases: :py:obj:`CleaningStep`


.. py:class:: MACDParams

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: fast
      :type:  int
      :value: Ellipsis



   .. py:attribute:: slow
      :type:  int
      :value: Ellipsis



   .. py:attribute:: signal
      :type:  int
      :value: Ellipsis



   .. py:attribute:: close_column
      :type:  str
      :value: Ellipsis



   .. py:attribute:: macd_column
      :type:  str
      :value: Ellipsis



   .. py:attribute:: signal_column
      :type:  str
      :value: Ellipsis



.. py:class:: MACDNormalizerStep

   Bases: :py:obj:`CleaningStep`


.. py:class:: ATRParams

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: output_column
      :type:  str
      :value: Ellipsis



   .. py:attribute:: high_column
      :type:  str
      :value: Ellipsis



   .. py:attribute:: low_column
      :type:  str
      :value: Ellipsis



   .. py:attribute:: close_column
      :type:  str
      :value: Ellipsis



.. py:class:: ATRNormalizerStep

   Bases: :py:obj:`CleaningStep`


.. py:class:: VWAPParams

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: output_column
      :type:  str
      :value: Ellipsis



   .. py:attribute:: high_column
      :type:  str
      :value: Ellipsis



   .. py:attribute:: low_column
      :type:  str
      :value: Ellipsis



   .. py:attribute:: close_column
      :type:  str
      :value: Ellipsis



   .. py:attribute:: volume_column
      :type:  str
      :value: Ellipsis



.. py:class:: VWAPNormalizerStep

   Bases: :py:obj:`CleaningStep`


