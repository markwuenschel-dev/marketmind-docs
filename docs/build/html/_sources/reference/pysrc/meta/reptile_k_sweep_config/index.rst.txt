pysrc.meta.reptile_k_sweep_config
=================================

.. py:module:: pysrc.meta.reptile_k_sweep_config


Attributes
----------

.. autoapisummary::

   pysrc.meta.reptile_k_sweep_config.THR_MLC4_QG01
   pysrc.meta.reptile_k_sweep_config.THR_MLC4_KS01
   pysrc.meta.reptile_k_sweep_config.THR_MLC4_WC01
   pysrc.meta.reptile_k_sweep_config.GOVERNED_K_VALUES
   pysrc.meta.reptile_k_sweep_config.ArmStatus


Classes
-------

.. autoapisummary::

   pysrc.meta.reptile_k_sweep_config.KSweepArmResult
   pysrc.meta.reptile_k_sweep_config.KSweepRegimeResult
   pysrc.meta.reptile_k_sweep_config.KSweepTaskKRecord
   pysrc.meta.reptile_k_sweep_config.KSweepReport
   pysrc.meta.reptile_k_sweep_config.KSweepConfig


Module Contents
---------------

.. py:data:: THR_MLC4_QG01
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_MLC4_KS01
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THR_MLC4_WC01
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: GOVERNED_K_VALUES
   :type:  Final[tuple[int, Ellipsis]]
   :value: Ellipsis


.. py:data:: ArmStatus
   :type:  Any

.. py:class:: KSweepArmResult

   .. py:attribute:: k
      :type:  int
      :value: Ellipsis



   .. py:attribute:: aggregate_mean_delta_ic
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: aggregate_harvey_t
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: wall_clock_s
      :type:  float
      :value: Ellipsis



   .. py:attribute:: saturation_detected
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: arm_status
      :type:  ArmStatus
      :value: Ellipsis



   .. py:attribute:: failure_code
      :type:  str | None
      :value: Ellipsis



   .. py:method:: to_json_obj()


.. py:class:: KSweepRegimeResult

   .. py:attribute:: k
      :type:  int
      :value: Ellipsis



   .. py:attribute:: regime_class
      :type:  str
      :value: Ellipsis



   .. py:attribute:: mean_delta_ic
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: harvey_t
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: task_count
      :type:  int
      :value: Ellipsis



   .. py:method:: to_json_obj()


.. py:class:: KSweepTaskKRecord

   .. py:attribute:: task_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: regime_class
      :type:  str
      :value: Ellipsis



   .. py:attribute:: batch_position
      :type:  int
      :value: Ellipsis



   .. py:attribute:: k
      :type:  int
      :value: Ellipsis



   .. py:attribute:: ic_meta
      :type:  float
      :value: Ellipsis



   .. py:attribute:: ic_adapted
      :type:  float
      :value: Ellipsis



   .. py:attribute:: delta_ic
      :type:  float
      :value: Ellipsis



   .. py:method:: to_json_obj()


.. py:class:: KSweepReport

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



   .. py:attribute:: k_values
      :type:  tuple[int, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: arm_results
      :type:  tuple[KSweepArmResult, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: regime_results
      :type:  tuple[KSweepRegimeResult, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: per_task_records
      :type:  tuple[KSweepTaskKRecord, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: k_sweep_config_hash
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


.. py:class:: KSweepConfig

   .. py:attribute:: k_values
      :type:  tuple[int, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: trainer_seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: curriculum_sampler_seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: base_trainer_config
      :type:  ReptileTrainerConfig
      :value: Ellipsis



   .. py:attribute:: saturation_epsilon
      :type:  float
      :value: Ellipsis



   .. py:method:: k_sweep_config_hash()


   .. py:method:: default_mlc4_bounded(trainer_seed = ..., curriculum_sampler_seed = ..., saturation_epsilon = ...)


