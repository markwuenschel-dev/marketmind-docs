pysrc.meta.reptile_proxy_alignment_config
=========================================

.. py:module:: pysrc.meta.reptile_proxy_alignment_config


Attributes
----------

.. autoapisummary::

   pysrc.meta.reptile_proxy_alignment_config.THR_MLC5_PA01
   pysrc.meta.reptile_proxy_alignment_config.THR_MLC5_PA02
   pysrc.meta.reptile_proxy_alignment_config.THR_MLC5_EP01
   pysrc.meta.reptile_proxy_alignment_config.MLC5_CONTENT_HASH_CANONICALIZATION
   pysrc.meta.reptile_proxy_alignment_config.ChallengerProxy
   pysrc.meta.reptile_proxy_alignment_config.ControlProxy
   pysrc.meta.reptile_proxy_alignment_config.ArmLabel
   pysrc.meta.reptile_proxy_alignment_config.InnerProxyKind


Classes
-------

.. autoapisummary::

   pysrc.meta.reptile_proxy_alignment_config.ProxyEpochRecord
   pysrc.meta.reptile_proxy_alignment_config.ProxyAlignmentAggregateResult
   pysrc.meta.reptile_proxy_alignment_config.ProxyAlignmentReport
   pysrc.meta.reptile_proxy_alignment_config.ProxyAlignmentConfig


Module Contents
---------------

.. py:data:: THR_MLC5_PA01
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_MLC5_PA02
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_MLC5_EP01
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: MLC5_CONTENT_HASH_CANONICALIZATION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ChallengerProxy
   :type:  Any

.. py:data:: ControlProxy
   :type:  Any

.. py:data:: ArmLabel
   :type:  Any

.. py:data:: InnerProxyKind
   :type:  Any

.. py:class:: ProxyEpochRecord

   .. py:attribute:: epoch
      :type:  int
      :value: Ellipsis



   .. py:attribute:: proxy_type
      :type:  ArmLabel
      :value: Ellipsis



   .. py:attribute:: proxy_loss
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: held_out_ic
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: proxy_loss_delta
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: held_out_ic_delta
      :type:  float | None
      :value: Ellipsis



   .. py:method:: to_json_obj()


.. py:class:: ProxyAlignmentAggregateResult

   .. py:attribute:: proxy_type
      :type:  ArmLabel
      :value: Ellipsis



   .. py:attribute:: pearson_r
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: pearson_p_value
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: n_epochs_measured
      :type:  int
      :value: Ellipsis



   .. py:attribute:: divergence_detected
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: divergence_window_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: epoch_records
      :type:  tuple[ProxyEpochRecord, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: final_theta_meta
      :type:  tuple[float, Ellipsis]
      :value: Ellipsis



   .. py:method:: to_json_obj()


.. py:class:: ProxyAlignmentReport

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



   .. py:attribute:: n_outer_epochs
      :type:  int
      :value: Ellipsis



   .. py:attribute:: challenger_result
      :type:  ProxyAlignmentAggregateResult
      :value: Ellipsis



   .. py:attribute:: control_result
      :type:  ProxyAlignmentAggregateResult
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


.. py:class:: ProxyAlignmentConfig

   .. py:attribute:: n_outer_epochs
      :type:  int
      :value: Ellipsis



   .. py:attribute:: challenger_proxy
      :type:  ChallengerProxy
      :value: Ellipsis



   .. py:attribute:: control_proxy
      :type:  ControlProxy
      :value: Ellipsis



   .. py:attribute:: trainer_seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: curriculum_sampler_seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: heldout_partition_seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: divergence_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: outer_step_size
      :type:  float
      :value: Ellipsis



   .. py:attribute:: soft_rank_temperature
      :type:  float
      :value: Ellipsis



   .. py:attribute:: base_trainer_config
      :type:  ReptileTrainerConfig
      :value: Ellipsis



   .. py:method:: config_hash()


   .. py:method:: default_mlc5_bounded(trainer_seed = ..., curriculum_sampler_seed = ..., heldout_partition_seed = ..., n_outer_epochs = ..., divergence_window = ..., outer_step_size = ..., soft_rank_temperature = ..., challenger_proxy = ...)


