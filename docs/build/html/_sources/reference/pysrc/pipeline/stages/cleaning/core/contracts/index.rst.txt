pysrc.pipeline.stages.cleaning.core.contracts
=============================================

.. py:module:: pysrc.pipeline.stages.cleaning.core.contracts


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.core.contracts.CleaningDeterminismTier
   pysrc.pipeline.stages.cleaning.core.contracts.GovernanceMode
   pysrc.pipeline.stages.cleaning.core.contracts.FrameContract
   pysrc.pipeline.stages.cleaning.core.contracts.CleaningStepSpec
   pysrc.pipeline.stages.cleaning.core.contracts.CleaningPipelineSpec
   pysrc.pipeline.stages.cleaning.core.contracts.CleaningPipelineState
   pysrc.pipeline.stages.cleaning.core.contracts.CleaningMutationSummary
   pysrc.pipeline.stages.cleaning.core.contracts.CleaningRuntimeContext
   pysrc.pipeline.stages.cleaning.core.contracts.CleaningStepResult
   pysrc.pipeline.stages.cleaning.core.contracts.BuiltCleaningPipeline


Module Contents
---------------

.. py:class:: CleaningDeterminismTier

   Bases: :py:obj:`str`, :py:obj:`Enum`


   str(object='') -> str
   str(bytes_or_buffer[, encoding[, errors]]) -> str

   Create a new string object from the given object. If encoding or
   errors is specified, then the object must expose a data buffer
   that will be decoded using the given encoding and error handler.
   Otherwise, returns the result of object.__str__() (if defined)
   or repr(object).
   encoding defaults to sys.getdefaultencoding().
   errors defaults to 'strict'.


   .. py:attribute:: D0
      :type:  Any


   .. py:attribute:: D1
      :type:  Any


   .. py:attribute:: D2
      :type:  Any


   .. py:attribute:: D3
      :type:  Any


.. py:class:: GovernanceMode

   Bases: :py:obj:`str`, :py:obj:`Enum`


   str(object='') -> str
   str(bytes_or_buffer[, encoding[, errors]]) -> str

   Create a new string object from the given object. If encoding or
   errors is specified, then the object must expose a data buffer
   that will be decoded using the given encoding and error handler.
   Otherwise, returns the result of object.__str__() (if defined)
   or repr(object).
   encoding defaults to sys.getdefaultencoding().
   errors defaults to 'strict'.


   .. py:attribute:: GOVERNED
      :type:  Any


   .. py:attribute:: NONGOVERNED
      :type:  Any


.. py:class:: FrameContract

   .. py:attribute:: required_columns
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: optional_columns
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: schema
      :type:  MarketDataFrameSchema | None
      :value: Ellipsis



   .. py:attribute:: strict
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: unknown_ok
      :type:  bool
      :value: Ellipsis



   .. py:method:: from_mapping(raw)


   .. py:method:: validate(df, *, label)


   .. py:method:: to_payload()


.. py:class:: CleaningStepSpec

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
      :type:  FrameContract
      :value: Ellipsis



   .. py:attribute:: output_contract
      :type:  FrameContract
      :value: Ellipsis



   .. py:attribute:: determinism_tier
      :type:  CleaningDeterminismTier
      :value: Ellipsis



   .. py:attribute:: governance_mode
      :type:  GovernanceMode
      :value: Ellipsis



   .. py:attribute:: fallback_policy
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:method:: from_mapping(raw, *, default_governance_mode = ..., default_determinism_tier = ...)


   .. py:method:: to_payload()


.. py:class:: CleaningPipelineSpec

   .. py:attribute:: steps
      :type:  tuple[CleaningStepSpec, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: determinism_tier
      :type:  CleaningDeterminismTier
      :value: Ellipsis



   .. py:attribute:: seed_lineage
      :type:  str
      :value: Ellipsis



   .. py:attribute:: pit_boundary
      :type:  str
      :value: Ellipsis



   .. py:attribute:: governance_mode
      :type:  GovernanceMode
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:method:: from_mapping(raw)


   .. py:method:: to_payload()


.. py:class:: CleaningPipelineState

   .. py:attribute:: step_state
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: warnings
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: fallback_events
      :type:  list[dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: provider_lineage
      :type:  dict[str, dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: validation_failures
      :type:  list[dict[str, Any]]
      :value: Ellipsis



.. py:class:: CleaningMutationSummary

   .. py:attribute:: rows_in
      :type:  int
      :value: Ellipsis



   .. py:attribute:: rows_out
      :type:  int
      :value: Ellipsis



   .. py:attribute:: rows_removed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: rows_with_mutations
      :type:  int
      :value: Ellipsis



   .. py:attribute:: cells_mutated
      :type:  int
      :value: Ellipsis



   .. py:method:: to_payload()


.. py:class:: CleaningRuntimeContext

   .. py:attribute:: run_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: determinism_tier
      :type:  CleaningDeterminismTier
      :value: Ellipsis



   .. py:attribute:: seed_lineage
      :type:  str
      :value: Ellipsis



   .. py:attribute:: pit_boundary
      :type:  str
      :value: Ellipsis



   .. py:attribute:: governance_mode
      :type:  GovernanceMode
      :value: Ellipsis



   .. py:attribute:: providers
      :type:  MutableMapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: streaming
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: registry_state_hash
      :type:  str
      :value: Ellipsis



   .. py:method:: provider(key)


   .. py:method:: seed_for(material)


.. py:class:: CleaningStepResult

   .. py:attribute:: frame
      :type:  pl.DataFrame
      :value: Ellipsis



   .. py:attribute:: state
      :type:  CleaningPipelineState
      :value: Ellipsis



   .. py:attribute:: warnings
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: metrics
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: provider_lineage
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: validation_failures
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: fallback_events
      :type:  list[dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: mutation
      :type:  CleaningMutationSummary
      :value: Ellipsis



   .. py:method:: apply_to_state()


.. py:class:: BuiltCleaningPipeline

   .. py:attribute:: spec
      :type:  CleaningPipelineSpec
      :value: Ellipsis



   .. py:attribute:: steps
      :type:  tuple[Any, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: plan_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: registry_state_hash
      :type:  str
      :value: Ellipsis



   .. py:method:: run(df, *, context = ...)


   .. py:method:: to_plan_payload()


   .. py:method:: to_report_payload(result, *, context)


