pysrc.data.satellite_data
=========================

.. py:module:: pysrc.data.satellite_data


Classes
-------

.. autoapisummary::

   pysrc.data.satellite_data.SatelliteDataSpec
   pysrc.data.satellite_data.SatelliteDataProvider


Module Contents
---------------

.. py:class:: SatelliteDataSpec

   .. py:attribute:: provider
      :type:  str
      :value: Ellipsis



   .. py:attribute:: region
      :type:  str
      :value: Ellipsis



   .. py:attribute:: date_range
      :type:  tuple[str, str]
      :value: Ellipsis



   .. py:attribute:: resolution
      :type:  int
      :value: Ellipsis



.. py:class:: SatelliteDataProvider

   Bases: :py:obj:`ABC`


   .. py:method:: fetch(spec)


