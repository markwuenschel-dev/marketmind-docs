pysrc.tuning.core.validation_ir.pit_checks
==========================================

.. py:module:: pysrc.tuning.core.validation_ir.pit_checks


Exceptions
----------

.. autoapisummary::

   pysrc.tuning.core.validation_ir.pit_checks.PITViolationError


Functions
---------

.. autoapisummary::

   pysrc.tuning.core.validation_ir.pit_checks.validate_fold_pit
   pysrc.tuning.core.validation_ir.pit_checks.validate_no_leakage
   pysrc.tuning.core.validation_ir.pit_checks.validate_task_pit


Module Contents
---------------

.. py:exception:: PITViolationError

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:function:: validate_fold_pit(fold, as_of)

.. py:function:: validate_no_leakage(fold)

.. py:function:: validate_task_pit(task_ir, as_of)

