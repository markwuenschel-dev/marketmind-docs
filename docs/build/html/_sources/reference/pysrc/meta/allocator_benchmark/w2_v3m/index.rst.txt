pysrc.meta.allocator_benchmark.w2_v3m
=====================================

.. py:module:: pysrc.meta.allocator_benchmark.w2_v3m


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w2_v3m.W2_V3M_DATA_PROVIDER
   pysrc.meta.allocator_benchmark.w2_v3m.W2_V3M_DATASET_NAME
   pysrc.meta.allocator_benchmark.w2_v3m.W2_V3M_DEFAULT_SOURCE
   pysrc.meta.allocator_benchmark.w2_v3m.W2_V3M_DEFAULT_OUTPUT_ROOT
   pysrc.meta.allocator_benchmark.w2_v3m.W2_V3M_DEFAULT_TOP_CONTRIBUTORS
   pysrc.meta.allocator_benchmark.w2_v3m.W2_V3M_SIGNAL_IDS
   pysrc.meta.allocator_benchmark.w2_v3m.W2_V3M_CHILD_POLICY_IDS
   pysrc.meta.allocator_benchmark.w2_v3m.W2_V3M_ROUTER_IDS


Classes
-------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w2_v3m.W2V3MConfig
   pysrc.meta.allocator_benchmark.w2_v3m.W2V3MSurface
   pysrc.meta.allocator_benchmark.w2_v3m.W2V3MRunResult


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w2_v3m.load_w2_v3m_adjusted_panel
   pysrc.meta.allocator_benchmark.w2_v3m.build_w2_v3m_inventory
   pysrc.meta.allocator_benchmark.w2_v3m.build_w2_v3m_surfaces
   pysrc.meta.allocator_benchmark.w2_v3m.build_w2_v3m_signal_rows_for_surface
   pysrc.meta.allocator_benchmark.w2_v3m.apply_w2_v3m_walk_forward_folds
   pysrc.meta.allocator_benchmark.w2_v3m.run_w2_v3m_experiment
   pysrc.meta.allocator_benchmark.w2_v3m.run_default_w2_v3m_experiment


Module Contents
---------------

.. py:data:: W2_V3M_DATA_PROVIDER
   :type:  Any

.. py:data:: W2_V3M_DATASET_NAME
   :type:  Any

.. py:data:: W2_V3M_DEFAULT_SOURCE
   :type:  Any

.. py:data:: W2_V3M_DEFAULT_OUTPUT_ROOT
   :type:  Any

.. py:data:: W2_V3M_DEFAULT_TOP_CONTRIBUTORS
   :type:  tuple[str, Ellipsis]
   :value: Ellipsis


.. py:data:: W2_V3M_SIGNAL_IDS
   :type:  tuple[str, Ellipsis]
   :value: Ellipsis


.. py:data:: W2_V3M_CHILD_POLICY_IDS
   :type:  tuple[str, Ellipsis]
   :value: Ellipsis


.. py:data:: W2_V3M_ROUTER_IDS
   :type:  tuple[str, Ellipsis]
   :value: Ellipsis


.. py:class:: W2V3MConfig

   .. py:attribute:: horizon
      :type:  int
      :value: Ellipsis



   .. py:attribute:: base_cost
      :type:  float
      :value: Ellipsis



   .. py:attribute:: liquidity_floor
      :type:  float
      :value: Ellipsis



   .. py:attribute:: top_k
      :type:  int
      :value: Ellipsis



   .. py:attribute:: max_gross_exposure
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_single_instrument_weight
      :type:  float
      :value: Ellipsis



   .. py:attribute:: score_threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: score_higher_is_better
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: corporate_action_event_window_days
      :type:  int
      :value: Ellipsis



   .. py:attribute:: save_signal_rows
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: use_xgboost
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: xgboost_train_row_cap
      :type:  int
      :value: Ellipsis



   .. py:attribute:: xgboost_predict_batch_rows
      :type:  int
      :value: Ellipsis



   .. py:attribute:: exclude_earliest_train_calendar_year
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: panel_coalesce_float32
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: release_input_panel_after_surfaces
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: repair_reload_panel_after_surface_prep
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: w3_audit_spill_intermediates
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: w3_audit_skip_shuffled_label_rerun
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: w3_audit_force_heavy_surface_b_checks
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: workers
      :type:  int
      :value: Ellipsis



   .. py:attribute:: xgboost_n_jobs
      :type:  int
      :value: Ellipsis



   .. py:attribute:: seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: timestamp_utc
      :type:  str
      :value: Ellipsis



.. py:class:: W2V3MSurface

   .. py:attribute:: rows
      :type:  pd.DataFrame
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  dict[str, object]
      :value: Ellipsis



.. py:class:: W2V3MRunResult

   .. py:attribute:: inventory
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: surface_summary
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



.. py:function:: load_w2_v3m_adjusted_panel(source_path, *, workers = ..., panel_coalesce_float32 = ..., loader_backend = ...)

.. py:function:: build_w2_v3m_inventory(panel, *, source_path)

.. py:function:: build_w2_v3m_surfaces(panel, config = ...)

.. py:function:: build_w2_v3m_signal_rows_for_surface(surface_rows, surface_id, config = ...)

.. py:function:: apply_w2_v3m_walk_forward_folds(rows, *, exclude_earliest_train_calendar_year = ...)

.. py:function:: run_w2_v3m_experiment(*, source_path = ..., source_panel = ..., output_root = ..., config = ...)

.. py:function:: run_default_w2_v3m_experiment()

