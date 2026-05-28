pysrc.meta_learning.confidence_contract
=======================================

.. py:module:: pysrc.meta_learning.confidence_contract


Attributes
----------

.. autoapisummary::

   pysrc.meta_learning.confidence_contract.CONFIDENCE_SCALAR_MIN
   pysrc.meta_learning.confidence_contract.CONFIDENCE_SCALAR_MAX
   pysrc.meta_learning.confidence_contract.CONFIDENCE_CALIBRATION_SCHEMA_VERSION
   pysrc.meta_learning.confidence_contract.REPORTING_GATE_PASS
   pysrc.meta_learning.confidence_contract.REPORTING_GATE_FAIL
   pysrc.meta_learning.confidence_contract.REPORTING_GATE_INSUFFICIENT


Functions
---------

.. autoapisummary::

   pysrc.meta_learning.confidence_contract.validate_confidence_scalar
   pysrc.meta_learning.confidence_contract.apply_confidence_attenuation
   pysrc.meta_learning.confidence_contract.is_routing_enabled
   pysrc.meta_learning.confidence_contract.insufficient_confidence_calibration_block
   pysrc.meta_learning.confidence_contract.synthetic_confidence_calibration_pass_block
   pysrc.meta_learning.confidence_contract.validate_confidence_calibration_artifact_block


Module Contents
---------------

.. py:data:: CONFIDENCE_SCALAR_MIN
   :type:  Final[float]
   :value: Ellipsis


.. py:data:: CONFIDENCE_SCALAR_MAX
   :type:  Final[float]
   :value: Ellipsis


.. py:data:: CONFIDENCE_CALIBRATION_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: REPORTING_GATE_PASS
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: REPORTING_GATE_FAIL
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: REPORTING_GATE_INSUFFICIENT
   :type:  Final[str]
   :value: Ellipsis


.. py:function:: validate_confidence_scalar(value)

.. py:function:: apply_confidence_attenuation(*, base_position, confidence_scalar)

.. py:function:: is_routing_enabled(*, pilot_explicit_opt_in = ..., reject_set_negative_evidence_after_costs = ...)

.. py:function:: insufficient_confidence_calibration_block(*, reason)

.. py:function:: synthetic_confidence_calibration_pass_block(*, ece_value, calibration_method = ..., reliability_reference = ...)

.. py:function:: validate_confidence_calibration_artifact_block(obj)

