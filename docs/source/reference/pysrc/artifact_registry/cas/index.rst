pysrc.artifact_registry.cas
===========================

.. py:module:: pysrc.artifact_registry.cas


Classes
-------

.. autoapisummary::

   pysrc.artifact_registry.cas.HashRefs
   pysrc.artifact_registry.cas.LocalCAS


Module Contents
---------------

.. py:class:: HashRefs

   .. py:attribute:: cas
      :type:  HashRef
      :value: Ellipsis



   .. py:attribute:: attest
      :type:  HashRef | None
      :value: Ellipsis



   .. py:attribute:: size
      :type:  int
      :value: Ellipsis



   .. py:attribute:: media_type
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: canonical_bytes
      :type:  bytes
      :value: Ellipsis



   .. py:method:: to_lineage_dict(*, schema_version = ..., determinism_tier = ...)


.. py:class:: LocalCAS(root)

   .. py:attribute:: CAS_DIR_NAME
      :type:  Any


   .. py:attribute:: ATTEST_INDEX_NAME
      :type:  Any


   .. py:method:: put_json(obj, media_type = ...)


   .. py:method:: put_bytes(data, media_type, logical_name = ...)


   .. py:method:: get_bytes(cas)


   .. py:method:: materialize(cas, path)


   .. py:method:: exists(cas)


   .. py:method:: verify(cas)


   .. py:method:: verify_or_raise(cas)


   .. py:method:: resolve_attest(attest)


