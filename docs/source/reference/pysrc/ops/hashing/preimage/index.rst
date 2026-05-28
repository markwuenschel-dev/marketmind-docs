pysrc.ops.hashing.preimage
==========================

.. py:module:: pysrc.ops.hashing.preimage


Attributes
----------

.. autoapisummary::

   pysrc.ops.hashing.preimage.PREIMAGE_NAMESPACE_ENCODING
   pysrc.ops.hashing.preimage.PREIMAGE_LENGTH_BYTES


Classes
-------

.. autoapisummary::

   pysrc.ops.hashing.preimage.PreimagePart
   pysrc.ops.hashing.preimage.CompositePreimage


Functions
---------

.. autoapisummary::

   pysrc.ops.hashing.preimage.assert_preimage_invariant_enabled
   pysrc.ops.hashing.preimage.make_part
   pysrc.ops.hashing.preimage.encode_namespace
   pysrc.ops.hashing.preimage.encode_length_prefix
   pysrc.ops.hashing.preimage.build_composite_preimage
   pysrc.ops.hashing.preimage.compose_for_purpose


Module Contents
---------------

.. py:data:: PREIMAGE_NAMESPACE_ENCODING
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: PREIMAGE_LENGTH_BYTES
   :type:  Final[int]
   :value: Ellipsis


.. py:class:: PreimagePart

   .. py:attribute:: payload
      :type:  bytes
      :value: Ellipsis



   .. py:attribute:: label
      :type:  str | None
      :value: Ellipsis



.. py:class:: CompositePreimage

   .. py:attribute:: purpose
      :type:  HashPurpose
      :value: Ellipsis



   .. py:attribute:: namespace
      :type:  str
      :value: Ellipsis



   .. py:attribute:: encoded
      :type:  bytes
      :value: Ellipsis



   .. py:attribute:: part_count
      :type:  int
      :value: Ellipsis



.. py:function:: assert_preimage_invariant_enabled()

.. py:function:: make_part(payload, *, label = ...)

.. py:function:: encode_namespace(namespace)

.. py:function:: encode_length_prefix(length)

.. py:function:: build_composite_preimage(namespace, *parts)

.. py:function:: compose_for_purpose(purpose, namespace, *parts)

