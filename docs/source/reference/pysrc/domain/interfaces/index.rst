pysrc.domain.interfaces
=======================

.. py:module:: pysrc.domain.interfaces


Attributes
----------

.. autoapisummary::

   pysrc.domain.interfaces.PositionSchema
   pysrc.domain.interfaces.HistoricalSchema
   pysrc.domain.interfaces.T_co


Classes
-------

.. autoapisummary::

   pysrc.domain.interfaces.Order
   pysrc.domain.interfaces.Position
   pysrc.domain.interfaces.OrderExecutor
   pysrc.domain.interfaces.PositionService
   pysrc.domain.interfaces.MarketDataProvider
   pysrc.domain.interfaces.AsyncMarketDataProvider
   pysrc.domain.interfaces.EconomicDataProvider
   pysrc.domain.interfaces.ProviderFactory
   pysrc.domain.interfaces.RiskManager
   pysrc.domain.interfaces.PositionSizer
   pysrc.domain.interfaces.AbstractAPIDataManager


Module Contents
---------------

.. py:class:: Order

   .. py:attribute:: order_id
      :type:  int
      :value: Ellipsis



   .. py:attribute:: action
      :type:  str
      :value: Ellipsis



   .. py:attribute:: total_quantity
      :type:  float
      :value: Ellipsis



   .. py:attribute:: order_type
      :type:  str
      :value: Ellipsis



   .. py:attribute:: lmt_price
      :type:  Optional[float]
      :value: Ellipsis



   .. py:attribute:: aux_price
      :type:  Optional[float]
      :value: Ellipsis



   .. py:attribute:: tif
      :type:  str
      :value: Ellipsis



   .. py:attribute:: account
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: symbol
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: solicited
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: extra
      :type:  Dict[str, Any]
      :value: Ellipsis



   .. py:method:: market(symbol, qty)


.. py:class:: Position

   .. py:attribute:: account
      :type:  str
      :value: Ellipsis



   .. py:attribute:: symbol
      :type:  str
      :value: Ellipsis



   .. py:attribute:: position
      :type:  float
      :value: Ellipsis



   .. py:attribute:: avg_cost
      :type:  float
      :value: Ellipsis



   .. py:attribute:: model_code
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: extra
      :type:  Dict[str, Any]
      :value: Ellipsis



.. py:data:: PositionSchema
   :type:  SchemaDict
   :value: Ellipsis


.. py:data:: HistoricalSchema
   :type:  SchemaDict
   :value: Ellipsis


.. py:class:: OrderExecutor

   Bases: :py:obj:`Protocol`


   .. py:method:: submit(order)


   .. py:method:: submit_batch(orders)


   .. py:method:: cancel(order_id)


   .. py:method:: status(order_id)


.. py:class:: PositionService

   Bases: :py:obj:`Protocol`


   .. py:method:: get_positions()


   .. py:method:: get_positions_as_polars()


.. py:class:: MarketDataProvider

   Bases: :py:obj:`Protocol`


   .. py:method:: get_price(symbol)


   .. py:method:: get_prices(symbols)


   .. py:method:: get_historical(symbol, start, end, interval = ..., lazy = ...)


   .. py:method:: get_historical_batch(symbols, start, end, interval = ..., lazy = ...)


   .. py:method:: map_over(symbols, fn, combine = ...)


   .. py:method:: stream_realtime(symbol, interval = ...)
      :async:



.. py:class:: AsyncMarketDataProvider

   Bases: :py:obj:`MarketDataProvider`, :py:obj:`Protocol`


   .. py:method:: get_price_async(symbol)
      :async:



   .. py:method:: get_prices_async(symbols)
      :async:



.. py:class:: EconomicDataProvider

   Bases: :py:obj:`Protocol`


   .. py:method:: get_indicator(indicator, start, end)


.. py:data:: T_co
   :type:  Any

.. py:class:: ProviderFactory

   Bases: :py:obj:`ABC`, :py:obj:`Generic`\ [\ :py:obj:`T_co`\ ]


   .. py:method:: register(provider_type)


   .. py:method:: load_entry_points(group = ...)


   .. py:method:: create(provider_type, config, **kwargs)


   .. py:method:: build_provider(config, **kwargs)


.. py:class:: RiskManager

   .. py:method:: validate(order)


.. py:class:: PositionSizer

   .. py:method:: size(symbol, signal, price)


.. py:class:: AbstractAPIDataManager(config)

   .. py:attribute:: registry
      :type:  Dict[str, Type[Any]]
      :value: Ellipsis



   .. py:method:: register(source_type)


   .. py:method:: add_source(source_type, source)


   .. py:method:: load_data(query, source_name = ...)
      :async:



