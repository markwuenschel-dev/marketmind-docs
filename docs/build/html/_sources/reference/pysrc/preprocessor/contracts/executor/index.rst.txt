pysrc.preprocessor.contracts.executor
=====================================

.. py:module:: pysrc.preprocessor.contracts.executor


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.contracts.executor.CapabilityFacts
   pysrc.preprocessor.contracts.executor.ExecutionEvidence
   pysrc.preprocessor.contracts.executor.GovernedExecutionSpec
   pysrc.preprocessor.contracts.executor.GovernedExecutionCacheKey


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.contracts.executor.reject_if_governance_required
   pysrc.preprocessor.contracts.executor.validate_governed_execution


Module Contents
---------------

.. py:class:: CapabilityFacts

   .. py:attribute:: has_cudf
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: has_polars_gpu
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: backend
      :type:  str
      :value: Ellipsis



   .. py:method:: to_payload()


.. py:class:: ExecutionEvidence

   .. py:attribute:: events
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: metrics
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:method:: to_payload()


.. py:class:: GovernedExecutionSpec

   .. py:attribute:: plan
      :type:  PreprocessingPlan
      :value: Ellipsis



   .. py:attribute:: state
      :type:  PreprocessingStateManifest
      :value: Ellipsis



   .. py:attribute:: capabilities
      :type:  CapabilityFacts
      :value: Ellipsis



   .. py:attribute:: governance
      :type:  GovernanceDecision
      :value: Ellipsis



   .. py:attribute:: actual_materialization
      :type:  str
      :value: Ellipsis



   .. py:attribute:: schema_signature
      :type:  str
      :value: Ellipsis



   .. py:attribute:: evidence
      :type:  ExecutionEvidence
      :value: Ellipsis



   .. py:attribute:: attempted_retry
      :type:  bool
      :value: Ellipsis



.. py:class:: GovernedExecutionCacheKey

   .. py:attribute:: value
      :type:  str
      :value: Ellipsis



   .. py:method:: from_inputs(*, plan, state, capabilities, governance)


.. py:function:: reject_if_governance_required(*, governed, fallback_name)

.. py:function:: validate_governed_execution(spec)

