pysrc.preprocessor.graph.backends.cudf
======================================

.. py:module:: pysrc.preprocessor.graph.backends.cudf


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.graph.backends.cudf.logger


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.graph.backends.cudf.CuDFExecutor


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.graph.backends.cudf.robust_scaler_cudf
   pysrc.preprocessor.graph.backends.cudf.feature_returns_cudf
   pysrc.preprocessor.graph.backends.cudf.feature_sma_cudf
   pysrc.preprocessor.graph.backends.cudf.feature_rsi_cudf
   pysrc.preprocessor.graph.backends.cudf.data_load_csv_cudf


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:function:: robust_scaler_cudf(ir, gdf, group_by = ..., **_)

.. py:class:: CuDFExecutor(*, pool_size = ..., to_torch = ...)

   Bases: :py:obj:`Executor`


   .. py:method:: read_parquet(path, columns = ..., byte_range = ...)


   .. py:method:: execute(compiled_plan, df)


.. py:function:: feature_returns_cudf(ir, gdf, **_)

.. py:function:: feature_sma_cudf(ir, gdf, **_)

.. py:function:: feature_rsi_cudf(ir, gdf, **_)

.. py:function:: data_load_csv_cudf(ir, gdf, **_)

