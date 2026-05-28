pysrc.registry.screening_taxonomy
=================================

.. py:module:: pysrc.registry.screening_taxonomy


Attributes
----------

.. autoapisummary::

   pysrc.registry.screening_taxonomy.REASON_CODE_TO_FAMILY


Classes
-------

.. autoapisummary::

   pysrc.registry.screening_taxonomy.ScreeningStage
   pysrc.registry.screening_taxonomy.ScreeningStatus
   pysrc.registry.screening_taxonomy.ReasonFamily
   pysrc.registry.screening_taxonomy.ReasonCode


Module Contents
---------------

.. py:class:: ScreeningStage

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


   .. py:attribute:: INTAKE
      :type:  Any


   .. py:attribute:: LANE_0
      :type:  Any


   .. py:attribute:: LANE_1
      :type:  Any


   .. py:attribute:: LANE_2
      :type:  Any


   .. py:attribute:: PROMOTION
      :type:  Any


.. py:class:: ScreeningStatus

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


   .. py:attribute:: ACCEPTED
      :type:  Any


   .. py:attribute:: REJECTED
      :type:  Any


   .. py:attribute:: ERROR
      :type:  Any


   .. py:attribute:: SKIPPED
      :type:  Any


.. py:class:: ReasonFamily

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


   .. py:attribute:: SPEC
      :type:  Any


   .. py:attribute:: DATA
      :type:  Any


   .. py:attribute:: DUPLICATE
      :type:  Any


   .. py:attribute:: INVARIANT
      :type:  Any


   .. py:attribute:: STAT_VALIDITY
      :type:  Any


   .. py:attribute:: COST
      :type:  Any


   .. py:attribute:: STABILITY
      :type:  Any


   .. py:attribute:: PROMOTION
      :type:  Any


   .. py:attribute:: SYSTEM
      :type:  Any


.. py:class:: ReasonCode

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


   .. py:attribute:: SPEC_INVALID
      :type:  Any


   .. py:attribute:: SCHEMA_VALIDATION_FAIL
      :type:  Any


   .. py:attribute:: DUPLICATE_SPEC_HASH
      :type:  Any


   .. py:attribute:: DATA_UNAVAILABLE
      :type:  Any


   .. py:attribute:: UNSUPPORTED_INPUT_DOMAIN
      :type:  Any


   .. py:attribute:: PROVENANCE_REFERENCE_MISSING
      :type:  Any


   .. py:attribute:: RESOURCE_BUDGET_EXCEEDED
      :type:  Any


   .. py:attribute:: INVARIANT_PRECHECK_FAIL
      :type:  Any


   .. py:attribute:: IC_BELOW_THRESHOLD
      :type:  Any


   .. py:attribute:: DSR_P_ABOVE_CUTOFF
      :type:  Any


   .. py:attribute:: PBO_ABOVE_CUTOFF
      :type:  Any


   .. py:attribute:: HARVEY_T_BELOW_CUTOFF
      :type:  Any


   .. py:attribute:: COST_MODEL_FAIL
      :type:  Any


   .. py:attribute:: LEAKAGE_INVARIANT_VIOLATION
      :type:  Any


   .. py:attribute:: FEATURE_STABILITY_FAIL
      :type:  Any


   .. py:attribute:: REGIME_COVERAGE_FAIL
      :type:  Any


   .. py:attribute:: ANTI_GOODHART_FAIL
      :type:  Any


   .. py:attribute:: BASELINE_REGRESSION
      :type:  Any


   .. py:attribute:: PROMOTION_VETO
      :type:  Any


.. py:data:: REASON_CODE_TO_FAMILY
   :type:  Dict[ReasonCode, ReasonFamily]
   :value: Ellipsis


