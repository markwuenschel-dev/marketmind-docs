marketmind_gate.gates.integrity
===============================

.. py:module:: marketmind_gate.gates.integrity


Classes
-------

.. autoapisummary::

   marketmind_gate.gates.integrity.ArtifactRef
   marketmind_gate.gates.integrity.IntegrityResult


Functions
---------

.. autoapisummary::

   marketmind_gate.gates.integrity.verify_artifact_integrity
   marketmind_gate.gates.integrity.verify_single_artifact


Module Contents
---------------

.. py:class:: ArtifactRef

   .. py:attribute:: artifact_type
      :type:  str
      :value: Ellipsis



   .. py:attribute:: uri
      :type:  str
      :value: Ellipsis



   .. py:attribute:: content_hash
      :type:  str
      :value: Ellipsis



   .. py:method:: to_dict()


.. py:class:: IntegrityResult

   .. py:attribute:: valid
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: errors
      :type:  list[GateError]
      :value: Ellipsis



   .. py:attribute:: artifact_refs
      :type:  list[ArtifactRef]
      :value: Ellipsis



   .. py:attribute:: artifacts
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:function:: verify_artifact_integrity(bundle_dir, artifact_index)

.. py:function:: verify_single_artifact(uri, declared_hash, bundle_dir)

