pysrc.ops.observability_sdk
===========================

.. py:module:: pysrc.ops.observability_sdk


Attributes
----------

.. autoapisummary::

   pysrc.ops.observability_sdk.P
   pysrc.ops.observability_sdk.T
   pysrc.ops.observability_sdk.logger


Classes
-------

.. autoapisummary::

   pysrc.ops.observability_sdk.Lane
   pysrc.ops.observability_sdk.Component
   pysrc.ops.observability_sdk.ErrorType
   pysrc.ops.observability_sdk.CacheTier
   pysrc.ops.observability_sdk.SpanContext
   pysrc.ops.observability_sdk.ObservabilitySDK


Functions
---------

.. autoapisummary::

   pysrc.ops.observability_sdk.get_sdk
   pysrc.ops.observability_sdk.span
   pysrc.ops.observability_sdk.time_it
   pysrc.ops.observability_sdk.record_artifact_registered
   pysrc.ops.observability_sdk.record_cache_access
   pysrc.ops.observability_sdk.record_inference_latency
   pysrc.ops.observability_sdk.record_error


Module Contents
---------------

.. py:data:: P
   :type:  Any

.. py:data:: T
   :type:  Any

.. py:data:: logger
   :type:  Any

.. py:class:: Lane

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


   .. py:attribute:: A
      :type:  Any


   .. py:attribute:: B
      :type:  Any


.. py:class:: Component

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


   .. py:attribute:: PREPROCESSOR
      :type:  Any


   .. py:attribute:: INFERENCE
      :type:  Any


   .. py:attribute:: STRATEGY
      :type:  Any


   .. py:attribute:: CACHE
      :type:  Any


   .. py:attribute:: REGISTRY
      :type:  Any


   .. py:attribute:: ORCHESTRATION
      :type:  Any


.. py:class:: ErrorType

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


   .. py:attribute:: VALIDATION
      :type:  Any


   .. py:attribute:: TIMEOUT
      :type:  Any


   .. py:attribute:: RESOURCE
      :type:  Any


   .. py:attribute:: DETERMINISM
      :type:  Any


   .. py:attribute:: CONTRACT
      :type:  Any


   .. py:attribute:: INFRASTRUCTURE
      :type:  Any


   .. py:attribute:: UNKNOWN
      :type:  Any


.. py:class:: CacheTier

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


   .. py:attribute:: L1
      :type:  Any


   .. py:attribute:: L2
      :type:  Any


   .. py:attribute:: L3
      :type:  Any


   .. py:attribute:: L4
      :type:  Any


.. py:class:: SpanContext

   .. py:attribute:: run_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: lane
      :type:  Lane
      :value: Ellipsis



   .. py:attribute:: strategy_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: plan_hash
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: fold_id
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: worker_id
      :type:  str | None
      :value: Ellipsis



.. py:class:: ObservabilitySDK

   .. py:attribute:: service_name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: ALLOWED_METRIC_LABELS
      :type:  Final[frozenset[str]]
      :value: Ellipsis



   .. py:attribute:: HIGH_CARD_FIELDS
      :type:  Final[frozenset[str]]
      :value: Ellipsis



   .. py:method:: set_build_info(version, commit_sha, python_version)


   .. py:method:: span(name, ctx, kind = ..., attributes = ...)


   .. py:method:: record_inference_latency(latency_ms, lane, component = ...)


   .. py:method:: record_cache_access(tier, operation, hit)


   .. py:method:: record_artifact_registered(lane, artifact_type)


   .. py:method:: record_error(error_type, component, ctx = ..., exception = ...)


   .. py:method:: time_it(name, component)


.. py:function:: get_sdk()

.. py:function:: span(name, ctx, kind = ..., attributes = ...)

.. py:function:: time_it(name, component)

.. py:function:: record_artifact_registered(lane, artifact_type)

.. py:function:: record_cache_access(tier, operation, hit)

.. py:function:: record_inference_latency(latency_ms, lane, component = ...)

.. py:function:: record_error(error_type, component, ctx = ..., exception = ...)

