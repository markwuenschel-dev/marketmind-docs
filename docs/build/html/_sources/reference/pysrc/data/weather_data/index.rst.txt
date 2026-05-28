pysrc.data.weather_data
=======================

.. py:module:: pysrc.data.weather_data


Classes
-------

.. autoapisummary::

   pysrc.data.weather_data.WeatherDataSpec
   pysrc.data.weather_data.WeatherDataProvider


Module Contents
---------------

.. py:class:: WeatherDataSpec

   .. py:attribute:: station_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: variables
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: frequency
      :type:  str
      :value: Ellipsis



   .. py:attribute:: date_range
      :type:  tuple[str, str]
      :value: Ellipsis



.. py:class:: WeatherDataProvider

   Bases: :py:obj:`ABC`


   .. py:method:: fetch(spec)


