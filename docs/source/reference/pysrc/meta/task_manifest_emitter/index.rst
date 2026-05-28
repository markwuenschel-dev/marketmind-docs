pysrc.meta.task_manifest_emitter
================================

.. py:module:: pysrc.meta.task_manifest_emitter


Attributes
----------

.. autoapisummary::

   pysrc.meta.task_manifest_emitter.SCHEMA_VERSION
   pysrc.meta.task_manifest_emitter.GOVERNED_SCHEMA_VERSION
   pysrc.meta.task_manifest_emitter.CONTENT_HASH_ALGORITHM
   pysrc.meta.task_manifest_emitter.CONTENT_HASH_CANONICALIZATION


Classes
-------

.. autoapisummary::

   pysrc.meta.task_manifest_emitter.TaskManifestTaskInput
   pysrc.meta.task_manifest_emitter.TaskManifestReport


Functions
---------

.. autoapisummary::

   pysrc.meta.task_manifest_emitter.compute_task_id
   pysrc.meta.task_manifest_emitter.resolve_pit_boundary
   pysrc.meta.task_manifest_emitter.build_task_record
   pysrc.meta.task_manifest_emitter.build_task_manifest_document
   pysrc.meta.task_manifest_emitter.emit_task_manifest
   pysrc.meta.task_manifest_emitter.emit_task_manifest_from_mapping
   pysrc.meta.task_manifest_emitter.recompute_task_manifest_content_hash_from_document
   pysrc.meta.task_manifest_emitter.emit_governed_task_manifest


Module Contents
---------------

.. py:data:: SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: GOVERNED_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: CONTENT_HASH_ALGORITHM
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: CONTENT_HASH_CANONICALIZATION
   :type:  Final[str]
   :value: Ellipsis


.. py:class:: TaskManifestTaskInput

   .. py:attribute:: regime_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: regime_class
      :type:  str
      :value: Ellipsis



   .. py:attribute:: t0
      :type:  str
      :value: Ellipsis



   .. py:attribute:: t1
      :type:  str
      :value: Ellipsis



   .. py:attribute:: signal_ids_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: signal_set_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: support_last_timestamp
      :type:  str
      :value: Ellipsis



   .. py:attribute:: pit_boundary
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: signal_ids
      :type:  tuple[str, Ellipsis] | None
      :value: Ellipsis



   .. py:attribute:: signal_mask
      :type:  tuple[bool, Ellipsis] | None
      :value: Ellipsis



   .. py:attribute:: active_k
      :type:  int | None
      :value: Ellipsis



.. py:class:: TaskManifestReport

   .. py:attribute:: document
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: content_hash
      :type:  str
      :value: Ellipsis



.. py:function:: compute_task_id(*, regime_id, t0, t1, signal_ids_hash)

.. py:function:: resolve_pit_boundary(*, support_last_timestamp, pit_boundary)

.. py:function:: build_task_record(task)

.. py:function:: build_task_manifest_document(*, tasks, run_identity, schema_version = ..., include_non_promotable = ...)

.. py:function:: emit_task_manifest(output_path, *, tasks, seed)

.. py:function:: emit_task_manifest_from_mapping(output_path, *, tasks, seed)

.. py:function:: recompute_task_manifest_content_hash_from_document(document)

.. py:function:: emit_governed_task_manifest(tasks, config)

