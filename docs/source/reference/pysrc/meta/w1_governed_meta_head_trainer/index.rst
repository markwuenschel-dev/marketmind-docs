pysrc.meta.w1_governed_meta_head_trainer
========================================

.. py:module:: pysrc.meta.w1_governed_meta_head_trainer


Attributes
----------

.. autoapisummary::

   pysrc.meta.w1_governed_meta_head_trainer.TRAINED_BY_W1_GOVERNED_META_HEAD_V1


Classes
-------

.. autoapisummary::

   pysrc.meta.w1_governed_meta_head_trainer.W1GovernedMetaHeadTrainConfig
   pysrc.meta.w1_governed_meta_head_trainer.W1GovernedMetaHeadTrainSuccess
   pysrc.meta.w1_governed_meta_head_trainer.W1GovernedMetaHeadTrainFailure


Functions
---------

.. autoapisummary::

   pysrc.meta.w1_governed_meta_head_trainer.derive_w1_governed_meta_head_trainer_config_hash
   pysrc.meta.w1_governed_meta_head_trainer.derive_w1_governed_meta_head_model_state_hash
   pysrc.meta.w1_governed_meta_head_trainer.fit_w1_governed_meta_head


Module Contents
---------------

.. py:data:: TRAINED_BY_W1_GOVERNED_META_HEAD_V1
   :type:  Final[str]
   :value: Ellipsis


.. py:class:: W1GovernedMetaHeadTrainConfig

   .. py:attribute:: outer_lr
      :type:  float
      :value: Ellipsis



   .. py:attribute:: n_gradient_steps
      :type:  int
      :value: Ellipsis



.. py:class:: W1GovernedMetaHeadTrainSuccess

   .. py:attribute:: weights
      :type:  NDArray[np.float64]
      :value: Ellipsis



   .. py:attribute:: tasks
      :type:  tuple[MetaTask, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: trainer_config_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: model_state_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: training_run_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: final_mse
      :type:  float
      :value: Ellipsis



   .. py:attribute:: batch_counts
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: code_version
      :type:  str
      :value: Ellipsis



.. py:class:: W1GovernedMetaHeadTrainFailure

   .. py:attribute:: reasons
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: batch_counts
      :type:  dict[str, Any] | None
      :value: Ellipsis



.. py:function:: derive_w1_governed_meta_head_trainer_config_hash(head_cfg, *, reptile_config, batch_size)

.. py:function:: derive_w1_governed_meta_head_model_state_hash(weights)

.. py:function:: fit_w1_governed_meta_head(*, sampler, reptile_config, support_targets_by_task_id, head_cfg, seed)

