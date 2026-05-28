pysrc.pipeline.stages.market_data.sources.fred
==============================================

.. py:module:: pysrc.pipeline.stages.market_data.sources.fred


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.fred.FREDVintageSeam
   pysrc.pipeline.stages.market_data.sources.fred.FREDApproximationStub
   pysrc.pipeline.stages.market_data.sources.fred.FREDSource


Module Contents
---------------

.. py:class:: FREDVintageSeam

   Bases: :py:obj:`Protocol`


   .. py:method:: apply(frame, *, retrieval_time)


.. py:class:: FREDApproximationStub

   .. py:method:: apply(frame, *, retrieval_time)


.. py:class:: FREDSource(config, *, fred_client = ..., vintage_seam = ..., retrieval_clock = ...)

   Bases: :py:obj:`DataSource`


   .. py:method:: get_historical(symbol, start, end, *, eager = ...)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = ...)
      :async:



