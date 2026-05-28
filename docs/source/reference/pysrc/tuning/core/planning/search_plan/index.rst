pysrc.tuning.core.planning.search_plan
======================================

.. py:module:: pysrc.tuning.core.planning.search_plan


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.planning.search_plan.SearchStep
   pysrc.tuning.core.planning.search_plan.SearchPlan


Module Contents
---------------

.. py:class:: SearchStep

   .. py:attribute:: step_index
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_candidates
      :type:  int
      :value: Ellipsis



   .. py:attribute:: algorithm_snapshot
      :type:  str
      :value: Ellipsis



   .. py:attribute:: partition_id
      :type:  str
      :value: Ellipsis



.. py:class:: SearchPlan

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: space_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: steps
      :type:  tuple[SearchStep, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: budget
      :type:  ExecutionBudget
      :value: Ellipsis



   .. py:attribute:: meta
      :type:  PlanMetadata
      :value: Ellipsis



