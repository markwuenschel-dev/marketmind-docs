pysrc.tuning.core.planning.partition_plan
=========================================

.. py:module:: pysrc.tuning.core.planning.partition_plan


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.planning.partition_plan.TimePartition
   pysrc.tuning.core.planning.partition_plan.PartitionPlan


Module Contents
---------------

.. py:class:: TimePartition

   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: start
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: end
      :type:  datetime
      :value: Ellipsis



.. py:class:: PartitionPlan

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: symbols
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: time_partitions
      :type:  tuple[TimePartition, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: n_folds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_total_tasks
      :type:  int
      :value: Ellipsis



