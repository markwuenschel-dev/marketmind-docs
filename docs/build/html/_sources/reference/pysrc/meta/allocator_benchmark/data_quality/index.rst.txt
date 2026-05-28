pysrc.meta.allocator_benchmark.data_quality
===========================================

.. py:module:: pysrc.meta.allocator_benchmark.data_quality


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.data_quality.W2_V2_DQ_TOP_CONTRIBUTORS
   pysrc.meta.allocator_benchmark.data_quality.W2_V2_DQ_REPORT_NAME
   pysrc.meta.allocator_benchmark.data_quality.W2_V2_DQ_SUMMARY_NAME


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.data_quality.run_w2_v2_top_contributor_data_quality
   pysrc.meta.allocator_benchmark.data_quality.build_w2_v2_top_contributor_data_quality_payload
   pysrc.meta.allocator_benchmark.data_quality.load_amex_raw_ohlcv_panel
   pysrc.meta.allocator_benchmark.data_quality.load_amex_ohlcv_rows


Module Contents
---------------

.. py:data:: W2_V2_DQ_TOP_CONTRIBUTORS
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:data:: W2_V2_DQ_REPORT_NAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: W2_V2_DQ_SUMMARY_NAME
   :type:  Final[str]
   :value: Ellipsis


.. py:function:: run_w2_v2_top_contributor_data_quality(*, amex_fixture_dir = ..., raw_ohlcv_directory = ..., sanity_report_path = ..., accepted_sanity_report_path = ..., signal_rows_path = ..., output_dir = ..., contributors = ..., top_contributors = ..., close_floor = ..., volume_floor = ...)

.. py:function:: build_w2_v2_top_contributor_data_quality_payload(*, selected_trades, raw_ohlcv_panel, top_contributors = ..., close_floor = ..., volume_floor = ..., source_metadata = ..., default_test_net_utility = ..., best_baseline_test_net_utility = ..., selected = ...)

.. py:function:: load_amex_raw_ohlcv_panel(directory)

.. py:function:: load_amex_ohlcv_rows(directory)

