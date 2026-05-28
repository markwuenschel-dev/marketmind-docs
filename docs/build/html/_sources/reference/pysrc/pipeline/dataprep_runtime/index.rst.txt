pysrc.pipeline.dataprep_runtime
===============================

.. py:module:: pysrc.pipeline.dataprep_runtime


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.dataprep_runtime.pd
   pysrc.pipeline.dataprep_runtime.pl
   pysrc.pipeline.dataprep_runtime.dd
   pysrc.pipeline.dataprep_runtime.np
   pysrc.pipeline.dataprep_runtime.yaml
   pysrc.pipeline.dataprep_runtime.pynvml
   pysrc.pipeline.dataprep_runtime.psutil
   pysrc.pipeline.dataprep_runtime.BackendLiteral
   pysrc.pipeline.dataprep_runtime.logger
   pysrc.pipeline.dataprep_runtime.run_cfg


Exceptions
----------

.. autoapisummary::

   pysrc.pipeline.dataprep_runtime.DataPrepError
   pysrc.pipeline.dataprep_runtime.ConfigError
   pysrc.pipeline.dataprep_runtime.DataValidationError


Classes
-------

.. autoapisummary::

   pysrc.pipeline.dataprep_runtime.DataFrameAdapter
   pysrc.pipeline.dataprep_runtime.ConfigProxy
   pysrc.pipeline.dataprep_runtime.BackendManager
   pysrc.pipeline.dataprep_runtime.Evolver
   pysrc.pipeline.dataprep_runtime.OrchestratorConfig
   pysrc.pipeline.dataprep_runtime.DataPrepOrchestrator
   pysrc.pipeline.dataprep_runtime.Cache


Functions
---------

.. autoapisummary::

   pysrc.pipeline.dataprep_runtime.expand_grid
   pysrc.pipeline.dataprep_runtime.stage
   pysrc.pipeline.dataprep_runtime.run_dataprep
   pysrc.pipeline.dataprep_runtime.run_dataprep_from_path


Module Contents
---------------

.. py:data:: pd
   :type:  Any

.. py:data:: pl
   :type:  Any

.. py:data:: dd
   :type:  Any

.. py:data:: np
   :type:  Any

.. py:data:: yaml
   :type:  Any

.. py:data:: pynvml
   :type:  Any

.. py:data:: psutil
   :type:  Any

.. py:data:: BackendLiteral
   :type:  Any

.. py:function:: expand_grid(base, constraints = ...)

.. py:function:: stage(name = ..., timeout_s = ...)

.. py:class:: DataFrameAdapter(df)

   .. py:method:: shape()


   .. py:method:: columns()


   .. py:method:: hash()


.. py:class:: ConfigProxy(data)

   .. py:method:: get(path, default = ...)


.. py:class:: BackendManager

   .. py:attribute:: HAS_POLARS
      :type:  Any


   .. py:attribute:: HAS_PANDAS
      :type:  Any


   .. py:attribute:: HAS_DASK
      :type:  Any


   .. py:method:: require_polars()


.. py:class:: Evolver(cache, version_tag, code_id)

   .. py:method:: load(context_hash)


   .. py:method:: save(context_hash, trials)


   .. py:method:: shrink_grid(grid, prior_trials, quantile = ...)


.. py:data:: logger
   :type:  Any

.. py:data:: run_cfg
   :type:  Any

.. py:exception:: DataPrepError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: ConfigError

   Bases: :py:obj:`DataPrepError`


   Common base class for all non-exit exceptions.


.. py:exception:: DataValidationError

   Bases: :py:obj:`DataPrepError`


   Common base class for all non-exit exceptions.


.. py:class:: OrchestratorConfig

   .. py:attribute:: per_symbol_parallelism
      :type:  Union[int, str]
      :value: Ellipsis



   .. py:attribute:: gpu_slots
      :type:  Union[int, str]
      :value: Ellipsis



   .. py:attribute:: lazy
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: date_chunk_size
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: cache_version_tag
      :type:  str
      :value: Ellipsis



   .. py:attribute:: cache_checkpoints
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: search_mode
      :type:  str
      :value: Ellipsis



   .. py:attribute:: n_trials
      :type:  int
      :value: Ellipsis



   .. py:attribute:: metric_name
      :type:  str
      :value: Ellipsis



.. py:class:: DataPrepOrchestrator(run_cfg, cache = ..., backtest_metric = ..., entry_point_groups = ...)

   .. py:attribute:: run_id
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: cfg
      :type:  Dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: run_cfg
      :type:  Dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: run_cfg_raw
      :type:  Dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: code_id
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: ocfg
      :type:  OrchestratorConfig
      :value: Ellipsis



   .. py:attribute:: cache
      :type:  Any
      :value: Ellipsis



   .. py:attribute:: backtest_metric
      :type:  Optional[Callable[[Any, Any, Mapping[str, Any], Mapping[str, Any]], float]]
      :value: Ellipsis



   .. py:method:: run()


   .. py:method:: preprocess_multi_symbol(clean_df, preset, params)


   .. py:method:: adaptive_map(fn, items, kind = ..., max_workers = ...)


.. py:function:: run_dataprep(run_cfg, backtest_metric = ...)

.. py:function:: run_dataprep_from_path(run_cfg_path, backtest_metric)

.. py:class:: Cache

   .. py:method:: save_df(key, df)


