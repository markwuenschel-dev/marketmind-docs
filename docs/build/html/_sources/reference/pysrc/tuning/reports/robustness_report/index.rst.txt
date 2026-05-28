pysrc.tuning.reports.robustness_report
======================================

.. py:module:: pysrc.tuning.reports.robustness_report


Classes
-------

.. autoapisummary::

   pysrc.tuning.reports.robustness_report.RobustnessReport


Functions
---------

.. autoapisummary::

   pysrc.tuning.reports.robustness_report.render_robustness_report


Module Contents
---------------

.. py:class:: RobustnessReport

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: candidate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: fold_score_variance
      :type:  float
      :value: Ellipsis



   .. py:attribute:: stability_score
      :type:  float
      :value: Ellipsis



   .. py:attribute:: pbo_score
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: regime_breakdown
      :type:  dict[str, float]
      :value: Ellipsis



.. py:function:: render_robustness_report(artifact)

