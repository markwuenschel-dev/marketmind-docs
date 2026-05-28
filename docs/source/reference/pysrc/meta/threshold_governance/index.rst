pysrc.meta.threshold_governance
===============================

.. py:module:: pysrc.meta.threshold_governance


Attributes
----------

.. autoapisummary::

   pysrc.meta.threshold_governance.REGISTER_FILENAME
   pysrc.meta.threshold_governance.THRESHOLD_STATES
   pysrc.meta.threshold_governance.REQUIRED_RECORD_FIELDS
   pysrc.meta.threshold_governance.RG09_HARNESS_GATE_PREFLIGHT_IDS


Exceptions
----------

.. autoapisummary::

   pysrc.meta.threshold_governance.ThresholdGovernanceError


Classes
-------

.. autoapisummary::

   pysrc.meta.threshold_governance.ThresholdAuditSeverity
   pysrc.meta.threshold_governance.ThresholdAuditFinding
   pysrc.meta.threshold_governance.ThresholdPreflightReport
   pysrc.meta.threshold_governance.ThresholdRecord
   pysrc.meta.threshold_governance.ConfiguredThresholdSpec


Functions
---------

.. autoapisummary::

   pysrc.meta.threshold_governance.default_register_path
   pysrc.meta.threshold_governance.load_threshold_register
   pysrc.meta.threshold_governance.clear_threshold_register_cache
   pysrc.meta.threshold_governance.resolve_threshold
   pysrc.meta.threshold_governance.require_gate_threshold_id
   pysrc.meta.threshold_governance.warn_hardcoded_threshold
   pysrc.meta.threshold_governance.preflight_configured_thresholds
   pysrc.meta.threshold_governance.preflight_threshold_references
   pysrc.meta.threshold_governance.preflight_report_to_json
   pysrc.meta.threshold_governance.maybe_preflight_rg09_harness_gate_thresholds


Module Contents
---------------

.. py:data:: REGISTER_FILENAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: THRESHOLD_STATES
   :type:  Final[frozenset[str]]
   :value: Ellipsis


.. py:data:: REQUIRED_RECORD_FIELDS
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:exception:: ThresholdGovernanceError(message, *, details = ...)

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:class:: ThresholdAuditSeverity

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


   .. py:attribute:: WARN
      :type:  Any


   .. py:attribute:: FAIL
      :type:  Any


.. py:class:: ThresholdAuditFinding

   .. py:attribute:: severity
      :type:  ThresholdAuditSeverity
      :value: Ellipsis



   .. py:attribute:: code
      :type:  str
      :value: Ellipsis



   .. py:attribute:: message
      :type:  str
      :value: Ellipsis



   .. py:attribute:: details
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:class:: ThresholdPreflightReport

   .. py:attribute:: findings
      :type:  tuple[ThresholdAuditFinding, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: passed
      :type:  bool
      :value: Ellipsis



.. py:class:: ThresholdRecord

   .. py:attribute:: threshold_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: governing_surface
      :type:  str
      :value: Ellipsis



   .. py:attribute:: consumer_surface
      :type:  str
      :value: Ellipsis



   .. py:attribute:: state
      :type:  str
      :value: Ellipsis



   .. py:attribute:: current_expression
      :type:  str
      :value: Ellipsis



   .. py:attribute:: evidence_required
      :type:  str
      :value: Ellipsis



   .. py:attribute:: evidence_location
      :type:  str
      :value: Ellipsis



   .. py:attribute:: authority
      :type:  str
      :value: Ellipsis



   .. py:attribute:: gate_critical
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: supersedes
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: superseded_by
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: last_reviewed
      :type:  str
      :value: Ellipsis



.. py:class:: ConfiguredThresholdSpec

   .. py:attribute:: field_name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: gate_critical
      :type:  bool
      :value: Ellipsis



.. py:function:: default_register_path()

.. py:function:: load_threshold_register(path = ...)

.. py:function:: clear_threshold_register_cache()

.. py:function:: resolve_threshold(threshold_id, *, consumer, gate_critical, register_path = ...)

.. py:function:: require_gate_threshold_id(threshold_id, *, consumer)

.. py:function:: warn_hardcoded_threshold(*, consumer, detail)

.. py:function:: preflight_configured_thresholds(raw_config, *, consumer, field_specs, register_path = ...)

.. py:function:: preflight_threshold_references(refs, *, consumer, register_path = ...)

.. py:function:: preflight_report_to_json(report)

.. py:data:: RG09_HARNESS_GATE_PREFLIGHT_IDS
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:function:: maybe_preflight_rg09_harness_gate_thresholds(*, consumer = ...)

