pysrc.infra.brokers.ibkr.ib_data_collection
===========================================

.. py:module:: pysrc.infra.brokers.ibkr.ib_data_collection


Attributes
----------

.. autoapisummary::

   pysrc.infra.brokers.ibkr.ib_data_collection.pd


Exceptions
----------

.. autoapisummary::

   pysrc.infra.brokers.ibkr.ib_data_collection.NoDataError


Functions
---------

.. autoapisummary::

   pysrc.infra.brokers.ibkr.ib_data_collection.create_mock_bars
   pysrc.infra.brokers.ibkr.ib_data_collection.ib_connection
   pysrc.infra.brokers.ibkr.ib_data_collection.fetch_historical_data


Module Contents
---------------

.. py:data:: pd
   :type:  Any

.. py:function:: create_mock_bars(n, start_date = ...)

.. py:exception:: NoDataError

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:function:: ib_connection(*args, **kwargs)

.. py:function:: fetch_historical_data(symbol, end_datetime, *, duration = ..., bar_size = ..., what_to_show = ..., use_cache = ..., ib_client = ...)

