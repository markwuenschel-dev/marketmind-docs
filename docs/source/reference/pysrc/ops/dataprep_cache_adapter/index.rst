pysrc.ops.dataprep_cache_adapter
================================

.. py:module:: pysrc.ops.dataprep_cache_adapter


Classes
-------

.. autoapisummary::

   pysrc.ops.dataprep_cache_adapter.MultiTierCacheAdapter


Module Contents
---------------

.. py:class:: MultiTierCacheAdapter(client)

   .. py:method:: exists(key)


   .. py:method:: save_npz(key, data)


   .. py:method:: load_npz(key)


   .. py:method:: save_json(key, data)


   .. py:method:: load_json(key)


   .. py:method:: save_df(key, df, **kwargs)


   .. py:method:: load_df(key, **kwargs)


