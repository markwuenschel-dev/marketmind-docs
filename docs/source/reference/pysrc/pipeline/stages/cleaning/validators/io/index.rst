pysrc.pipeline.stages.cleaning.validators.io
============================================

.. py:module:: pysrc.pipeline.stages.cleaning.validators.io


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.validators.io.FSInterface
   pysrc.pipeline.stages.cleaning.validators.io.LocalFS
   pysrc.pipeline.stages.cleaning.validators.io.IOValidationParams
   pysrc.pipeline.stages.cleaning.validators.io.IOValidationStep


Module Contents
---------------

.. py:class:: FSInterface

   .. py:method:: get_size(path)


.. py:class:: LocalFS

   Bases: :py:obj:`FSInterface`


   .. py:method:: get_size(path)


.. py:class:: IOValidationParams

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: file_path
      :type:  str
      :value: Ellipsis



   .. py:attribute:: format
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: max_size_bytes
      :type:  int
      :value: Ellipsis



   .. py:attribute:: fs
      :type:  FSInterface | None
      :value: Ellipsis



.. py:class:: IOValidationStep

   Bases: :py:obj:`CleaningStep`


