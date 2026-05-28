pysrc.meta.w1_real_task_pool
============================

.. py:module:: pysrc.meta.w1_real_task_pool


Attributes
----------

.. autoapisummary::

   pysrc.meta.w1_real_task_pool.LOG
   pysrc.meta.w1_real_task_pool.W1RealPoolEvidenceMode


Classes
-------

.. autoapisummary::

   pysrc.meta.w1_real_task_pool.W1RealPoolBuildError
   pysrc.meta.w1_real_task_pool.UniverseResolver
   pysrc.meta.w1_real_task_pool.W1RealPoolConfig
   pysrc.meta.w1_real_task_pool.W1RealTaskPoolOutcome


Functions
---------

.. autoapisummary::

   pysrc.meta.w1_real_task_pool.w1_meta_tasks_as_manifest_inputs
   pysrc.meta.w1_real_task_pool.w1_support_mean_log_return_net_from_pool
   pysrc.meta.w1_real_task_pool.build_w1_real_task_pool


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:data:: W1RealPoolEvidenceMode
   :type:  Any

.. py:class:: W1RealPoolBuildError

   Bases: :py:obj:`DataPreconditionError`


.. py:function:: w1_meta_tasks_as_manifest_inputs(tasks)

.. py:class:: UniverseResolver

   Bases: :py:obj:`Protocol`


.. py:class:: W1RealPoolConfig

   .. py:attribute:: data_view
      :type:  DataViewLike
      :value: Ellipsis



   .. py:attribute:: encoder
      :type:  ContextEncoderProtocol
      :value: Ellipsis



   .. py:attribute:: labeler
      :type:  RegimeLabeler
      :value: Ellipsis



   .. py:attribute:: bocpd_config
      :type:  BOCPDConfig
      :value: Ellipsis



   .. py:attribute:: universe_resolver
      :type:  UniverseResolver
      :value: Ellipsis



   .. py:attribute:: signal_set_version
      :type:  int
      :value: Ellipsis



   .. py:attribute:: construction_seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: start_ts
      :type:  str
      :value: Ellipsis



   .. py:attribute:: end_ts
      :type:  str
      :value: Ellipsis



   .. py:attribute:: universe_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: symbols
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: regime_label_source
      :type:  Literal['emitted_bocpd', 'labeler_from_dataview']
      :value: Ellipsis



   .. py:attribute:: registry_jsonl_path
      :type:  Path | None
      :value: Ellipsis



   .. py:attribute:: bucket_minimums
      :type:  Mapping[str, int]
      :value: Ellipsis



   .. py:attribute:: gfc_holdout_start
      :type:  str
      :value: Ellipsis



   .. py:attribute:: gfc_holdout_end
      :type:  str
      :value: Ellipsis



   .. py:attribute:: covid_holdout_start
      :type:  str
      :value: Ellipsis



   .. py:attribute:: covid_holdout_end
      :type:  str
      :value: Ellipsis



   .. py:attribute:: calendar_origin
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: episode_stride_days
      :type:  int
      :value: Ellipsis



   .. py:attribute:: fields
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: spread_bps
      :type:  float
      :value: Ellipsis



   .. py:attribute:: slippage_bps
      :type:  float
      :value: Ellipsis



   .. py:attribute:: borrow_rate_ann
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_calendar_bars
      :type:  int | None
      :value: Ellipsis



   .. py:attribute:: evidence_mode
      :type:  W1RealPoolEvidenceMode
      :value: Ellipsis



   .. py:attribute:: test_fixture_log_returns
      :type:  NDArray[np.float64] | None
      :value: Ellipsis



.. py:class:: W1RealTaskPoolOutcome

   .. py:attribute:: tasks
      :type:  tuple[MetaTask, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: task_pool_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: diagnostics
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: holdout_declaration
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: registry
      :type:  TaskRegistry
      :value: Ellipsis



   .. py:attribute:: task_query_targets_net
      :type:  tuple[tuple[str, float], Ellipsis]
      :value: Ellipsis



   .. py:attribute:: task_support_mean_log_return_net
      :type:  tuple[tuple[str, float], Ellipsis]
      :value: Ellipsis



   .. py:attribute:: data_fingerprint
      :type:  str | None
      :value: Ellipsis



.. py:function:: w1_support_mean_log_return_net_from_pool(outcome)

.. py:function:: build_w1_real_task_pool(config)

