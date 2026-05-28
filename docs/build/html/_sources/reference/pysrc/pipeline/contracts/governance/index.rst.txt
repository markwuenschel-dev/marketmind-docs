pysrc.pipeline.contracts.governance
===================================

.. py:module:: pysrc.pipeline.contracts.governance


Classes
-------

.. autoapisummary::

   pysrc.pipeline.contracts.governance.Admissibility
   pysrc.pipeline.contracts.governance.FailureClass
   pysrc.pipeline.contracts.governance.DowngradePolicy
   pysrc.pipeline.contracts.governance.MaterializationPolicy
   pysrc.pipeline.contracts.governance.RetryPolicyClass
   pysrc.pipeline.contracts.governance.GovernanceDecision


Functions
---------

.. autoapisummary::

   pysrc.pipeline.contracts.governance.validate_fail_closed_defaults
   pysrc.pipeline.contracts.governance.require_governed_admissible


Module Contents
---------------

.. py:class:: Admissibility

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


   .. py:attribute:: ADMIT
      :type:  Any


   .. py:attribute:: REJECT
      :type:  Any


.. py:class:: FailureClass

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


   .. py:attribute:: CONTRACT_VIOLATION
      :type:  Any


   .. py:attribute:: CAPABILITY_REJECTION
      :type:  Any


   .. py:attribute:: RETRYABLE_OPERATIONAL_FAILURE
      :type:  Any


   .. py:attribute:: NON_GOVERNED_COMPATIBILITY_PATH
      :type:  Any


.. py:class:: DowngradePolicy

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


   .. py:attribute:: NONE_ALLOWED
      :type:  Any


   .. py:attribute:: EXPLICIT_APPROVAL_REQUIRED
      :type:  Any


.. py:class:: MaterializationPolicy

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


   .. py:attribute:: EXACT_DECLARED_ONLY
      :type:  Any


   .. py:attribute:: EXPLICIT_CHANGE_REQUIRED
      :type:  Any


.. py:class:: RetryPolicyClass

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


   .. py:attribute:: NONE
      :type:  Any


   .. py:attribute:: SAME_SEMANTICS_ONLY
      :type:  Any


.. py:class:: GovernanceDecision

   .. py:attribute:: admissibility
      :type:  Admissibility
      :value: Ellipsis



   .. py:attribute:: reasons
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: failure_class
      :type:  FailureClass | None
      :value: Ellipsis



   .. py:attribute:: downgrade_policy
      :type:  DowngradePolicy
      :value: Ellipsis



   .. py:attribute:: materialization_policy
      :type:  MaterializationPolicy
      :value: Ellipsis



   .. py:attribute:: retry_policy
      :type:  RetryPolicyClass
      :value: Ellipsis



   .. py:attribute:: governed
      :type:  bool
      :value: Ellipsis



   .. py:method:: admit(reason, *, governed = ...)


   .. py:method:: reject(reason, *, failure_class = ..., governed = ...)


.. py:function:: validate_fail_closed_defaults(decision)

.. py:function:: require_governed_admissible(decision)

