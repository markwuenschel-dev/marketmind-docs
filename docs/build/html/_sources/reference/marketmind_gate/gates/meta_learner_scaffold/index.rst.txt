marketmind_gate.gates.meta_learner_scaffold
===========================================

.. py:module:: marketmind_gate.gates.meta_learner_scaffold


Attributes
----------

.. autoapisummary::

   marketmind_gate.gates.meta_learner_scaffold.EXPECTED_TASK_MANIFEST_PREFIX
   marketmind_gate.gates.meta_learner_scaffold.EXPECTED_META_VALIDITY_PREFIX
   marketmind_gate.gates.meta_learner_scaffold.EXPECTED_EXEC_ASSUMPTIONS_PREFIX
   marketmind_gate.gates.meta_learner_scaffold.REQUIRED_ARTIFACTS
   marketmind_gate.gates.meta_learner_scaffold.ARTIFACT_SURFACE_ROLES
   marketmind_gate.gates.meta_learner_scaffold.REASON_MISSING_ARTIFACTS
   marketmind_gate.gates.meta_learner_scaffold.REASON_SCHEMA_PREFIX_MISMATCH
   marketmind_gate.gates.meta_learner_scaffold.REASON_META_VALIDITY_OVERALL_ABSENT
   marketmind_gate.gates.meta_learner_scaffold.REASON_META_VALIDITY_OVERALL_SCAFFOLD
   marketmind_gate.gates.meta_learner_scaffold.REASON_META_VALIDITY_OVERALL_REDACTED
   marketmind_gate.gates.meta_learner_scaffold.REASON_GOVERNED_CONTRACT_MISMATCH
   marketmind_gate.gates.meta_learner_scaffold.REASON_GOVERNED_SCHEMA_INVALID
   marketmind_gate.gates.meta_learner_scaffold.SCHEMA_FILES


Classes
-------

.. autoapisummary::

   marketmind_gate.gates.meta_learner_scaffold.MetaLearnerScaffoldStatus
   marketmind_gate.gates.meta_learner_scaffold.MetaLearnerScaffoldGateResult


Functions
---------

.. autoapisummary::

   marketmind_gate.gates.meta_learner_scaffold.evaluate_meta_learner_scaffold


Module Contents
---------------

.. py:class:: MetaLearnerScaffoldStatus

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


   .. py:attribute:: SCAFFOLD_INCOMPLETE
      :type:  Any


.. py:data:: EXPECTED_TASK_MANIFEST_PREFIX
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: EXPECTED_META_VALIDITY_PREFIX
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: EXPECTED_EXEC_ASSUMPTIONS_PREFIX
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: REQUIRED_ARTIFACTS
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:data:: ARTIFACT_SURFACE_ROLES
   :type:  Final[tuple[tuple[str, str], Ellipsis]]
   :value: Ellipsis


.. py:data:: REASON_MISSING_ARTIFACTS
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: REASON_SCHEMA_PREFIX_MISMATCH
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: REASON_META_VALIDITY_OVERALL_ABSENT
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: REASON_META_VALIDITY_OVERALL_SCAFFOLD
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: REASON_META_VALIDITY_OVERALL_REDACTED
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: REASON_GOVERNED_CONTRACT_MISMATCH
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: REASON_GOVERNED_SCHEMA_INVALID
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: SCHEMA_FILES
   :type:  Final[dict[str, str]]
   :value: Ellipsis


.. py:class:: MetaLearnerScaffoldGateResult

   .. py:attribute:: status
      :type:  MetaLearnerScaffoldStatus
      :value: Ellipsis



   .. py:attribute:: artifacts_present
      :type:  dict[str, bool]
      :value: Ellipsis



   .. py:attribute:: schema_ok
      :type:  dict[str, bool]
      :value: Ellipsis



   .. py:attribute:: overall_result
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: incomplete_reason_codes
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: evidence
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:method:: to_json_dict()


.. py:function:: evaluate_meta_learner_scaffold(run_dir)

