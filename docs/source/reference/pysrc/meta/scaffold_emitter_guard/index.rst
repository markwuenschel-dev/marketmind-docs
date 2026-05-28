pysrc.meta.scaffold_emitter_guard
=================================

.. py:module:: pysrc.meta.scaffold_emitter_guard


Attributes
----------

.. autoapisummary::

   pysrc.meta.scaffold_emitter_guard.GOVERNED_LANE_ENV


Exceptions
----------

.. autoapisummary::

   pysrc.meta.scaffold_emitter_guard.ScaffoldEmitterForbiddenError


Functions
---------

.. autoapisummary::

   pysrc.meta.scaffold_emitter_guard.assert_scaffold_emitter_allowed
   pysrc.meta.scaffold_emitter_guard.governed_lane_context


Module Contents
---------------

.. py:data:: GOVERNED_LANE_ENV
   :type:  Final[str]
   :value: Ellipsis


.. py:exception:: ScaffoldEmitterForbiddenError

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:function:: assert_scaffold_emitter_allowed(*, emitter_name)

.. py:function:: governed_lane_context()

