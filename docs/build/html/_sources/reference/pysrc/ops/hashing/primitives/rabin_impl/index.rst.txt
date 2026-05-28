pysrc.ops.hashing.primitives.rabin_impl
=======================================

.. py:module:: pysrc.ops.hashing.primitives.rabin_impl


Attributes
----------

.. autoapisummary::

   pysrc.ops.hashing.primitives.rabin_impl.RABIN_POLY
   pysrc.ops.hashing.primitives.rabin_impl.RABIN_POLY_DEGREE


Classes
-------

.. autoapisummary::

   pysrc.ops.hashing.primitives.rabin_impl.RabinRollingHasher


Module Contents
---------------

.. py:data:: RABIN_POLY
   :type:  int
   :value: Ellipsis


.. py:data:: RABIN_POLY_DEGREE
   :type:  int
   :value: Ellipsis


.. py:class:: RabinRollingHasher(window_size, poly = ...)

   .. py:method:: reset()


   .. py:method:: roll_byte(incoming)


   .. py:method:: fingerprint(data)


   .. py:method:: find_boundaries(data, mask)


   .. py:method:: make_hashref(fingerprint)


