marketmind_gate.gates.phase2_ml_evidence_shell
==============================================

.. py:module:: marketmind_gate.gates.phase2_ml_evidence_shell


Attributes
----------

.. autoapisummary::

   marketmind_gate.gates.phase2_ml_evidence_shell.REQUIRED_ARTIFACTS
   marketmind_gate.gates.phase2_ml_evidence_shell.SCHEMA_FILES


Classes
-------

.. autoapisummary::

   marketmind_gate.gates.phase2_ml_evidence_shell.Phase2MLEvidenceShellStatus
   marketmind_gate.gates.phase2_ml_evidence_shell.Phase2MLEvidenceShellResult


Functions
---------

.. autoapisummary::

   marketmind_gate.gates.phase2_ml_evidence_shell.evaluate_phase2_ml_evidence_shell


Module Contents
---------------

.. py:class:: Phase2MLEvidenceShellStatus

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


   .. py:attribute:: EVIDENCE_INCOMPLETE
      :type:  Any


   .. py:attribute:: EVIDENCE_STRUCTURALLY_USABLE
      :type:  Any


.. py:data:: REQUIRED_ARTIFACTS
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:data:: SCHEMA_FILES
   :type:  Final[dict[str, str]]
   :value: Ellipsis


.. py:class:: Phase2MLEvidenceShellResult

   .. py:attribute:: status
      :type:  Phase2MLEvidenceShellStatus
      :value: Ellipsis



   .. py:attribute:: artifacts_present
      :type:  dict[str, bool]
      :value: Ellipsis



   .. py:attribute:: schema_ok
      :type:  dict[str, bool]
      :value: Ellipsis



   .. py:attribute:: binding_ok
      :type:  dict[str, bool]
      :value: Ellipsis



   .. py:attribute:: promotable_claim_emitted
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: reason_codes
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: evidence
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:method:: to_json_dict()


.. py:function:: evaluate_phase2_ml_evidence_shell(run_dir)

