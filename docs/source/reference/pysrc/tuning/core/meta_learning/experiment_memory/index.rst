pysrc.tuning.core.meta_learning.experiment_memory
=================================================

.. py:module:: pysrc.tuning.core.meta_learning.experiment_memory


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.meta_learning.experiment_memory.ExperimentRecord
   pysrc.tuning.core.meta_learning.experiment_memory.ExperimentMemory


Module Contents
---------------

.. py:class:: ExperimentRecord

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: space_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: best_candidate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: best_score
      :type:  float
      :value: Ellipsis



   .. py:attribute:: n_trials
      :type:  int
      :value: Ellipsis



   .. py:attribute:: completed_at
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: tags
      :type:  dict[str, str]
      :value: Ellipsis



.. py:class:: ExperimentMemory

   .. py:attribute:: records
      :type:  tuple[ExperimentRecord, Ellipsis]
      :value: Ellipsis



   .. py:method:: by_space(space_hash)


   .. py:method:: top_k(k)


