pysrc.ops.multi_tier_cache
==========================

.. py:module:: pysrc.ops.multi_tier_cache


Attributes
----------

.. autoapisummary::

   pysrc.ops.multi_tier_cache.redis
   pysrc.ops.multi_tier_cache.REDIS_AVAILABLE
   pysrc.ops.multi_tier_cache.T


Classes
-------

.. autoapisummary::

   pysrc.ops.multi_tier_cache.Call
   pysrc.ops.multi_tier_cache.Singleflight
   pysrc.ops.multi_tier_cache.L2Cache
   pysrc.ops.multi_tier_cache.PlasmaL2Cache
   pysrc.ops.multi_tier_cache.MemfdL2Cache
   pysrc.ops.multi_tier_cache.L3Cache
   pysrc.ops.multi_tier_cache.TierMetrics
   pysrc.ops.multi_tier_cache.MultiTierMetrics
   pysrc.ops.multi_tier_cache.InvalidationListener
   pysrc.ops.multi_tier_cache.MultiTierClient
   pysrc.ops.multi_tier_cache.PrometheusExporter


Functions
---------

.. autoapisummary::

   pysrc.ops.multi_tier_cache.version_to_int
   pysrc.ops.multi_tier_cache.multi_tier_cache


Module Contents
---------------

.. py:data:: redis
   :type:  Any

.. py:data:: REDIS_AVAILABLE
   :type:  Any

.. py:data:: T
   :type:  Any

.. py:function:: version_to_int(version_str)

.. py:class:: Call

   .. py:attribute:: future
      :type:  Union[Future, asyncio.Future]
      :value: Ellipsis



   .. py:attribute:: start_time
      :type:  float
      :value: Ellipsis



   .. py:attribute:: is_async
      :type:  bool
      :value: Ellipsis



.. py:class:: Singleflight

   .. py:method:: do(key, fn)


   .. py:method:: do_async(key, fn)
      :async:



.. py:class:: L2Cache

   .. py:method:: get(key)


   .. py:method:: set(key, value, ttl = ...)


   .. py:method:: invalidate(key)


.. py:class:: PlasmaL2Cache(plasma_path = ...)

   Bases: :py:obj:`L2Cache`


   .. py:method:: get(key)


   .. py:method:: set(key, value, ttl = ...)


   .. py:method:: invalidate(key)


.. py:class:: MemfdL2Cache(cache_dir = ...)

   Bases: :py:obj:`L2Cache`


   .. py:method:: get(key)


   .. py:method:: set(key, value, ttl = ...)


   .. py:method:: invalidate(key)


.. py:class:: L3Cache(redis_client = ..., key_prefix = ...)

   .. py:method:: get(key)


   .. py:method:: set(key, value, ttl = ...)


   .. py:method:: invalidate(key)


   .. py:method:: publish_invalidation(channel, key)


.. py:class:: TierMetrics

   .. py:attribute:: tier_name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: hits
      :type:  int
      :value: Ellipsis



   .. py:attribute:: misses
      :type:  int
      :value: Ellipsis



   .. py:attribute:: sets
      :type:  int
      :value: Ellipsis



   .. py:attribute:: promotions
      :type:  int
      :value: Ellipsis



   .. py:attribute:: latency_ns
      :type:  int
      :value: Ellipsis



   .. py:method:: hit_rate()


   .. py:method:: avg_latency_us()


.. py:class:: MultiTierMetrics

   .. py:method:: summary()


.. py:class:: InvalidationListener(redis_client, channel, callback)

   .. py:method:: start()


   .. py:method:: stop()


.. py:class:: MultiTierClient(l1_size = ..., l1_ttl = ..., l2_type = ..., l2_path = ..., redis_client = ..., l3_key_prefix = ..., l4_cache_dir = ..., enable_singleflight = ..., ttl_jitter = ..., check_l4_on_miss = ..., enable_invalidation_listener = ...)

   .. py:method:: get(key, version = ...)


   .. py:method:: set(key, value, ttl = ..., version = ..., write_through = ..., persist_to_l4 = ...)


   .. py:method:: compute_or_get(key, compute_fn, ttl = ..., version = ..., persist_to_l4 = ...)


   .. py:method:: compute_or_get_async(key, compute_fn, ttl = ..., version = ..., persist_to_l4 = ...)
      :async:



   .. py:method:: invalidate(key, broadcast = ...)


   .. py:method:: invalidate_pattern(prefix, broadcast = ...)


   .. py:method:: close()


.. py:function:: multi_tier_cache(ttl = ..., version = ..., persist_large_objects = ..., key_fn = ..., redis_client = ..., l2_type = ..., check_l4_on_miss = ...)

.. py:class:: PrometheusExporter(client)

   .. py:method:: export()


