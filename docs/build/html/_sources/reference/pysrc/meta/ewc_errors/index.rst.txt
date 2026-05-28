pysrc.meta.ewc_errors
=====================

.. py:module:: pysrc.meta.ewc_errors


Exceptions
----------

.. autoapisummary::

   pysrc.meta.ewc_errors.EWCValidationError
   pysrc.meta.ewc_errors.ArtifactImmutabilityError
   pysrc.meta.ewc_errors.InsufficientTaskPoolError
   pysrc.meta.ewc_errors.EWCDivergenceError


Module Contents
---------------

.. py:exception:: EWCValidationError(message, *, details = ...)

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:exception:: ArtifactImmutabilityError(message, *, path = ...)

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:exception:: InsufficientTaskPoolError(message, *, details = ...)

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:exception:: EWCDivergenceError(message, *, details = ...)

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


