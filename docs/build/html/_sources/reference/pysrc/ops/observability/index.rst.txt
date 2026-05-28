pysrc.ops.observability
=======================

.. py:module:: pysrc.ops.observability


Attributes
----------

.. autoapisummary::

   pysrc.ops.observability.TraceBasedExemplarFilter
   pysrc.ops.observability.ExponentialBucketHistogramAggregation
   pysrc.ops.observability.ExplicitBucketHistogramAggregation
   pysrc.ops.observability.T
   pysrc.ops.observability.F


Exceptions
----------

.. autoapisummary::

   pysrc.ops.observability.ObservabilityError
   pysrc.ops.observability.ExporterEgressError
   pysrc.ops.observability.ExporterTransientError
   pysrc.ops.observability.MetricsEmitError
   pysrc.ops.observability.PiiRedactionError
   pysrc.ops.observability.TracingInitError


Classes
-------

.. autoapisummary::

   pysrc.ops.observability.NoOpMetricsManager
   pysrc.ops.observability.NoOpTracingManager
   pysrc.ops.observability.CircuitBreaker
   pysrc.ops.observability.CardinalityLimiter
   pysrc.ops.observability.PIIRedactor
   pysrc.ops.observability.BoundedEventQueue
   pysrc.ops.observability.MetricConfig
   pysrc.ops.observability.SafeOTLPMetricExporter
   pysrc.ops.observability.MetricsManager
   pysrc.ops.observability.TracingConfig
   pysrc.ops.observability.SafeOTLPSpanExporter
   pysrc.ops.observability.AdaptiveRatioSampler
   pysrc.ops.observability.PiiRedactionSpanProcessor
   pysrc.ops.observability.TracingManager
   pysrc.ops.observability.TraceEnrichedLogger
   pysrc.ops.observability.LoggingManager
   pysrc.ops.observability.AdaptiveThreshold
   pysrc.ops.observability.SLOBurnRate
   pysrc.ops.observability.FastAPIMiddleware
   pysrc.ops.observability.KafkaInstrumentor


Functions
---------

.. autoapisummary::

   pysrc.ops.observability.set_tenant
   pysrc.ops.observability.get_tenant
   pysrc.ops.observability.set_strategy
   pysrc.ops.observability.get_strategy
   pysrc.ops.observability.instrument
   pysrc.ops.observability.register_cache_hit_rate_gauges
   pysrc.ops.observability.register_cache_hit_rate_gauges_for
   pysrc.ops.observability.get_metrics
   pysrc.ops.observability.get_tracing
   pysrc.ops.observability.get_logging
   pysrc.ops.observability.get_logger
   pysrc.ops.observability.init_observability


Module Contents
---------------

.. py:exception:: ObservabilityError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: ExporterEgressError

   Bases: :py:obj:`ObservabilityError`


   Common base class for all non-exit exceptions.


.. py:exception:: ExporterTransientError

   Bases: :py:obj:`ObservabilityError`


   Common base class for all non-exit exceptions.


.. py:exception:: MetricsEmitError

   Bases: :py:obj:`ObservabilityError`


   Common base class for all non-exit exceptions.


.. py:exception:: PiiRedactionError

   Bases: :py:obj:`ObservabilityError`


   Common base class for all non-exit exceptions.


.. py:exception:: TracingInitError

   Bases: :py:obj:`ObservabilityError`


   Common base class for all non-exit exceptions.


.. py:data:: TraceBasedExemplarFilter
   :type:  Any

.. py:data:: ExponentialBucketHistogramAggregation
   :type:  Any

.. py:data:: ExplicitBucketHistogramAggregation
   :type:  Any

.. py:class:: NoOpMetricsManager(*_a, **_k)

   .. py:method:: counter(*_a, **_k)


   .. py:method:: histogram(*_a, **_k)


   .. py:method:: record_counter(*_a, **_k)


   .. py:method:: record_histogram(*_a, **_k)


   .. py:method:: shutdown()


.. py:class:: NoOpTracingManager(*_a, **_k)

   .. py:method:: set_sample_rate(*_a, **_k)


   .. py:method:: start_span(*_a, **_k)


   .. py:method:: start_span_with_links(*_a, **_k)


   .. py:method:: inject_context(carrier)


   .. py:method:: extract_context(carrier)


.. py:data:: T
   :type:  Any

.. py:data:: F
   :type:  Any

.. py:function:: set_tenant(tenant_id)

.. py:function:: get_tenant()

.. py:function:: set_strategy(strategy_id)

.. py:function:: get_strategy()

.. py:class:: CircuitBreaker(fail_threshold = ..., reset_after_sec = ...)

   .. py:method:: on_success()


   .. py:method:: on_failure()


   .. py:method:: is_open()


.. py:class:: CardinalityLimiter(max_keys_per_label = ...)

   .. py:method:: sanitize(label_key, label_value)


   .. py:method:: overflow_count()


   .. py:method:: stats()


.. py:class:: PIIRedactor(patterns = ..., fast_keys_allowlist = ...)

   .. py:attribute:: DEFAULT_PATTERNS
      :type:  Any


   .. py:method:: redact_text(text)


   .. py:method:: redact_dict(data)


