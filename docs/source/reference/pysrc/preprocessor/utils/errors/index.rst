pysrc.preprocessor.utils.errors
===============================

.. py:module:: pysrc.preprocessor.utils.errors


Exceptions
----------

.. autoapisummary::

   pysrc.preprocessor.utils.errors.OOMRetry
   pysrc.preprocessor.utils.errors.UnsupportedAST
   pysrc.preprocessor.utils.errors.SchemaMismatch


Module Contents
---------------

.. py:exception:: OOMRetry(message = ..., retry_hint = ...)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: UnsupportedAST

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: SchemaMismatch(message, details = ...)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


