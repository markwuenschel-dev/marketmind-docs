pysrc.meta.ewc_config
=====================

.. py:module:: pysrc.meta.ewc_config


Attributes
----------

.. autoapisummary::

   pysrc.meta.ewc_config.THR_MLC6_FD01
   pysrc.meta.ewc_config.THR_MLC6_NG01
   pysrc.meta.ewc_config.THR_MLC6_LM01
   pysrc.meta.ewc_config.MLC6_CONTENT_HASH_CANONICALIZATION
   pysrc.meta.ewc_config.ArmLabel


Classes
-------

.. autoapisummary::

   pysrc.meta.ewc_config.EWCUpdateRecord
   pysrc.meta.ewc_config.EWCArmResult
   pysrc.meta.ewc_config.EWCForgettingReport
   pysrc.meta.ewc_config.EWCSweepConfig


Module Contents
---------------

.. py:data:: THR_MLC6_FD01
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_MLC6_NG01
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_MLC6_LM01
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: MLC6_CONTENT_HASH_CANONICALIZATION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ArmLabel
   :type:  Any

.. py:class:: EWCUpdateRecord

   .. py:attribute:: arm_label
      :type:  str
      :value: Ellipsis



   .. py:attribute:: update_step
      :type:  int
      :value: Ellipsis



   .. py:attribute:: heldout_ic
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: heldout_ic_delta
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: fresh_task_gain
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: theta_l2_drift_from_anchor
      :type:  float | None
      :value: Ellipsis



   .. py:method:: to_json_obj()


.. py:class:: EWCArmResult

   .. py:attribute:: arm_label
      :type:  str
      :value: Ellipsis



   .. py:attribute:: arm_kind
      :type:  Literal['from_scratch', 'warm_start']
      :value: Ellipsis



   .. py:attribute:: lambda_ewc
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: forgetting_delta
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: forgetting_pct
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: mean_fresh_task_gain
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: final_theta_l2_drift
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: arm_status
      :type:  Literal['COMPLETED', 'FAILED']
      :value: Ellipsis



   .. py:attribute:: failure_code
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: update_records
      :type:  tuple[EWCUpdateRecord, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: final_theta_meta
      :type:  tuple[float, Ellipsis]
      :value: Ellipsis



   .. py:method:: to_json_obj()


.. py:class:: EWCForgettingReport

   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: run_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: seed_lineage
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: determinism_tier
      :type:  str
      :value: Ellipsis



   .. py:attribute:: n_pretrain_steps
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_update_steps
      :type:  int
      :value: Ellipsis



   .. py:attribute:: lambda_ewc_values
      :type:  list[float]
      :value: Ellipsis



   .. py:attribute:: from_scratch_result
      :type:  EWCArmResult
      :value: Ellipsis



   .. py:attribute:: warm_start_arm_results
      :type:  list[EWCArmResult]
      :value: Ellipsis



   .. py:attribute:: anchor_regime_counts
      :type:  dict[str, int]
      :value: Ellipsis



   .. py:attribute:: config_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: mlc_scope
      :type:  str
      :value: Ellipsis



   .. py:attribute:: gate_ii_status
      :type:  str
      :value: Ellipsis



   .. py:attribute:: promotion_evidence
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: content_hash
      :type:  dict[str, str]
      :value: Ellipsis



   .. py:attribute:: reproducibility
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:method:: to_json_document()


.. py:class:: EWCSweepConfig

   .. py:attribute:: lambda_ewc_values
      :type:  tuple[float, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: n_pretrain_steps
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_update_steps
      :type:  int
      :value: Ellipsis



   .. py:attribute:: anchor_set_size_per_bucket
      :type:  int
      :value: Ellipsis



   .. py:attribute:: trainer_seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: historical_partition_seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: outer_step_size
      :type:  float
      :value: Ellipsis



   .. py:attribute:: base_trainer_config
      :type:  ReptileTrainerConfig
      :value: Ellipsis



   .. py:method:: config_hash()


   .. py:method:: default_mlc6_bounded(trainer_seed = ..., historical_partition_seed = ...)


