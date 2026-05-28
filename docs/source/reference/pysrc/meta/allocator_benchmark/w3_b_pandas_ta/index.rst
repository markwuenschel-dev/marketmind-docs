pysrc.meta.allocator_benchmark.w3_b_pandas_ta
=============================================

.. py:module:: pysrc.meta.allocator_benchmark.w3_b_pandas_ta


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_b_pandas_ta.W3_B_PANDAS_TA_DIR
   pysrc.meta.allocator_benchmark.w3_b_pandas_ta.W3A_FROZEN_BASELINES
   pysrc.meta.allocator_benchmark.w3_b_pandas_ta.LOG


Classes
-------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_b_pandas_ta.W3BPandasTARunResult


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_b_pandas_ta.run_w3_b_pandas_ta_experiment
   pysrc.meta.allocator_benchmark.w3_b_pandas_ta.build_w3_b_feature_panel
   pysrc.meta.allocator_benchmark.w3_b_pandas_ta.apply_w3_b_warmup_policy
   pysrc.meta.allocator_benchmark.w3_b_pandas_ta.run_w3_b_ta_child_policies


Module Contents
---------------

.. py:data:: W3_B_PANDAS_TA_DIR
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: W3A_FROZEN_BASELINES
   :type:  Final[dict[str, float | int]]
   :value: Ellipsis


.. py:data:: LOG
   :type:  Any

.. py:class:: W3BPandasTARunResult

   .. py:attribute:: indicator_diagnostics_report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: child_policy_report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: router_report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: summary_path
      :type:  Path
      :value: Ellipsis



.. py:function:: run_w3_b_pandas_ta_experiment(*, source_path = ..., source_panel = ..., output_dir = ..., config = ...)

.. py:function:: build_w3_b_feature_panel(surface_rows, *, surface_id, config)

.. py:function:: apply_w3_b_warmup_policy(rows, *, active_indicators, provider_warmup)

.. py:function:: run_w3_b_ta_child_policies(rows, *, active_indicators, orientations, config, w2_config = ...)

