pysrc.pipeline.stages.cleaning.imputers.denoise
===============================================

.. py:module:: pysrc.pipeline.stages.cleaning.imputers.denoise


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.imputers.denoise.DenoiseParams
   pysrc.pipeline.stages.cleaning.imputers.denoise.DenoiseNormalizerStep


Module Contents
---------------

.. py:class:: DenoiseParams

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: method
      :type:  Literal['ewm', 'minmax']
      :value: Ellipsis



   .. py:attribute:: span
      :type:  int
      :value: Ellipsis



.. py:class:: DenoiseNormalizerStep

   Bases: :py:obj:`CleaningStep`


