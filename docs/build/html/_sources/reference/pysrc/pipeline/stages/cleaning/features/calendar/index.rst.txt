pysrc.pipeline.stages.cleaning.features.calendar
================================================

.. py:module:: pysrc.pipeline.stages.cleaning.features.calendar


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.features.calendar.TimeZoneParams
   pysrc.pipeline.stages.cleaning.features.calendar.TimeZoneNormalizerStep
   pysrc.pipeline.stages.cleaning.features.calendar.GlobalCalendarParams
   pysrc.pipeline.stages.cleaning.features.calendar.GlobalCalendarNormalizerStep


Module Contents
---------------

.. py:class:: TimeZoneParams

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: target_tz
      :type:  str
      :value: Ellipsis



   .. py:attribute:: timestamp_col
      :type:  str
      :value: Ellipsis



.. py:class:: TimeZoneNormalizerStep

   Bases: :py:obj:`CleaningStep`


.. py:class:: GlobalCalendarParams

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: countries
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: day_of_week
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: is_holiday
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: timestamp_col
      :type:  str
      :value: Ellipsis



.. py:class:: GlobalCalendarNormalizerStep

   Bases: :py:obj:`CleaningStep`


