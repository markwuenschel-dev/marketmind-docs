pysrc.pipeline.core.pipeline_core_metrics
=========================================

.. py:module:: pysrc.pipeline.core.pipeline_core_metrics


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.core.pipeline_core_metrics.ERROR_COUNTER
   pysrc.pipeline.core.pipeline_core_metrics.STEP_EXECUTION_TIME
   pysrc.pipeline.core.pipeline_core_metrics.mlflow


Exceptions
----------

.. autoapisummary::

   pysrc.pipeline.core.pipeline_core_metrics.PipelineMetricsError
   pysrc.pipeline.core.pipeline_core_metrics.MLflowUnavailable


Classes
-------

.. autoapisummary::

   pysrc.pipeline.core.pipeline_core_metrics.AsyncMLflowLogger


Functions
---------

.. autoapisummary::

   pysrc.pipeline.core.pipeline_core_metrics.track_step_execution
   pysrc.pipeline.core.pipeline_core_metrics.wire_streaming_observers


Module Contents
---------------

.. py:exception:: PipelineMetricsError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: MLflowUnavailable

   Bases: :py:obj:`PipelineMetricsError`


   Common base class for all non-exit exceptions.


.. py:data:: ERROR_COUNTER
   :type:  Any

.. py:data:: STEP_EXECUTION_TIME
   :type:  Any

.. py:data:: mlflow
   :type:  Any

.. py:class:: AsyncMLflowLogger

   .. py:method:: log_metrics(metrics, *, step = ...)
      :async:



   .. py:method:: log_params(params)
      :async:



   .. py:method:: set_experiment(name)
      :async:



   .. py:method:: start_run(*, run_name = ..., nested = ..., tags = ...)
      :async:



   .. py:method:: end_run()
      :async:



   .. py:method:: log_artifact(local_path, *, artifact_path = ...)
      :async:



.. py:function:: track_step_execution(step_name, *, stage = ..., engine = ...)

.. py:function:: wire_streaming_observers(get_buffer_len, get_processed_volume)

