marketmind_gate.gates.core
==========================

.. py:module:: marketmind_gate.gates.core


Classes
-------

.. autoapisummary::

   marketmind_gate.gates.core.GateStatus
   marketmind_gate.gates.core.GateResult
   marketmind_gate.gates.core.ValidationResult


Functions
---------

.. autoapisummary::

   marketmind_gate.gates.core.gate_files_exist
   marketmind_gate.gates.core.gate_json_valid
   marketmind_gate.gates.core.gate_sharpe_threshold
   marketmind_gate.gates.core.gate_max_drawdown
   marketmind_gate.gates.core.validate_bundle


Module Contents
---------------

.. py:class:: GateStatus

   Bases: :py:obj:`Enum`


   .. py:attribute:: PASS
      :type:  Any


   .. py:attribute:: FAIL
      :type:  Any


.. py:class:: GateResult

   .. py:attribute:: gate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: status
      :type:  GateStatus
      :value: Ellipsis



   .. py:attribute:: reason
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: evidence
      :type:  Optional[dict[str, Any]]
      :value: Ellipsis



.. py:class:: ValidationResult

   .. py:attribute:: bundle_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: overall_status
      :type:  GateStatus
      :value: Ellipsis



   .. py:attribute:: gates
      :type:  List[GateResult]
      :value: Ellipsis



   .. py:method:: to_dict()


.. py:function:: gate_files_exist(bundle_path)

.. py:function:: gate_json_valid(bundle_path)

.. py:function:: gate_sharpe_threshold(bundle_path, min_sharpe = ...)

.. py:function:: gate_max_drawdown(bundle_path, max_allowed = ...)

.. py:function:: validate_bundle(bundle_path)

