pysrc.pipeline.stages.market_data.sources.market_data
=====================================================

.. py:module:: pysrc.pipeline.stages.market_data.sources.market_data


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.market_data.T
   pysrc.pipeline.stages.market_data.sources.market_data.REGISTRY


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.market_data.AsyncLRU
   pysrc.pipeline.stages.market_data.sources.market_data.SourceRegistry
   pysrc.pipeline.stages.market_data.sources.market_data.CompositeSource
   pysrc.pipeline.stages.market_data.sources.market_data.FailoverSource
   pysrc.pipeline.stages.market_data.sources.market_data.MarketDataConfig
   pysrc.pipeline.stages.market_data.sources.market_data.MarketDataManager


Functions
---------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.market_data.register_source
   pysrc.pipeline.stages.market_data.sources.market_data.build_client_from_config


Module Contents
---------------

.. py:data:: T
   :type:  Any

.. py:class:: AsyncLRU(maxsize = ..., ttl = ...)

   .. py:method:: get_or_set(key, coro_factory)
      :async:



.. py:class:: SourceRegistry

   .. py:method:: register(name, cls)


   .. py:method:: names()


   .. py:method:: get(name)


   .. py:method:: create(name, cfg)


   .. py:method:: ensure(name, cfg)


.. py:data:: REGISTRY
   :type:  Any

.. py:function:: register_source(name)

.. py:class:: CompositeSource(cfg)

   Bases: :py:obj:`DataSource`


   .. py:method:: get_historical(symbol, start, end, *, eager = ...)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = ...)
      :async:



.. py:class:: FailoverSource(cfg)

   Bases: :py:obj:`DataSource`


   .. py:method:: get_historical(symbol, start, end, *, eager = ...)
      :async:



   .. py:method:: get_realtime(symbol, *, interval = ...)
      :async:



.. py:class:: MarketDataConfig

   .. py:attribute:: default_source
      :type:  str
      :value: Ellipsis



   .. py:attribute:: cache_maxsize
      :type:  int
      :value: Ellipsis



   .. py:attribute:: cache_ttl
      :type:  float
      :value: Ellipsis



   .. py:attribute:: retry_attempts
      :type:  int
      :value: Ellipsis



   .. py:attribute:: retry_base_delay
      :type:  float
      :value: Ellipsis



   .. py:attribute:: fanout_concurrency
      :type:  int
      :value: Ellipsis



   .. py:attribute:: source_configs
      :type:  Optional[Mapping[str, Mapping[str, Any]]]
      :value: Ellipsis



.. py:class:: MarketDataManager(*, config = ...)

   .. py:method:: register_instance(name, src)


   .. py:method:: get_historical(symbol, start, end, *, source_name = ..., eager = ...)
      :async:



   .. py:method:: get_historical_cached(symbol, start, end, *, source_name = ..., eager = ...)
      :async:



   .. py:method:: get_historical_many(symbols, start, end, *, source_name = ..., eager = ..., use_cache = ...)
      :async:



   .. py:method:: get_historical_auto(symbol, start, end, *, candidates = ..., eager = ...)
      :async:



   .. py:method:: get_realtime(symbol, *, source_name = ..., interval = ...)
      :async:



   .. py:method:: close()


.. py:function:: build_client_from_config(cfg)

