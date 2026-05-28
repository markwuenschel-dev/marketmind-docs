pysrc.tuning.orchestration.retries
==================================

.. py:module:: pysrc.tuning.orchestration.retries


Attributes
----------

.. autoapisummary::

   pysrc.tuning.orchestration.retries.T


Exceptions
----------

.. autoapisummary::

   pysrc.tuning.orchestration.retries.MaxRetriesExceededError


Classes
-------

.. autoapisummary::

   pysrc.tuning.orchestration.retries.RetryPolicy


Functions
---------

.. autoapisummary::

   pysrc.tuning.orchestration.retries.with_retries


Module Contents
---------------

.. py:data:: T
   :type:  Any

.. py:exception:: MaxRetriesExceededError

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:class:: RetryPolicy(max_attempts = ..., initial_backoff = ..., max_backoff = ..., eta = ...)

.. py:function:: with_retries(fn, policy, retryable = ...)

