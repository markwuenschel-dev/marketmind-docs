pysrc.pipeline.ii0c_governed_artifacts
======================================

.. py:module:: pysrc.pipeline.ii0c_governed_artifacts


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.ii0c_governed_artifacts.II0C_GOVERNED_SUMMARY_FILENAME
   pysrc.pipeline.ii0c_governed_artifacts.II0C_GOVERNED_SUMMARY_SCHEMA
   pysrc.pipeline.ii0c_governed_artifacts.II0C_WRAPPED_PHASE
   pysrc.pipeline.ii0c_governed_artifacts.II0C_SCAFFOLD_PHASE


Classes
-------

.. autoapisummary::

   pysrc.pipeline.ii0c_governed_artifacts.II0CGovernedArtifactError
   pysrc.pipeline.ii0c_governed_artifacts.II0CGovernedArtifactResult


Functions
---------

.. autoapisummary::

   pysrc.pipeline.ii0c_governed_artifacts.emit_ii0c_governed_artifacts


Module Contents
---------------

.. py:data:: II0C_GOVERNED_SUMMARY_FILENAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: II0C_GOVERNED_SUMMARY_SCHEMA
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: II0C_WRAPPED_PHASE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: II0C_SCAFFOLD_PHASE
   :type:  Final[str]
   :value: Ellipsis


.. py:class:: II0CGovernedArtifactError

   Bases: :py:obj:`PhaseIIArtifactError`


.. py:class:: II0CGovernedArtifactResult

   .. py:attribute:: output_dir
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: wrapper_summary_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: shell_result
      :type:  Phase2MLEvidenceShellResult
      :value: Ellipsis



   .. py:attribute:: wrapper_summary
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:function:: emit_ii0c_governed_artifacts(*, run_context)

