pysrc.pipeline.stages.cleaning.imputers.missing
===============================================

.. py:module:: pysrc.pipeline.stages.cleaning.imputers.missing


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.imputers.missing.logger
   pysrc.pipeline.stages.cleaning.imputers.missing.KalmanFilter


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.imputers.missing.MissingValueParams
   pysrc.pipeline.stages.cleaning.imputers.missing.MissingValueNormalizerStep


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:data:: KalmanFilter
   :type:  Any

.. py:class:: MissingValueParams

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: method
      :type:  Literal['forward_fill', 'backward_fill', 'interpolate', 'median', 'kalman']
      :value: Ellipsis



   .. py:attribute:: backward_fill
      :type:  bool
      :value: Ellipsis



.. py:class:: MissingValueNormalizerStep

   Bases: :py:obj:`CleaningStep`


