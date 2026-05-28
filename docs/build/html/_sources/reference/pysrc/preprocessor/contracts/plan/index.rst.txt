pysrc.preprocessor.contracts.plan
=================================

.. py:module:: pysrc.preprocessor.contracts.plan


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.contracts.plan.MaterializationSpec
   pysrc.preprocessor.contracts.plan.CanonicalOp
   pysrc.preprocessor.contracts.plan.PreprocessingPlan


Module Contents
---------------

.. py:class:: MaterializationSpec

   .. py:attribute:: format
      :type:  str
      :value: Ellipsis



   .. py:attribute:: schema_signature
      :type:  str
      :value: Ellipsis



   .. py:attribute:: partial_allowed
      :type:  bool
      :value: Ellipsis



.. py:class:: CanonicalOp

   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: params
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: provides
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: requires
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:method:: to_payload()


.. py:class:: PreprocessingPlan

   .. py:attribute:: version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: ops
      :type:  tuple[CanonicalOp, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: group_by
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: materialization
      :type:  MaterializationSpec
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:method:: to_payload()


   .. py:method:: plan_id()


