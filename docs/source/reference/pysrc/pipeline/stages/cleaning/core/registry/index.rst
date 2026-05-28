pysrc.pipeline.stages.cleaning.core.registry
============================================

.. py:module:: pysrc.pipeline.stages.cleaning.core.registry


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.core.registry.CleaningStepRegistration


Functions
---------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.core.registry.register_cleaning_step
   pysrc.pipeline.stages.cleaning.core.registry.bootstrap_default_cleaning_registry
   pysrc.pipeline.stages.cleaning.core.registry.resolve_cleaning_step
   pysrc.pipeline.stages.cleaning.core.registry.list_registered_cleaning_steps
   pysrc.pipeline.stages.cleaning.core.registry.registry_state_hash


Module Contents
---------------

.. py:class:: CleaningStepRegistration

   .. py:attribute:: step_type
      :type:  str
      :value: Ellipsis



   .. py:attribute:: version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: step_cls
      :type:  type[Any]
      :value: Ellipsis



   .. py:attribute:: params_model
      :type:  type[BaseModel]
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



   .. py:attribute:: provider_requirements
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: stateful
      :type:  bool
      :value: Ellipsis



   .. py:method:: descriptor()


.. py:function:: register_cleaning_step(*, step_type, version, params_model, input_contract = ..., output_contract = ..., determinism_tier = ..., provider_requirements = ..., stateful = ...)

.. py:function:: bootstrap_default_cleaning_registry()

.. py:function:: resolve_cleaning_step(step_type, version)

.. py:function:: list_registered_cleaning_steps()

.. py:function:: registry_state_hash()

