pysrc.tuning.monitoring.drift
=============================

.. py:module:: pysrc.tuning.monitoring.drift


Classes
-------

.. autoapisummary::

   pysrc.tuning.monitoring.drift.DriftReport
   pysrc.tuning.monitoring.drift.DriftMonitor


Module Contents
---------------

.. py:class:: DriftReport

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: feature_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: drift_score
      :type:  float
      :value: Ellipsis



   .. py:attribute:: threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: is_drifting
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: observed_at
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: details
      :type:  dict[str, float]
      :value: Ellipsis



.. py:class:: DriftMonitor(job_id, threshold)

   .. py:method:: observe(drift_score, feature_hash, now, details = ...)


