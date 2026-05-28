pysrc.tuning.core.validation_ir.determinism_checks
==================================================

.. py:module:: pysrc.tuning.core.validation_ir.determinism_checks


Attributes
----------

.. autoapisummary::

   pysrc.tuning.core.validation_ir.determinism_checks.VALID_TIERS


Exceptions
----------

.. autoapisummary::

   pysrc.tuning.core.validation_ir.determinism_checks.DeterminismViolationError


Functions
---------

.. autoapisummary::

   pysrc.tuning.core.validation_ir.determinism_checks.validate_tier
   pysrc.tuning.core.validation_ir.determinism_checks.assert_tier_not_downgraded


Module Contents
---------------

.. py:data:: VALID_TIERS
   :type:  frozenset[str]
   :value: Ellipsis


.. py:exception:: DeterminismViolationError

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:function:: validate_tier(meta)

.. py:function:: assert_tier_not_downgraded(current, proposed)

