pysrc.strategies.momentum.exceptions
====================================

.. py:module:: pysrc.strategies.momentum.exceptions


Exceptions
----------

.. autoapisummary::

   pysrc.strategies.momentum.exceptions.CostGateRejection
   pysrc.strategies.momentum.exceptions.SerializationError
   pysrc.strategies.momentum.exceptions.MissingExecutionAssumptionsError


Classes
-------

.. autoapisummary::

   pysrc.strategies.momentum.exceptions.FeatureFlagError
   pysrc.strategies.momentum.exceptions.ConvergenceError


Functions
---------

.. autoapisummary::

   pysrc.strategies.momentum.exceptions.exception_metadata


Module Contents
---------------

.. py:class:: FeatureFlagError

   Bases: :py:obj:`PipelineError`


.. py:class:: ConvergenceError(message, *, n_iterations = ..., asset_id = ...)

   Bases: :py:obj:`MaterializationError`


.. py:exception:: CostGateRejection(message, *, variant, run_id, reason_code)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: SerializationError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: MissingExecutionAssumptionsError

   Bases: :py:obj:`FileNotFoundError`


   File not found.


.. py:function:: exception_metadata(exc)

