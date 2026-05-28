marketmind_gate.gates.policy
============================

.. py:module:: marketmind_gate.gates.policy


Classes
-------

.. autoapisummary::

   marketmind_gate.gates.policy.ThresholdResult


Functions
---------

.. autoapisummary::

   marketmind_gate.gates.policy.apply_thresholds
   marketmind_gate.gates.policy.check_required_artifacts


Module Contents
---------------

.. py:class:: ThresholdResult

   .. py:attribute:: valid
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: violations
      :type:  list[GateError]
      :value: Ellipsis



.. py:function:: apply_thresholds(transfer_report, policy)

.. py:function:: check_required_artifacts(artifact_types, mode, policy)

