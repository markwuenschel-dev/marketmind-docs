pysrc.pipeline.stages.cleaning.imputers.outliers
================================================

.. py:module:: pysrc.pipeline.stages.cleaning.imputers.outliers


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.imputers.outliers.OutlierParams
   pysrc.pipeline.stages.cleaning.imputers.outliers.OutlierNormalizerStep


Module Contents
---------------

.. py:class:: OutlierParams

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: method
      :type:  Literal['zscore', 'iqr']
      :value: Ellipsis



   .. py:attribute:: threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: factor
      :type:  float
      :value: Ellipsis



.. py:class:: OutlierNormalizerStep

   Bases: :py:obj:`CleaningStep`


