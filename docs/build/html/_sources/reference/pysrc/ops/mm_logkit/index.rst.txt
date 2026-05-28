pysrc.ops.mm_logkit
===================

.. py:module:: pysrc.ops.mm_logkit


Attributes
----------

.. autoapisummary::

   pysrc.ops.mm_logkit.HAVE_INFLUX
   pysrc.ops.mm_logkit.REDACT_KEYS_DEFAULT


Classes
-------

.. autoapisummary::

   pysrc.ops.mm_logkit.RedactFilter
   pysrc.ops.mm_logkit.JSONFormatter
   pysrc.ops.mm_logkit.KVFormatter
   pysrc.ops.mm_logkit.LogRecorder
   pysrc.ops.mm_logkit.BoundLogger
   pysrc.ops.mm_logkit.InfluxDBHandler


Functions
---------

.. autoapisummary::

   pysrc.ops.mm_logkit.redact_processor
   pysrc.ops.mm_logkit.redact_sensitive_info
   pysrc.ops.mm_logkit.timestamp_processor
   pysrc.ops.mm_logkit.safe_filter_by_level
   pysrc.ops.mm_logkit.build_console_handler
   pysrc.ops.mm_logkit.build_file_handler
   pysrc.ops.mm_logkit.build_syslog_handler
   pysrc.ops.mm_logkit.build_http_handler
   pysrc.ops.mm_logkit.build_influx_handler
   pysrc.ops.mm_logkit.configure_logger
   pysrc.ops.mm_logkit.get_logger
   pysrc.ops.mm_logkit.log_drift_warning


Module Contents
---------------

.. py:data:: HAVE_INFLUX
   :type:  Any

.. py:data:: REDACT_KEYS_DEFAULT
   :type:  Any

.. py:class:: RedactFilter(keys = ...)

   Bases: :py:obj:`logging.Filter`


   .. py:method:: filter(record)


.. py:function:: redact_processor(_, __, event_dict)

.. py:function:: redact_sensitive_info(keys)

.. py:function:: timestamp_processor(_, __, event_dict)

.. py:function:: safe_filter_by_level(logger, level, event_dict)

.. py:class:: JSONFormatter

   Bases: :py:obj:`logging.Formatter`


   .. py:method:: format(record)


.. py:class:: KVFormatter

   Bases: :py:obj:`logging.Formatter`


   .. py:method:: format(record)


.. py:class:: LogRecorder(logger_name = ...)

   .. py:method:: has_message(substring, level = ...)


.. py:class:: BoundLogger(logger, processors = ..., context = ...)

   Bases: :py:obj:`_BaseBoundLogger`


   .. py:method:: name()


   .. py:method:: setLevel(level)


   .. py:method:: bind(**context)


   .. py:method:: debug(msg, *a, **k)


   .. py:method:: info(msg, *a, **k)


   .. py:method:: warning(msg, *a, **k)


   .. py:method:: error(msg, *a, **k)


   .. py:method:: critical(msg, *a, **k)


   .. py:method:: exception(msg, *a, **k)


   .. py:method:: DEBUG(*args, **kwargs)


   .. py:method:: INFO(*args, **kwargs)


   .. py:method:: WARNING(*args, **kwargs)


   .. py:method:: ERROR(*args, **kwargs)


   .. py:method:: CRITICAL(*args, **kwargs)


   .. py:method:: EXCEPTION(*args, **kwargs)


.. py:function:: build_console_handler(cfg)

.. py:function:: build_file_handler(cfg)

.. py:function:: build_syslog_handler(cfg)

.. py:function:: build_http_handler(cfg)

.. py:function:: build_influx_handler(cfg)

.. py:function:: configure_logger(config = ..., **legacy_kwargs)

.. py:function:: get_logger(name = ...)

.. py:function:: log_drift_warning(*args, **kwargs)

.. py:class:: InfluxDBHandler(client, bucket, org)

   Bases: :py:obj:`logging.Handler`


   .. py:method:: emit(record)


   .. py:method:: handleError(record)


