pysrc.tuning.monitoring.throughput
==================================

.. py:module:: pysrc.tuning.monitoring.throughput


Classes
-------

.. autoapisummary::

   pysrc.tuning.monitoring.throughput.ThroughputReport
   pysrc.tuning.monitoring.throughput.ThroughputMonitor


Module Contents
---------------

.. py:class:: ThroughputReport

   .. py:attribute:: trials_per_second
      :type:  float
      :value: Ellipsis



   .. py:attribute:: tasks_per_second
      :type:  float
      :value: Ellipsis



   .. py:attribute:: observation_seconds
      :type:  float
      :value: Ellipsis



.. py:class:: ThroughputMonitor

   .. py:method:: record_trial(n = ...)


   .. py:method:: record_task(n = ...)


   .. py:method:: report()


