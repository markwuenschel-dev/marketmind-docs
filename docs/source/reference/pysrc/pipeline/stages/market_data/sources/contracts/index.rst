pysrc.pipeline.stages.market_data.sources.contracts
===================================================

.. py:module:: pysrc.pipeline.stages.market_data.sources.contracts


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.contracts.DataSource


Module Contents
---------------

.. py:class:: DataSource(config)

   Bases: :py:obj:`ABC`


   .. py:method:: get_historical(symbol, start, end, *, eager = ...)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = ...)
      :async:



   .. py:method:: close()
      :async:



