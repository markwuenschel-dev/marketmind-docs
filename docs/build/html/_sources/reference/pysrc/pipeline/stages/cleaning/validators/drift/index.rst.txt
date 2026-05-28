pysrc.pipeline.stages.cleaning.validators.drift
===============================================

.. py:module:: pysrc.pipeline.stages.cleaning.validators.drift


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.validators.drift.BaseDriftTest
   pysrc.pipeline.stages.cleaning.validators.drift.KSTest
   pysrc.pipeline.stages.cleaning.validators.drift.DriftDetectionParams
   pysrc.pipeline.stages.cleaning.validators.drift.DriftDetectionStep


Module Contents
---------------

.. py:class:: BaseDriftTest

   .. py:method:: compute(current, reference)


.. py:class:: KSTest

   Bases: :py:obj:`BaseDriftTest`


   .. py:method:: compute(current, reference)


.. py:class:: DriftDetectionParams

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: columns
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: strict
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: reference_frame
      :type:  Any | None
      :value: Ellipsis



.. py:class:: DriftDetectionStep

   Bases: :py:obj:`CleaningStep`


