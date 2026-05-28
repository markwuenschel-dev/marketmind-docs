pysrc.pipeline.stages.market_data.sources.alternative
=====================================================

.. py:module:: pysrc.pipeline.stages.market_data.sources.alternative


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.alternative.AlternativeDataSource
   pysrc.pipeline.stages.market_data.sources.alternative.SatelliteDataSource
   pysrc.pipeline.stages.market_data.sources.alternative.WeatherDataSource
   pysrc.pipeline.stages.market_data.sources.alternative.SocialSentimentDataSource


Module Contents
---------------

.. py:class:: AlternativeDataSource

   Bases: :py:obj:`DataSource`


   .. py:method:: get_historical(symbol, start, end, *, eager = ...)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = ...)
      :async:



.. py:class:: SatelliteDataSource

   Bases: :py:obj:`AlternativeDataSource`, :py:obj:`APIDataSource`


   .. py:method:: get_historical(symbol, start, end, *, eager = ...)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = ...)
      :async:



.. py:class:: WeatherDataSource

   Bases: :py:obj:`AlternativeDataSource`, :py:obj:`APIDataSource`


   .. py:method:: get_historical(symbol, start, end, *, eager = ...)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = ...)
      :async:



.. py:class:: SocialSentimentDataSource

   Bases: :py:obj:`AlternativeDataSource`, :py:obj:`APIDataSource`


   .. py:method:: get_historical(symbol, start, end, *, eager = ...)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = ...)
      :async:



