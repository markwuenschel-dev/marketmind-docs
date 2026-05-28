pysrc.meta.allocator_benchmark.w3_replication
=============================================

.. py:module:: pysrc.meta.allocator_benchmark.w3_replication


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_replication.W3_REPLICATION_OUTPUT_DIR
   pysrc.meta.allocator_benchmark.w3_replication.W3_REPLICATION_REPORT_NAME
   pysrc.meta.allocator_benchmark.w3_replication.W3_REPLICATION_SUMMARY_NAME
   pysrc.meta.allocator_benchmark.w3_replication.W3_REPLICATION_DEFAULT_SEEDS
   pysrc.meta.allocator_benchmark.w3_replication.W3_REPLICATION_DEFAULT_TOP_K_VALUES


Classes
-------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_replication.W3ReplicationConfig


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_replication.run_w3_replication_and_concentration_test
   pysrc.meta.allocator_benchmark.w3_replication.build_w3_replication_report


Module Contents
---------------

.. py:data:: W3_REPLICATION_OUTPUT_DIR
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: W3_REPLICATION_REPORT_NAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W3_REPLICATION_SUMMARY_NAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W3_REPLICATION_DEFAULT_SEEDS
   :type:  Final[tuple[int, Ellipsis]]
   :value: Ellipsis


.. py:data:: W3_REPLICATION_DEFAULT_TOP_K_VALUES
   :type:  Final[tuple[int, Ellipsis]]
   :value: Ellipsis


.. py:class:: W3ReplicationConfig

   .. py:attribute:: close_floor
      :type:  float
      :value: Ellipsis



   .. py:attribute:: volume_floor
      :type:  float
      :value: Ellipsis



   .. py:attribute:: seeds
      :type:  tuple[int, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: top_k_values
      :type:  tuple[int, Ellipsis]
      :value: Ellipsis



.. py:function:: run_w3_replication_and_concentration_test(*, freeze_manifest_path = ..., baseline_report_path = ..., signal_rows_path = ..., amex_fixture_dir = ..., accepted_w2_v2_report_path = ..., output_dir = ..., expected_baseline_report_hash = ..., replication_config = ..., challenger_runner = ...)

.. py:function:: build_w3_replication_report(*, signal_rows, baseline_records, config, replication_config = ..., source_metadata = ..., challenger_runner = ...)

