pysrc.meta.reptile_proxy_alignment_errors
=========================================

.. py:module:: pysrc.meta.reptile_proxy_alignment_errors


Exceptions
----------

.. autoapisummary::

   pysrc.meta.reptile_proxy_alignment_errors.ProxyAlignmentValidationError
   pysrc.meta.reptile_proxy_alignment_errors.ArtifactImmutabilityError
   pysrc.meta.reptile_proxy_alignment_errors.InsufficientTaskPoolError
   pysrc.meta.reptile_proxy_alignment_errors.ProxyArmDivergenceError


Module Contents
---------------

.. py:exception:: ProxyAlignmentValidationError(message, *, details = ...)

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:exception:: ArtifactImmutabilityError(message, *, path = ...)

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:exception:: InsufficientTaskPoolError(message, *, details = ...)

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:exception:: ProxyArmDivergenceError(message, *, details = ...)

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


