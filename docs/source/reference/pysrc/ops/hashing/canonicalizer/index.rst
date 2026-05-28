pysrc.ops.hashing.canonicalizer
===============================

.. py:module:: pysrc.ops.hashing.canonicalizer


Attributes
----------

.. autoapisummary::

   pysrc.ops.hashing.canonicalizer.FLOAT64_QUIET_NAN_BE
   pysrc.ops.hashing.canonicalizer.FLOAT32_QUIET_NAN_BE
   pysrc.ops.hashing.canonicalizer.FLOAT64_POS_ZERO_BE
   pysrc.ops.hashing.canonicalizer.FLOAT32_POS_ZERO_BE
   pysrc.ops.hashing.canonicalizer.CANON


Classes
-------

.. autoapisummary::

   pysrc.ops.hashing.canonicalizer.Canonicalizer


Functions
---------

.. autoapisummary::

   pysrc.ops.hashing.canonicalizer.canonicalize_json_bytes


Module Contents
---------------

.. py:data:: FLOAT64_QUIET_NAN_BE
   :type:  bytes
   :value: Ellipsis


.. py:data:: FLOAT32_QUIET_NAN_BE
   :type:  bytes
   :value: Ellipsis


.. py:data:: FLOAT64_POS_ZERO_BE
   :type:  bytes
   :value: Ellipsis


.. py:data:: FLOAT32_POS_ZERO_BE
   :type:  bytes
   :value: Ellipsis


.. py:class:: Canonicalizer

   .. py:method:: encode_string(s)


   .. py:method:: encode_u64be(n)


   .. py:method:: encode_u32be(n)


   .. py:method:: encode_i16be(n)


   .. py:method:: encode_i64be(n)


   .. py:method:: normalize_float64(v, *, tier = ...)


   .. py:method:: normalize_float64_array(arr, *, tier = ...)


   .. py:method:: canonicalize_json(obj)


   .. py:method:: canonicalize_dataframe(df, *, sort_key, namespace = ..., tier = ...)


   .. py:method:: build_composite_preimage(namespace, *fields)


.. py:function:: canonicalize_json_bytes(obj)

.. py:data:: CANON
   :type:  Canonicalizer
   :value: Ellipsis


