pysrc.tuning.reports.drift_report
=================================

.. py:module:: pysrc.tuning.reports.drift_report


Classes
-------

.. autoapisummary::

   pysrc.tuning.reports.drift_report.DriftReport


Functions
---------

.. autoapisummary::

   pysrc.tuning.reports.drift_report.render_drift_report


Module Contents
---------------

.. py:class:: DriftReport

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: feature_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: mean_drift_score
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_drift_score
      :type:  float
      :value: Ellipsis



   .. py:attribute:: n_triggers
      :type:  int
      :value: Ellipsis



   .. py:attribute:: window_start
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: window_end
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: details
      :type:  dict[str, float]
      :value: Ellipsis



.. py:function:: render_drift_report(artifact)

