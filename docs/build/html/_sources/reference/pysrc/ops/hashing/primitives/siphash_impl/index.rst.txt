pysrc.ops.hashing.primitives.siphash_impl
=========================================

.. py:module:: pysrc.ops.hashing.primitives.siphash_impl


Classes
-------

.. autoapisummary::

   pysrc.ops.hashing.primitives.siphash_impl.SipHashKey
   pysrc.ops.hashing.primitives.siphash_impl.SipHash24Hasher


Module Contents
---------------

.. py:class:: SipHashKey

   .. py:attribute:: key_bytes
      :type:  bytes
      :value: Ellipsis



   .. py:attribute:: key_id
      :type:  str
      :value: Ellipsis



   .. py:method:: k0()


   .. py:method:: k1()


   .. py:method:: generate()


.. py:class:: SipHash24Hasher(key)

   .. py:method:: key_id()


   .. py:method:: hash_map_key(key_bytes, *, namespace, purpose = ...)


   .. py:method:: hash_composite_key(*fields, namespace, purpose = ...)


