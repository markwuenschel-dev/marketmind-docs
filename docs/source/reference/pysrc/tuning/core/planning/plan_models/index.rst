pysrc.tuning.core.planning.plan_models
======================================

.. py:module:: pysrc.tuning.core.planning.plan_models


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.planning.plan_models.ExecutionBudget
   pysrc.tuning.core.planning.plan_models.PlanMetadata


Module Contents
---------------

.. py:class:: ExecutionBudget

   .. py:attribute:: max_trials
      :type:  int
      :value: Ellipsis



   .. py:attribute:: timeout_seconds
      :type:  int | None
      :value: Ellipsis



   .. py:attribute:: max_parallel
      :type:  int
      :value: Ellipsis



   .. py:attribute:: priority
      :type:  Literal['throughput', 'latency', 'cost']
      :value: Ellipsis



.. py:class:: PlanMetadata

   .. py:attribute:: plan_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: spec_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: created_at_ns
      :type:  int
      :value: Ellipsis



   .. py:attribute:: determinism_tier
      :type:  str
      :value: Ellipsis



