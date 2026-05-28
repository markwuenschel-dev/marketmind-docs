pysrc.registry.screening_report
===============================

.. py:module:: pysrc.registry.screening_report


Classes
-------

.. autoapisummary::

   pysrc.registry.screening_report.ScreeningReportBuilder


Module Contents
---------------

.. py:class:: ScreeningReportBuilder(screening_run_id, pit_boundary, data_snapshot_hash, seed)

   .. py:attribute:: SCHEMA_VERSION
      :type:  Any


   .. py:method:: add_candidate(spec_hash, signal_name, slot_index = ..., evaluation_ordinal = ...)


   .. py:method:: add_stage(candidate_index, stage, status, reason_code = ..., reason_detail = ..., metrics = ..., duration_ms = ..., timestamp = ...)


   .. py:method:: set_final(candidate_index, final_status, final_stage, final_reason_code = ...)


   .. py:method:: serialize()


