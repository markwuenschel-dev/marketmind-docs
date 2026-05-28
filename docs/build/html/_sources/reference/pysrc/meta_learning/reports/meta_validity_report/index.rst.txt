pysrc.meta_learning.reports.meta_validity_report
================================================

.. py:module:: pysrc.meta_learning.reports.meta_validity_report


Attributes
----------

.. autoapisummary::

   pysrc.meta_learning.reports.meta_validity_report.REQUIRED_TOP_LEVEL_KEYS
   pysrc.meta_learning.reports.meta_validity_report.INNER_LOOP_GAIN_KEYS
   pysrc.meta_learning.reports.meta_validity_report.TASK_POOL_COUNTS_REQUIRED
   pysrc.meta_learning.reports.meta_validity_report.TASK_POOL_COUNTS_OPTIONAL
   pysrc.meta_learning.reports.meta_validity_report.CONFIDENCE_CALIBRATION_KEYS


Exceptions
----------

.. autoapisummary::

   pysrc.meta_learning.reports.meta_validity_report.MetaValidityReportBuildError


Classes
-------

.. autoapisummary::

   pysrc.meta_learning.reports.meta_validity_report.MetaValidityReportBuilder


Functions
---------

.. autoapisummary::

   pysrc.meta_learning.reports.meta_validity_report.validate_inner_loop_gain_block
   pysrc.meta_learning.reports.meta_validity_report.validate_task_pool_counts_block
   pysrc.meta_learning.reports.meta_validity_report.validate_confidence_calibration_block
   pysrc.meta_learning.reports.meta_validity_report.validate_meta_validity_report_keys
   pysrc.meta_learning.reports.meta_validity_report.scaffold_inner_loop_gain
   pysrc.meta_learning.reports.meta_validity_report.scaffold_task_pool_counts
   pysrc.meta_learning.reports.meta_validity_report.scaffold_confidence_calibration
   pysrc.meta_learning.reports.meta_validity_report.build_meta_validity_report


Module Contents
---------------

.. py:data:: REQUIRED_TOP_LEVEL_KEYS
   :type:  frozenset[str]
   :value: Ellipsis


.. py:data:: INNER_LOOP_GAIN_KEYS
   :type:  frozenset[str]
   :value: Ellipsis


.. py:data:: TASK_POOL_COUNTS_REQUIRED
   :type:  frozenset[str]
   :value: Ellipsis


.. py:data:: TASK_POOL_COUNTS_OPTIONAL
   :type:  frozenset[str]
   :value: Ellipsis


.. py:data:: CONFIDENCE_CALIBRATION_KEYS
   :type:  frozenset[str]
   :value: Ellipsis


.. py:exception:: MetaValidityReportBuildError

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:function:: validate_inner_loop_gain_block(obj)

.. py:function:: validate_task_pool_counts_block(obj)

.. py:function:: validate_confidence_calibration_block(obj)

.. py:function:: validate_meta_validity_report_keys(payload)

.. py:function:: scaffold_inner_loop_gain(*, mean_query_ic = ..., harvey_t = ..., by_regime_class = ...)

.. py:function:: scaffold_task_pool_counts(*, batch_size, crisis_count, crisis_required, bucket_counts, phase = ...)

.. py:function:: scaffold_confidence_calibration(*, ece = ..., note = ...)

.. py:function:: build_meta_validity_report(*, schema_version, run_id, overall_result, reporting_gate, inner_loop_gain, shuffle_test_p_value, proxy_IC_pearson_r, crisis_holdout_ic, forgetting_ic_degradation_pct, task_pool_counts, confidence_calibration, fail_reasons, theta_day_prime_promoted, timestamp_utc = ...)

.. py:class:: MetaValidityReportBuilder

   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: run_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: overall_result
      :type:  str
      :value: Ellipsis



   .. py:attribute:: reporting_gate
      :type:  str
      :value: Ellipsis



   .. py:attribute:: inner_loop_gain
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: shuffle_test_p_value
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: proxy_IC_pearson_r
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: crisis_holdout_ic
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: forgetting_ic_degradation_pct
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: task_pool_counts
      :type:  dict[str, Any] | None
      :value: Ellipsis



   .. py:attribute:: confidence_calibration
      :type:  dict[str, Any] | None
      :value: Ellipsis



   .. py:attribute:: fail_reasons
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: theta_day_prime_promoted
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: timestamp_utc
      :type:  str | None
      :value: Ellipsis



   .. py:method:: build()


