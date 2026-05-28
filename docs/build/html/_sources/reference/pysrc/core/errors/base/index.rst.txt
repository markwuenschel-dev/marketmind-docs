pysrc.core.errors.base
======================

.. py:module:: pysrc.core.errors.base


Exceptions
----------

.. autoapisummary::

   pysrc.core.errors.base.BaseError
   pysrc.core.errors.base.UnsupportedPlan
   pysrc.core.errors.base.DataError
   pysrc.core.errors.base.GenericDataError
   pysrc.core.errors.base.AggregateError
   pysrc.core.errors.base.DataFetchError
   pysrc.core.errors.base.APIConnectionError
   pysrc.core.errors.base.StreamConnectionError
   pysrc.core.errors.base.DataTimeoutError
   pysrc.core.errors.base.DataValidationError
   pysrc.core.errors.base.SchemaValidationError
   pysrc.core.errors.base.FileFormatError
   pysrc.core.errors.base.PITViolationError
   pysrc.core.errors.base.StalenessError
   pysrc.core.errors.base.StatisticalTestError
   pysrc.core.errors.base.DataDriftError
   pysrc.core.errors.base.IBKRConnectionError
   pysrc.core.errors.base.NoDataError
   pysrc.core.errors.base.ConfigValidationError
   pysrc.core.errors.base.PreprocessingError
   pysrc.core.errors.base.ModelTrainingError
   pysrc.core.errors.base.TradingExecutionError
   pysrc.core.errors.base.InvalidInputError
   pysrc.core.errors.base.DataPreconditionError
   pysrc.core.errors.base.ModelCheckpointError
   pysrc.core.errors.base.ModelInferenceError


Classes
-------

.. autoapisummary::

   pysrc.core.errors.base.ErrorCodeEnum
   pysrc.core.errors.base.ExceptionRegistry


Module Contents
---------------

.. py:class:: ErrorCodeEnum

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


   .. py:attribute:: GENERIC
      :type:  Any


   .. py:attribute:: DATA_FETCH
      :type:  Any


   .. py:attribute:: API_CONNECTION
      :type:  Any


   .. py:attribute:: STREAM_CONNECTION
      :type:  Any


   .. py:attribute:: DATA_TIMEOUT
      :type:  Any


   .. py:attribute:: DATA_VALIDATION
      :type:  Any


   .. py:attribute:: SCHEMA_VALIDATION
      :type:  Any


   .. py:attribute:: FILE_FORMAT
      :type:  Any


   .. py:attribute:: STATISTICAL_TEST
      :type:  Any


   .. py:attribute:: DATA_DRIFT
      :type:  Any


   .. py:attribute:: NO_DATA
      :type:  Any


   .. py:attribute:: CONFIG_VALIDATION
      :type:  Any


   .. py:attribute:: PREPROCESSING
      :type:  Any


   .. py:attribute:: MODEL_TRAINING
      :type:  Any


   .. py:attribute:: TRADING_EXECUTION
      :type:  Any


   .. py:attribute:: INVALID_INPUT
      :type:  Any


   .. py:attribute:: DATA_PRECONDITION
      :type:  Any


   .. py:attribute:: MODEL_CHECKPOINT
      :type:  Any


   .. py:attribute:: MODEL_INFERENCE
      :type:  Any


   .. py:attribute:: UNSUPPORTED_PLAN
      :type:  Any


   .. py:attribute:: PIT_VIOLATION
      :type:  Any


   .. py:attribute:: STALENESS
      :type:  Any


.. py:exception:: BaseError(msg, *, code = ..., details = ..., cause = ...)

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


   .. py:method:: to_dict()


.. py:exception:: UnsupportedPlan(msg = ..., **kwargs)

   Bases: :py:obj:`BaseError`


   Unspecified run-time error.


.. py:exception:: DataError(message, details = ...)

   Bases: :py:obj:`BaseError`, :py:obj:`ABC`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: GenericDataError(message = ..., details = ...)

   Bases: :py:obj:`DataError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:class:: ExceptionRegistry

   .. py:method:: register(error_type, exception_class)


   .. py:method:: get_exception(error_type, message, details = ...)


.. py:exception:: AggregateError(message = ..., errors = ...)

   Bases: :py:obj:`DataError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


   .. py:method:: add_error(error)


.. py:exception:: DataFetchError(message = ..., details = ...)

   Bases: :py:obj:`DataError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: APIConnectionError(message = ..., details = ...)

   Bases: :py:obj:`DataFetchError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: StreamConnectionError(message = ..., details = ...)

   Bases: :py:obj:`DataFetchError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: DataTimeoutError(message = ..., details = ...)

   Bases: :py:obj:`DataFetchError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: DataValidationError(message = ..., codes = ..., details = ...)

   Bases: :py:obj:`DataError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: SchemaValidationError(message = ..., details = ...)

   Bases: :py:obj:`DataValidationError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: FileFormatError(message = ..., details = ...)

   Bases: :py:obj:`DataValidationError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: PITViolationError(message = ..., details = ...)

   Bases: :py:obj:`DataError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: StalenessError(message = ..., details = ...)

   Bases: :py:obj:`PITViolationError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: StatisticalTestError(message = ..., details = ...)

   Bases: :py:obj:`DataError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: DataDriftError(message = ..., details = ...)

   Bases: :py:obj:`StatisticalTestError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: IBKRConnectionError(message = ..., details = ...)

   Bases: :py:obj:`StreamConnectionError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: NoDataError(symbol, details = ...)

   Bases: :py:obj:`DataFetchError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: ConfigValidationError(message = ..., validation_errors = ...)

   Bases: :py:obj:`DataError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: PreprocessingError(message = ..., details = ...)

   Bases: :py:obj:`DataError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: ModelTrainingError(message = ..., details = ...)

   Bases: :py:obj:`DataError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: TradingExecutionError(message = ..., details = ...)

   Bases: :py:obj:`DataError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: InvalidInputError(message = ..., details = ...)

   Bases: :py:obj:`DataError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: DataPreconditionError(message = ..., details = ...)

   Bases: :py:obj:`DataError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: ModelCheckpointError(message = ..., details = ...)

   Bases: :py:obj:`DataError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


.. py:exception:: ModelInferenceError(message = ..., details = ...)

   Bases: :py:obj:`DataError`


   Unspecified run-time error.


   .. py:method:: get_error_code()


