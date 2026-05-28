pysrc.preprocessor.contracts.state
==================================

.. py:module:: pysrc.preprocessor.contracts.state


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.contracts.state.CURRENT_PREPROCESSING_SCHEMA_VERSION


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.contracts.state.FitStateArtifact
   pysrc.preprocessor.contracts.state.PreprocessingStateManifest


Module Contents
---------------

.. py:data:: CURRENT_PREPROCESSING_SCHEMA_VERSION
   :type:  Any

.. py:class:: FitStateArtifact

   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: payload
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:method:: to_payload()


.. py:class:: PreprocessingStateManifest

   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: plan_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: artifacts
      :type:  tuple[FitStateArtifact, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: lineage
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:method:: to_payload()


   .. py:method:: state_id()


