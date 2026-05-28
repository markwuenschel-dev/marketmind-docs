pysrc.meta.allocator_benchmark.report
=====================================

.. py:module:: pysrc.meta.allocator_benchmark.report


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.report.W2SystemType


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.report.build_w2_v0_report
   pysrc.meta.allocator_benchmark.report.build_w2_v1_report
   pysrc.meta.allocator_benchmark.report.build_w2_v2_report
   pysrc.meta.allocator_benchmark.report.skipped_w2_system_records
   pysrc.meta.allocator_benchmark.report.validate_w2_report
   pysrc.meta.allocator_benchmark.report.validate_w2_system_record


Module Contents
---------------

.. py:data:: W2SystemType
   :type:  Any

.. py:function:: build_w2_v0_report(*, config, run_id, created_at, data, pit, split, baselines, challengers, metrics, concentration, classification)

.. py:function:: build_w2_v1_report(*, config, run_id, created_at, data, pit, split, baselines, challengers, metrics, concentration, structural_failure_reasons = ...)

.. py:function:: build_w2_v2_report(*, config, run_id, created_at, data, pit, split, baselines, challengers, metrics, concentration, classification)

.. py:function:: skipped_w2_system_records(system_type, *, reason)

.. py:function:: validate_w2_report(report)

.. py:function:: validate_w2_system_record(record, *, expected_system_id = ..., expected_system_type = ...)

