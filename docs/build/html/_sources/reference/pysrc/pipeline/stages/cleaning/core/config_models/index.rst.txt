pysrc.pipeline.stages.cleaning.core.config_models
=================================================

.. py:module:: pysrc.pipeline.stages.cleaning.core.config_models


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.core.config_models.ExternalFrameContractModel
   pysrc.pipeline.stages.cleaning.core.config_models.ExternalCleaningStepSpecModel
   pysrc.pipeline.stages.cleaning.core.config_models.ExternalCleaningComboModel
   pysrc.pipeline.stages.cleaning.core.config_models.ExternalCleaningPipelineSpecModel
   pysrc.pipeline.stages.cleaning.core.config_models.ExternalCleaningConfigModel


Functions
---------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.core.config_models.pipeline_spec_from_external_cleaning_config
   pysrc.pipeline.stages.cleaning.core.config_models.pipeline_spec_from_external_pipeline_spec


Module Contents
---------------

.. py:class:: ExternalFrameContractModel

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: required_columns
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: optional_columns
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: schema_payload
      :type:  Mapping[str, Any] | None
      :value: Ellipsis



   .. py:attribute:: strict
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: unknown_ok
      :type:  bool
      :value: Ellipsis



   .. py:method:: to_internal()


.. py:class:: ExternalCleaningStepSpecModel

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: step_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: step_type
      :type:  str
      :value: Ellipsis



   .. py:attribute:: version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: params
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: input_contract
      :type:  ExternalFrameContractModel
      :value: Ellipsis



   .. py:attribute:: output_contract
      :type:  ExternalFrameContractModel
      :value: Ellipsis



   .. py:attribute:: determinism_tier
      :type:  CleaningDeterminismTier | None
      :value: Ellipsis



   .. py:attribute:: governance_mode
      :type:  GovernanceMode | None
      :value: Ellipsis



   .. py:attribute:: fallback_policy
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:method:: to_internal(*, default_governance_mode, default_determinism_tier)


.. py:class:: ExternalCleaningComboModel

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: name
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: when
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: steps
      :type:  tuple[ExternalCleaningStepSpecModel, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: order
      :type:  Mapping[str, Mapping[str, tuple[str, Ellipsis]]]
      :value: Ellipsis



.. py:class:: ExternalCleaningPipelineSpecModel

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: steps
      :type:  tuple[ExternalCleaningStepSpecModel, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: determinism_tier
      :type:  CleaningDeterminismTier
      :value: Ellipsis



   .. py:attribute:: governance_mode
      :type:  GovernanceMode
      :value: Ellipsis



   .. py:attribute:: seed_lineage
      :type:  str
      :value: Ellipsis



   .. py:attribute:: pit_boundary
      :type:  str
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:method:: to_internal()


.. py:class:: ExternalCleaningConfigModel

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: use
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: determinism_tier
      :type:  CleaningDeterminismTier
      :value: Ellipsis



   .. py:attribute:: governance_mode
      :type:  GovernanceMode
      :value: Ellipsis



   .. py:attribute:: seed_lineage
      :type:  str
      :value: Ellipsis



   .. py:attribute:: pit_boundary
      :type:  str
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: combos
      :type:  Mapping[str, ExternalCleaningComboModel] | tuple[ExternalCleaningComboModel, Ellipsis]
      :value: Ellipsis



.. py:function:: pipeline_spec_from_external_cleaning_config(raw, *, context = ..., metadata = ..., name = ...)

.. py:function:: pipeline_spec_from_external_pipeline_spec(raw)

