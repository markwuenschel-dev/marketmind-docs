pysrc.bridge.dataprep_orchestrator
==================================

.. py:module:: pysrc.bridge.dataprep_orchestrator


Classes
-------

.. autoapisummary::

   pysrc.bridge.dataprep_orchestrator.DataprepSpec
   pysrc.bridge.dataprep_orchestrator.DataprepResult
   pysrc.bridge.dataprep_orchestrator.DataprepOrchestrator


Module Contents
---------------

.. py:class:: DataprepSpec

   .. py:attribute:: pipeline_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: config_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: output_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: as_of
      :type:  str | None
      :value: Ellipsis



.. py:class:: DataprepResult

   .. py:attribute:: success
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: artifact_paths
      :type:  Mapping[str, Path]
      :value: Ellipsis



   .. py:attribute:: lineage_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: metrics
      :type:  Mapping[str, float]
      :value: Ellipsis



.. py:class:: DataprepOrchestrator

   Bases: :py:obj:`ABC`


   .. py:method:: prepare(spec)


   .. py:method:: validate(result)


   .. py:method:: replay(lineage_hash)


