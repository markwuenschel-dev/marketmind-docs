pysrc.meta.reptile_trainer
==========================

.. py:module:: pysrc.meta.reptile_trainer


Attributes
----------

.. autoapisummary::

   pysrc.meta.reptile_trainer.LOG


Classes
-------

.. autoapisummary::

   pysrc.meta.reptile_trainer.TrainerRunResult
   pysrc.meta.reptile_trainer.GovernedCurriculumSuccess
   pysrc.meta.reptile_trainer.GovernedCurriculumFailure
   pysrc.meta.reptile_trainer.ReptileTrainer
   pysrc.meta.reptile_trainer.TaskPoolSufficiencyError


Functions
---------

.. autoapisummary::

   pysrc.meta.reptile_trainer.reptile_outer_update
   pysrc.meta.reptile_trainer.collect_inner_adapted_thetas_d0
   pysrc.meta.reptile_trainer.prepare_governed_curriculum_batch


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:function:: reptile_outer_update(theta_meta, adapted_stack, outer_lr)

.. py:function:: collect_inner_adapted_thetas_d0(*, theta_meta, tasks, config, seed)

.. py:class:: TrainerRunResult

   .. py:attribute:: theta_meta
      :type:  NDArray[np.float32]
      :value: Ellipsis



   .. py:attribute:: theta_day_prime
      :type:  NDArray[np.float32] | None
      :value: Ellipsis



   .. py:attribute:: meta_validity_report
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: theta_day_prime_promoted
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: inner_loop_gain
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: observability
      :type:  tuple[dict[str, Any], Ellipsis]
      :value: Ellipsis



.. py:class:: GovernedCurriculumSuccess

   .. py:attribute:: tasks
      :type:  tuple[MetaTask, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: counts
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:class:: GovernedCurriculumFailure

   .. py:attribute:: reasons
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: counts
      :type:  dict[str, Any] | None
      :value: Ellipsis



   .. py:attribute:: log_context
      :type:  dict[str, Any] | None
      :value: Ellipsis



.. py:function:: prepare_governed_curriculum_batch(sampler, config)

.. py:class:: ReptileTrainer(config, sampler, *, seed = ..., context_encoder = ...)

   .. py:method:: theta_day_prime_promoted()


   .. py:method:: apply_ewc_seam(theta, *, lambda_ewc)


   .. py:method:: run_batch(*, theta_meta, theta_day_prime_prior = ..., seed = ...)


.. py:class:: TaskPoolSufficiencyError

   Bases: :py:obj:`DataPreconditionError`


