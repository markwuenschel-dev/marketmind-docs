pysrc.ops.dataprep_io
=====================

.. py:module:: pysrc.ops.dataprep_io


Attributes
----------

.. autoapisummary::

   pysrc.ops.dataprep_io.psutil
   pysrc.ops.dataprep_io.pynvml


Functions
---------

.. autoapisummary::

   pysrc.ops.dataprep_io.maybe_mem_info
   pysrc.ops.dataprep_io.resolve_workers
   pysrc.ops.dataprep_io.call_with_timeout
   pysrc.ops.dataprep_io.stage_with_guard
   pysrc.ops.dataprep_io.adaptive_map


Module Contents
---------------

.. py:data:: psutil
   :type:  Any

.. py:data:: pynvml
   :type:  Any

.. py:function:: maybe_mem_info(_ctx = ...)

.. py:function:: resolve_workers(val)

.. py:function:: call_with_timeout(fn, timeout_s)

.. py:function:: stage_with_guard(name, fn, *, timeout_s = ..., run_cfg, run_id, metrics, logger, ConfigError, DataPrepError, get_metrics_fn)

.. py:function:: adaptive_map(fn, items, kind = ..., max_workers = ...)

