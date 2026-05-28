pysrc.artifact_registry.run_registry
====================================

.. py:module:: pysrc.artifact_registry.run_registry


Attributes
----------

.. autoapisummary::

   pysrc.artifact_registry.run_registry.LOG


Classes
-------

.. autoapisummary::

   pysrc.artifact_registry.run_registry.RunStatus
   pysrc.artifact_registry.run_registry.RunArtifact
   pysrc.artifact_registry.run_registry.RunRecord
   pysrc.artifact_registry.run_registry.RunRegistry


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:class:: RunStatus

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


   .. py:attribute:: REGISTERING
      :type:  Any


   .. py:attribute:: COMPLETE
      :type:  Any


   .. py:attribute:: FAILED
      :type:  Any


.. py:class:: RunArtifact

   .. py:attribute:: role
      :type:  str
      :value: Ellipsis



   .. py:attribute:: cas
      :type:  HashRef
      :value: Ellipsis



   .. py:attribute:: attest
      :type:  HashRef | None
      :value: Ellipsis



   .. py:attribute:: media_type
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: size
      :type:  int
      :value: Ellipsis



.. py:class:: RunRecord

   .. py:attribute:: run_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: status
      :type:  RunStatus
      :value: Ellipsis



   .. py:attribute:: created_at
      :type:  str
      :value: Ellipsis



   .. py:attribute:: updated_at
      :type:  str
      :value: Ellipsis



   .. py:attribute:: artifacts
      :type:  list[RunArtifact]
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:class:: RunRegistry(root)

   .. py:attribute:: INDEX_FILENAME
      :type:  Any


   .. py:attribute:: TRIAL_COUNTERS_FILENAME
      :type:  Any


   .. py:method:: begin_run(metadata = ...)


   .. py:method:: add_artifact(run_id, role, hashes)


   .. py:method:: finalize_run(run_id, status = ...)


   .. py:method:: get_run(run_id, *, include_incomplete = ..., include_failed = ...)


   .. py:method:: iter_runs(*, status_filter = ...)


   .. py:method:: record_trial(family = ...)


   .. py:method:: get_trial_count(family = ...)


