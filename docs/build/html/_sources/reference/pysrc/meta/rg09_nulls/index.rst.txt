pysrc.meta.rg09_nulls
=====================

.. py:module:: pysrc.meta.rg09_nulls


Attributes
----------

.. autoapisummary::

   pysrc.meta.rg09_nulls.AUTHORIZED_NULL_FAMILIES


Functions
---------

.. autoapisummary::

   pysrc.meta.rg09_nulls.make_null_rng
   pysrc.meta.rg09_nulls.shuffled_regime_null
   pysrc.meta.rg09_nulls.shuffled_label_null
   pysrc.meta.rg09_nulls.matched_exchangeable_window_null


Module Contents
---------------

.. py:data:: AUTHORIZED_NULL_FAMILIES
   :type:  Final[tuple[str, str, str]]
   :value: Ellipsis


.. py:function:: make_null_rng(namespace, family, fixture_sha256, *, draw_index = ...)

.. py:function:: shuffled_regime_null(episodes, *, namespace, fixture_sha256, draw_index = ...)

.. py:function:: shuffled_label_null(episodes, *, namespace, fixture_sha256, draw_index = ...)

.. py:function:: matched_exchangeable_window_null(episodes, *, namespace, fixture_sha256, draw_index = ...)

