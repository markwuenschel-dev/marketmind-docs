pysrc.pipeline.stages.market_data.sources.influxdb
==================================================

.. py:module:: pysrc.pipeline.stages.market_data.sources.influxdb


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.influxdb.InfluxDBSource


Module Contents
---------------

.. py:class:: InfluxDBSource(config)

   Bases: :py:obj:`DataSource`


   .. py:method:: get_historical(symbol, start, end, *, eager = ...)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = ...)
      :async:



