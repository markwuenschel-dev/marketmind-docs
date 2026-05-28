pysrc.infra.brokers.ibkr.historical
===================================

.. py:module:: pysrc.infra.brokers.ibkr.historical


Attributes
----------

.. autoapisummary::

   pysrc.infra.brokers.ibkr.historical.logger


Classes
-------

.. autoapisummary::

   pysrc.infra.brokers.ibkr.historical.NoDataError


Functions
---------

.. autoapisummary::

   pysrc.infra.brokers.ibkr.historical.create_mock_bars
   pysrc.infra.brokers.ibkr.historical.fetch_historical_data
   pysrc.infra.brokers.ibkr.historical.fetch_multiple_historical_data


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:class:: NoDataError(symbol)

   Bases: :py:obj:`DataFetchError`


.. py:function:: create_mock_bars(n, start_date = ...)

.. py:function:: fetch_historical_data(symbol, end_date = ..., duration = ..., bar_size = ..., ibkr_client = ..., use_cache = ..., what_to_show = ..., use_rth = ..., format_date = ...)

.. py:function:: fetch_multiple_historical_data(symbols, end_date = ..., duration = ..., bar_size = ..., use_cache = ..., what_to_show = ..., use_rth = ..., format_date = ...)
   :async:


