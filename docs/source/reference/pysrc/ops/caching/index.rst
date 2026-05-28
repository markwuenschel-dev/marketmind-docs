pysrc.ops.caching
=================

.. py:module:: pysrc.ops.caching


Attributes
----------

.. autoapisummary::

   pysrc.ops.caching.T


Classes
-------

.. autoapisummary::

   pysrc.ops.caching.HashAlgorithm
   pysrc.ops.caching.CompressionLevel
   pysrc.ops.caching.CompressionStrategy
   pysrc.ops.caching.CacheEntry
   pysrc.ops.caching.CacheMetrics
   pysrc.ops.caching.AdaptiveTTLManager
   pysrc.ops.caching.EnhancedCacheManager
   pysrc.ops.caching.DistributedCacheCoordinator
   pysrc.ops.caching.PersistentCache


Functions
---------

.. autoapisummary::

   pysrc.ops.caching.hash_bytes
   pysrc.ops.caching.hash_config
   pysrc.ops.caching.hash_dataframe_deterministic
   pysrc.ops.caching.versioned_key
   pysrc.ops.caching.enhanced_cache


Module Contents
---------------

.. py:data:: T
   :type:  Any

.. py:class:: HashAlgorithm

   Bases: :py:obj:`Enum`


   .. py:attribute:: XXHASH
      :type:  Any


   .. py:attribute:: BLAKE3
      :type:  Any


   .. py:attribute:: SIPHASH
      :type:  Any


   .. py:attribute:: SHA256
      :type:  Any


.. py:function:: hash_bytes(data, algo = ...)

.. py:function:: hash_config(cfg_obj, algo = ...)

.. py:function:: hash_dataframe_deterministic(df, cols = ..., algo = ...)

.. py:function:: versioned_key(*parts, version = ...)

.. py:class:: CompressionLevel

   Bases: :py:obj:`Enum`


   .. py:attribute:: NONE
      :type:  Any


   .. py:attribute:: FAST
      :type:  Any


   .. py:attribute:: HIGH
      :type:  Any


.. py:class:: CompressionStrategy

   .. py:attribute:: small_threshold
      :type:  int
      :value: Ellipsis



   .. py:attribute:: fast_threshold
      :type:  int
      :value: Ellipsis



   .. py:method:: compress(data, level = ...)


   .. py:method:: decompress(data, level)


.. py:class:: CacheEntry

   .. py:attribute:: value
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: expiry
      :type:  float
      :value: Ellipsis



   .. py:attribute:: version
      :type:  int
      :value: Ellipsis



   .. py:attribute:: access_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: last_access
      :type:  float
      :value: Ellipsis



   .. py:attribute:: compression
      :type:  CompressionLevel
      :value: Ellipsis



.. py:class:: CacheMetrics

   .. py:attribute:: hits
      :type:  int
      :value: Ellipsis



   .. py:attribute:: misses
      :type:  int
      :value: Ellipsis



   .. py:attribute:: evictions
      :type:  int
      :value: Ellipsis



   .. py:attribute:: sets
      :type:  int
      :value: Ellipsis



   .. py:attribute:: total_latency_ns
      :type:  int
      :value: Ellipsis



   .. py:method:: hit_rate()


   .. py:method:: avg_latency_us()


.. py:class:: AdaptiveTTLManager(base_ttl = ...)

   .. py:method:: get_ttl(key, volatility = ...)


   .. py:method:: update_volatility(volatility)


.. py:class:: EnhancedCacheManager(max_size = ..., ttl = ..., eviction_policy = ..., enable_compression = ..., enable_metrics = ...)

   .. py:method:: get(key, version = ...)


   .. py:method:: set(key, value, ttl = ..., version = ..., volatility = ...)


   .. py:method:: invalidate(key)


   .. py:method:: invalidate_pattern(prefix)


   .. py:method:: get_async(key, version = ...)
      :async:



   .. py:method:: set_async(key, value, **kwargs)
      :async:



.. py:class:: DistributedCacheCoordinator(redis_client = ...)

   .. py:attribute:: CAS_SCRIPT
      :type:  Any


   .. py:method:: cas_update(key, value, timestamp)
      :async:



   .. py:method:: invalidate_broadcast(channel, key)
      :async:



.. py:function:: enhanced_cache(max_size = ..., ttl = ..., key_fn = ..., version = ..., enable_metrics = ...)

.. py:class:: PersistentCache(cache_dir = ..., enable_compression = ...)

   .. py:method:: exists(key)


   .. py:method:: save_df(key, df, version = ...)


   .. py:method:: load_df(key, expected_version = ...)


   .. py:method:: invalidate(key)


