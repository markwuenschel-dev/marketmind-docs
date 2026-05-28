pysrc.registry.gate_to_screening
================================

.. py:module:: pysrc.registry.gate_to_screening


Attributes
----------

.. autoapisummary::

   pysrc.registry.gate_to_screening.GATE_STAGE_MAP
   pysrc.registry.gate_to_screening.GATE_FAIL_REASON_MAP


Functions
---------

.. autoapisummary::

   pysrc.registry.gate_to_screening.gate_result_to_stage_and_code


Module Contents
---------------

.. py:data:: GATE_STAGE_MAP
   :type:  dict[str, ScreeningStage]
   :value: Ellipsis


.. py:data:: GATE_FAIL_REASON_MAP
   :type:  dict[str, ReasonCode]
   :value: Ellipsis


.. py:function:: gate_result_to_stage_and_code(gate_id, passed, reason = ...)

