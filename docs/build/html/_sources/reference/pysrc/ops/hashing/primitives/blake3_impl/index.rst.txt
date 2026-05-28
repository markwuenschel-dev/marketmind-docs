pysrc.ops.hashing.primitives.blake3_impl
========================================

.. py:module:: pysrc.ops.hashing.primitives.blake3_impl


Attributes
----------

.. autoapisummary::

   pysrc.ops.hashing.primitives.blake3_impl.BLAKE3


Classes
-------

.. autoapisummary::

   pysrc.ops.hashing.primitives.blake3_impl.Blake3Hasher
   pysrc.ops.hashing.primitives.blake3_impl.Blake3IncrementalHasher


Module Contents
---------------

.. py:class:: Blake3Hasher

   .. py:method:: hash_artifact_id(artifact_bytes)


   .. py:method:: hash_merkle_node(left_digest_hex, right_digest_hex, *, depth)


   .. py:method:: hash_audit_log_entry(entry_bytes, *, sequence_number)


   .. py:method:: hash_distributed_cache_key(key_material, *, namespace)


   .. py:method:: incremental_hasher()


.. py:class:: Blake3IncrementalHasher

   .. py:method:: update(chunk)


   .. py:method:: finalize_cas_id()


.. py:data:: BLAKE3
   :type:  Blake3Hasher
   :value: Ellipsis


