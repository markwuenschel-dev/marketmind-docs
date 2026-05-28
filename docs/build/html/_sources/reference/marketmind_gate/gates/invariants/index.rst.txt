marketmind_gate.gates.invariants
================================

.. py:module:: marketmind_gate.gates.invariants


Classes
-------

.. autoapisummary::

   marketmind_gate.gates.invariants.InvariantResult


Functions
---------

.. autoapisummary::

   marketmind_gate.gates.invariants.verify_rank_delta_invariant
   marketmind_gate.gates.invariants.verify_k_values_consistency
   marketmind_gate.gates.invariants.verify_transfer_binding
   marketmind_gate.gates.invariants.verify_comparability_locks
   marketmind_gate.gates.invariants.verify_transfer_invariants


Module Contents
---------------

.. py:class:: InvariantResult

   .. py:attribute:: valid
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: errors
      :type:  list[GateError]
      :value: Ellipsis



.. py:function:: verify_rank_delta_invariant(transfer_report)

.. py:function:: verify_k_values_consistency(transfer_report)

.. py:function:: verify_transfer_binding(transfer_report, mode, allow_run_ids = ...)

.. py:function:: verify_comparability_locks(transfer_report, required_locks)

.. py:function:: verify_transfer_invariants(transfer_report, mode, required_locks, allow_run_ids = ...)

