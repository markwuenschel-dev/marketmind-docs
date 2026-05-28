pysrc.tuning.reports.validation_report
======================================

.. py:module:: pysrc.tuning.reports.validation_report


Classes
-------

.. autoapisummary::

   pysrc.tuning.reports.validation_report.FoldResult
   pysrc.tuning.reports.validation_report.ValidationReport


Functions
---------

.. autoapisummary::

   pysrc.tuning.reports.validation_report.render_validation_report


Module Contents
---------------

.. py:class:: FoldResult

   .. py:attribute:: fold_index
      :type:  int
      :value: Ellipsis



   .. py:attribute:: sharpe
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_drawdown
      :type:  float
      :value: Ellipsis



   .. py:attribute:: cost_stress_bps
      :type:  float
      :value: Ellipsis



.. py:class:: ValidationReport

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: candidate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: method
      :type:  str
      :value: Ellipsis



   .. py:attribute:: fold_results
      :type:  tuple[FoldResult, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: mean_sharpe
      :type:  float
      :value: Ellipsis



   .. py:attribute:: mean_drawdown
      :type:  float
      :value: Ellipsis



.. py:function:: render_validation_report(artifact)

