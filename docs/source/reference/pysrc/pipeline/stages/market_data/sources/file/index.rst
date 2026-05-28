pysrc.pipeline.stages.market_data.sources.file
==============================================

.. py:module:: pysrc.pipeline.stages.market_data.sources.file


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.file.FileSource


Module Contents
---------------

.. py:class:: FileSource(config)

   Bases: :py:obj:`DataSource`


   .. py:method:: get_historical(symbol, start, end, *, eager = ...)
      :async:



   .. py:method:: get_historical_sync(symbol, start, end, *, eager = ...)


   .. py:method:: get_realtime(symbol, *, interval = ...)
      :async:



