pysrc.meta.reptile_k_sweep_errors
=================================

.. py:module:: pysrc.meta.reptile_k_sweep_errors


Exceptions
----------

.. autoapisummary::

   pysrc.meta.reptile_k_sweep_errors.KSweepValidationError
   pysrc.meta.reptile_k_sweep_errors.InnerLoopDivergenceError
   pysrc.meta.reptile_k_sweep_errors.ArtifactImmutabilityError


Module Contents
---------------

.. py:exception:: KSweepValidationError(message, *, details = ...)

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:exception:: InnerLoopDivergenceError(message, *, details = ...)

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:exception:: ArtifactImmutabilityError(message, *, path = ...)

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


