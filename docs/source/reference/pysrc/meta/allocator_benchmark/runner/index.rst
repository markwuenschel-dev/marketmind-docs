pysrc.meta.allocator_benchmark.runner
=====================================

.. py:module:: pysrc.meta.allocator_benchmark.runner


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.runner.W2AllocatorDataMode
   pysrc.meta.allocator_benchmark.runner.W2AllocatorEvidenceMode
   pysrc.meta.allocator_benchmark.runner.W2AmexDuplicatePolicy


Classes
-------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.runner.W2AllocatorBenchmarkRunResult


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.runner.build_default_w2_allocator_signal_rows
   pysrc.meta.allocator_benchmark.runner.load_w2_allocator_signal_rows
   pysrc.meta.allocator_benchmark.runner.adapt_w2_su_panel_to_w2_allocator_signal_rows
   pysrc.meta.allocator_benchmark.runner.run_w2_allocator_benchmark_from_signal_panel_path
   pysrc.meta.allocator_benchmark.runner.load_amex_2025_ohlcv_fixture_market_panel
   pysrc.meta.allocator_benchmark.runner.build_amex_2025_w2_allocator_signal_rows
   pysrc.meta.allocator_benchmark.runner.run_w2_allocator_benchmark_from_amex_2025_fixture
   pysrc.meta.allocator_benchmark.runner.run_w2_allocator_benchmark
   pysrc.meta.allocator_benchmark.runner.run_w2_v2_challenger_benchmark_from_frozen_inputs
   pysrc.meta.allocator_benchmark.runner.run_w2_v2_challenger_benchmark
   pysrc.meta.allocator_benchmark.runner.classify_w2_v2_result_from_records


Module Contents
---------------

.. py:data:: W2AllocatorDataMode
   :type:  Any

.. py:data:: W2AllocatorEvidenceMode
   :type:  Any

.. py:data:: W2AmexDuplicatePolicy
   :type:  Any

.. py:class:: W2AllocatorBenchmarkRunResult

   .. py:attribute:: weighted_signal_rows
      :type:  pd.DataFrame
      :value: Ellipsis



   .. py:attribute:: decision_rows
      :type:  pd.DataFrame
      :value: Ellipsis



   .. py:attribute:: baselines
      :type:  dict[str, dict[str, object]]
      :value: Ellipsis



   .. py:attribute:: challengers
      :type:  dict[str, dict[str, object]]
      :value: Ellipsis



   .. py:attribute:: metrics
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: report_path
      :type:  Path
      :value: Ellipsis



.. py:function:: build_default_w2_allocator_signal_rows()

.. py:function:: load_w2_allocator_signal_rows(path)

.. py:function:: adapt_w2_su_panel_to_w2_allocator_signal_rows(panel)

.. py:function:: run_w2_allocator_benchmark_from_signal_panel_path(path, *, data_mode, output_dir = ..., seed = ..., timestamp_utc = ...)

.. py:function:: load_amex_2025_ohlcv_fixture_market_panel(directory, *, duplicate_policy = ...)

.. py:function:: build_amex_2025_w2_allocator_signal_rows(directory, *, duplicate_policy = ..., seed = ..., timestamp_utc = ...)

.. py:function:: run_w2_allocator_benchmark_from_amex_2025_fixture(directory = ..., *, output_dir = ..., duplicate_policy = ..., seed = ..., timestamp_utc = ...)

.. py:function:: run_w2_allocator_benchmark(*, signal_rows = ..., decision_rows = ..., config = ..., output_dir = ..., seed = ..., timestamp_utc = ..., data_mode = ..., evidence_mode = ..., official_report = ..., external_data_quality_metrics = ...)

.. py:function:: run_w2_v2_challenger_benchmark_from_frozen_inputs(*, freeze_manifest_path = ..., baseline_report_path = ..., signal_rows_path = ..., expected_baseline_report_hash = ..., output_dir = ..., seed = ..., timestamp_utc = ..., official_report = ...)

.. py:function:: run_w2_v2_challenger_benchmark(*, signal_rows, baseline_records, config = ..., output_dir = ..., seed = ..., timestamp_utc = ..., official_report = ..., frozen_inputs = ...)

.. py:function:: classify_w2_v2_result_from_records(*, baseline_records, challengers, config, observed_instrument_count, cost_data_mode = ..., participation_metrics = ...)

