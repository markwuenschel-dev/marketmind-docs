pysrc.ops.hashing.envelope
==========================

.. py:module:: pysrc.ops.hashing.envelope


Classes
-------

.. autoapisummary::

   pysrc.ops.hashing.envelope.HashRef


Functions
---------

.. autoapisummary::

   pysrc.ops.hashing.envelope.make_cas_ref
   pysrc.ops.hashing.envelope.make_attest_ref
   pysrc.ops.hashing.envelope.make_merkle_ref
   pysrc.ops.hashing.envelope.make_cache_ref
   pysrc.ops.hashing.envelope.make_siphash_ref
   pysrc.ops.hashing.envelope.make_hmac_ref


Module Contents
---------------

.. py:class:: HashRef

   .. py:attribute:: domain
      :type:  str
      :value: Ellipsis



   .. py:attribute:: algo
      :type:  str
      :value: Ellipsis



   .. py:attribute:: digest
      :type:  str
      :value: Ellipsis



   .. py:attribute:: purpose
      :type:  str
      :value: Ellipsis



   .. py:attribute:: algo_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: canonicalizer_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: canonicalizer_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: key_id
      :type:  Optional[str]
      :value: Ellipsis



   .. py:method:: to_id_string()


   .. py:method:: hex_digest()


   .. py:method:: equality_check(other)


   .. py:method:: to_dict()


   .. py:method:: to_json(*, indent = ...)


   .. py:method:: from_dict(data)


   .. py:method:: from_json(s)


   .. py:method:: parse(value)


.. py:function:: make_cas_ref(digest_hex)

.. py:function:: make_attest_ref(digest_hex)

.. py:function:: make_merkle_ref(digest_hex)

.. py:function:: make_cache_ref(digest_hex, *, purpose, namespace = ...)

.. py:function:: make_siphash_ref(digest_hex, *, purpose, key_id)

.. py:function:: make_hmac_ref(digest_hex, *, key_id)

