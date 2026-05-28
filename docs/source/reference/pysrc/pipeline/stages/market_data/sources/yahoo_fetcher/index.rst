pysrc.pipeline.stages.market_data.sources.yahoo_fetcher
=======================================================

.. py:module:: pysrc.pipeline.stages.market_data.sources.yahoo_fetcher


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.yahoo_fetcher.YahooFinanceSource


Module Contents
---------------

.. py:class:: YahooFinanceSource(config = ..., *, fetch_clock = ...)

   Bases: :py:obj:`DataSource`


   .. py:method:: get_historical(symbol, start, end, *, eager = ...)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = ...)
      :async:



