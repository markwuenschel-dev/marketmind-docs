pysrc.tuning.monitoring.latency
===============================

.. py:module:: pysrc.tuning.monitoring.latency


Classes
-------

.. autoapisummary::

   pysrc.tuning.monitoring.latency.LatencyReport
   pysrc.tuning.monitoring.latency.LatencyMonitor


Module Contents
---------------

.. py:class:: LatencyReport

   .. py:attribute:: p50_ms
      :type:  float
      :value: Ellipsis



   .. py:attribute:: p95_ms
      :type:  float
      :value: Ellipsis



   .. py:attribute:: p99_ms
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_ms
      :type:  float
      :value: Ellipsis



.. py:class:: LatencyMonitor

   .. py:method:: record(latency_ms)


   .. py:method:: report()


