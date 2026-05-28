pysrc.meta.curriculum
=====================

.. py:module:: pysrc.meta.curriculum


Attributes
----------

.. autoapisummary::

   pysrc.meta.curriculum.LOG
   pysrc.meta.curriculum.CurriculumPhase
   pysrc.meta.curriculum.PriorityResolver


Classes
-------

.. autoapisummary::

   pysrc.meta.curriculum.CurriculumSufficiencyError
   pysrc.meta.curriculum.HoldoutExclusionSurface
   pysrc.meta.curriculum.CurriculumSamplerConfig
   pysrc.meta.curriculum.CurriculumBatch
   pysrc.meta.curriculum.CurriculumSampler


Functions
---------

.. autoapisummary::

   pysrc.meta.curriculum.governed_v2_task_pool_bucket_minimums


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:data:: CurriculumPhase
   :type:  Any

.. py:data:: PriorityResolver
   :type:  Any

.. py:class:: CurriculumSufficiencyError

   Bases: :py:obj:`DataPreconditionError`


.. py:function:: governed_v2_task_pool_bucket_minimums()

.. py:class:: HoldoutExclusionSurface

   .. py:attribute:: task_ids
      :type:  frozenset[str]
      :value: Ellipsis



   .. py:method:: allows(task)


.. py:class:: CurriculumSamplerConfig

   .. py:attribute:: batch_size
      :type:  int
      :value: Ellipsis



   .. py:attribute:: crisis_floor_fraction
      :type:  float
      :value: Ellipsis



   .. py:attribute:: bucket_minimums
      :type:  Mapping[str, int]
      :value: Ellipsis



   .. py:attribute:: priority_alpha
      :type:  float
      :value: Ellipsis



   .. py:attribute:: importance_beta
      :type:  float
      :value: Ellipsis



   .. py:attribute:: seed
      :type:  int
      :value: Ellipsis



.. py:class:: CurriculumBatch

   .. py:attribute:: tasks
      :type:  tuple[MetaTask, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: phase
      :type:  CurriculumPhase
      :value: Ellipsis



   .. py:attribute:: bucket_counts
      :type:  Mapping[str, int]
      :value: Ellipsis



   .. py:attribute:: priority_alpha
      :type:  float
      :value: Ellipsis



   .. py:attribute:: importance_beta
      :type:  float
      :value: Ellipsis



   .. py:attribute:: importance_weights
      :type:  tuple[float, Ellipsis]
      :value: Ellipsis



.. py:class:: CurriculumSampler(tasks, *, config, holdouts = ...)

   .. py:method:: trainable_tasks()


   .. py:method:: bucket_governance_minimums()


   .. py:method:: sample_bootstrap()


   .. py:method:: sample_per_like(*, priority_resolver)