.. py:class:: BoundedEventQueue(maxsize = ...)

   .. py:method:: put_nowait(ev)


   .. py:method:: get_batch(n = ...)


   .. py:method:: dropped()


   .. py:method:: size()


.. py:class:: MetricConfig

   .. py:attribute:: prometheus_port
      :type:  int
      :value: Ellipsis



   .. py:attribute:: otlp_endpoint
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: export_interval_millis
      :type:  int
      :value: Ellipsis



   .. py:attribute:: delta_temporality
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: enable_exemplars
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: buffered_emit
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: queue_max_events
      :type:  int
      :value: Ellipsis



   .. py:attribute:: flush_every_ms
      :type:  int
      :value: Ellipsis



   .. py:attribute:: labels_max_keys_per_label
      :type:  int
      :value: Ellipsis



   .. py:attribute:: endpoint_allowlist
      :type:  Tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: exporter_timeout_sec
      :type:  float
      :value: Ellipsis



   .. py:attribute:: breaker_fail_threshold
      :type:  int
      :value: Ellipsis



   .. py:attribute:: breaker_reset_seconds
      :type:  int
      :value: Ellipsis



.. py:class:: SafeOTLPMetricExporter(allowlist, breaker, timeout, *args, **kwargs)

   Bases: :py:obj:`_OTLPMetricExporter if _OTLPMetricExporter is not None else object`


   .. py:method:: export(metrics_data)


.. py:class:: MetricsManager(service_name = ..., config = ...)

   .. py:method:: counter(name, description = ..., unit = ...)


   .. py:method:: histogram(name, description = ..., unit = ...)


   .. py:method:: record_counter(counter, value = ..., labels = ...)


   .. py:method:: record_histogram(histogram, value, labels = ...)


   .. py:method:: shutdown()


.. py:class:: TracingConfig

   .. py:attribute:: otlp_endpoint
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: sample_rate
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_queue_size
      :type:  int
      :value: Ellipsis



   .. py:attribute:: max_export_batch_size
      :type:  int
      :value: Ellipsis



   .. py:attribute:: schedule_delay_millis
      :type:  int
      :value: Ellipsis



   .. py:attribute:: enable_console_export
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: endpoint_allowlist
      :type:  Tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: exporter_timeout_sec
      :type:  float
      :value: Ellipsis



.. py:class:: SafeOTLPSpanExporter(allowlist, breaker, timeout, *args, **kwargs)

   Bases: :py:obj:`_OTLPSpanExporter if _OTLPSpanExporter is not None else object`


   .. py:method:: export(spans)


.. py:class:: AdaptiveRatioSampler(initial_rate)

   Bases: :py:obj:`Sampler`


   .. py:method:: should_sample(parent_context, trace_id, name, kind, attributes, links)


   .. py:method:: get_description()


   .. py:method:: set_rate(new_rate)


.. py:class:: PiiRedactionSpanProcessor

   Bases: :py:obj:`_SpanProcessorBase`


   .. py:method:: on_start(span, parent_context = ...)


   .. py:method:: on_end(span)


   .. py:method:: shutdown()


   .. py:method:: force_flush(timeout_millis = ...)


.. py:class:: TracingManager(service_name = ..., config = ...)

   .. py:method:: set_sample_rate(rate)


   .. py:method:: start_span(name, kind = ..., attributes = ..., links = ...)


   .. py:method:: start_span_with_links(name, linked_spans, **kwargs)


   .. py:method:: inject_context(carrier)


   .. py:method:: extract_context(carrier)


.. py:class:: TraceEnrichedLogger(base_logger, service_name)

   .. py:method:: info(msg, **kwargs)


   .. py:method:: error(msg, **kwargs)


   .. py:method:: warning(msg, **kwargs)


   .. py:method:: debug(msg, **kwargs)


.. py:class:: LoggingManager(service_name = ..., mm_config = ...)

   .. py:method:: get_logger()


.. py:class:: AdaptiveThreshold(alpha = ..., sensitivity = ..., window_size = ...)

   .. py:method:: update(value)


   .. py:method:: threshold()


.. py:class:: SLOBurnRate(minutes = ...)

   .. py:method:: record(ok)


   .. py:method:: burn_rates(slo_error_budget)


.. py:function:: instrument(name = ..., labels = ..., record_exceptions = ..., measure_latency = ...)

.. py:class:: FastAPIMiddleware(app, service_name = ..., slo_error_budget = ...)

.. py:class:: KafkaInstrumentor

   .. py:method:: inject_context(headers)


   .. py:method:: extract_context(headers)


   .. py:method:: instrument_producer(producer)


   .. py:method:: instrument_consumer(consumer)


.. py:function:: register_cache_hit_rate_gauges(cache_client, metric_name = ...)

.. py:function:: register_cache_hit_rate_gauges_for(func_or_client, metric_name = ...)

.. py:function:: get_metrics()

.. py:function:: get_tracing()

.. py:function:: get_logging()

.. py:function:: get_logger()

.. py:function:: init_observability(service_name = ..., metrics_config = ..., tracing_config = ..., enable_metrics = ..., enable_tracing = ..., enable_logging = ...)

