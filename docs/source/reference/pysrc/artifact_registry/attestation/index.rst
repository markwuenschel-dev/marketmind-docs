pysrc.artifact_registry.attestation
===================================

.. py:module:: pysrc.artifact_registry.attestation


Classes
-------

.. autoapisummary::

   pysrc.artifact_registry.attestation.HashRefLike
   pysrc.artifact_registry.attestation.LocalCASProtocol
   pysrc.artifact_registry.attestation.ArtifactHashPair
   pysrc.artifact_registry.attestation.ArtifactEntry
   pysrc.artifact_registry.attestation.ArtifactAttestor
   pysrc.artifact_registry.attestation.BundleManifestWriter


Functions
---------

.. autoapisummary::

   pysrc.artifact_registry.attestation.build_artifact_entry
   pysrc.artifact_registry.attestation.bundle_entries_from_sequence


Module Contents
---------------

.. py:class:: HashRefLike

   Bases: :py:obj:`Protocol`


   .. py:attribute:: domain
      :type:  str
      :value: Ellipsis



   .. py:attribute:: algo
      :type:  str
      :value: Ellipsis



   .. py:attribute:: digest
      :type:  str
      :value: Ellipsis



   .. py:method:: to_id_string()


.. py:class:: LocalCASProtocol

   Bases: :py:obj:`Protocol`


   .. py:method:: put_json(payload)


   .. py:method:: put_bytes(payload, *, media_type)


.. py:class:: ArtifactHashPair

   .. py:attribute:: cas
      :type:  HashRefLike
      :value: Ellipsis



   .. py:attribute:: attest
      :type:  HashRefLike
      :value: Ellipsis



   .. py:attribute:: canonical_bytes
      :type:  bytes
      :value: Ellipsis



.. py:class:: ArtifactEntry

   .. py:attribute:: path
      :type:  str
      :value: Ellipsis



   .. py:attribute:: cas
      :type:  HashRefLike
      :value: Ellipsis



   .. py:attribute:: attest
      :type:  HashRefLike
      :value: Ellipsis



   .. py:attribute:: media_type
      :type:  str
      :value: Ellipsis



   .. py:attribute:: size
      :type:  int
      :value: Ellipsis



   .. py:method:: to_manifest_dict()


.. py:class:: ArtifactAttestor

   .. py:attribute:: cas
      :type:  LocalCASProtocol
      :value: Ellipsis



   .. py:method:: attest_json(payload, *, bundle_path, media_type = ...)


   .. py:method:: attest_bytes(payload, *, bundle_path, media_type)


   .. py:method:: to_gate_content_hash(attest)


.. py:class:: BundleManifestWriter

   .. py:attribute:: output_root
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: hash_policy
      :type:  Mapping[str, str]
      :value: Ellipsis



   .. py:method:: write(*, artifacts, created_at = ..., schema_version = ..., filename = ..., extra = ...)


.. py:function:: build_artifact_entry(*, path, cas, attest, media_type, size)

.. py:function:: bundle_entries_from_sequence(entries)

