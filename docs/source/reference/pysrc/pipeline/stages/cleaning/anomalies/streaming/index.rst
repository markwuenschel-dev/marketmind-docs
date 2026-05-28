pysrc.pipeline.stages.cleaning.anomalies.streaming
==================================================

.. py:module:: pysrc.pipeline.stages.cleaning.anomalies.streaming


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.anomalies.streaming.StreamingIsolationForest
   pysrc.pipeline.stages.cleaning.anomalies.streaming.StreamingAnomalyParams
   pysrc.pipeline.stages.cleaning.anomalies.streaming.StreamingAnomalyNormalizerStep


Module Contents
---------------

.. py:class:: StreamingIsolationForest(contamination, refit_every, window_size = ..., *, random_state = ...)

   .. py:method:: predict(df)


.. py:class:: StreamingAnomalyParams

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: contamination
      :type:  float
      :value: Ellipsis



   .. py:attribute:: refit_every
      :type:  int
      :value: Ellipsis



   .. py:attribute:: window_size
      :type:  int
      :value: Ellipsis



.. py:class:: StreamingAnomalyNormalizerStep

   Bases: :py:obj:`CleaningStep`


