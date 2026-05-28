pysrc.tuning.orchestration.budget_manager
=========================================

.. py:module:: pysrc.tuning.orchestration.budget_manager


Exceptions
----------

.. autoapisummary::

   pysrc.tuning.orchestration.budget_manager.BudgetExhaustedError


Classes
-------

.. autoapisummary::

   pysrc.tuning.orchestration.budget_manager.BudgetManager


Module Contents
---------------

.. py:exception:: BudgetExhaustedError

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:class:: BudgetManager(max_trials, timeout_seconds)

   .. py:method:: consume(n = ...)


   .. py:method:: remaining()


