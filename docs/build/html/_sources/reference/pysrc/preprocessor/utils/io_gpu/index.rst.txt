pysrc.preprocessor.utils.io_gpu
===============================

.. py:module:: pysrc.preprocessor.utils.io_gpu


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.utils.io_gpu.logger
   pysrc.preprocessor.utils.io_gpu.cudf
   pysrc.preprocessor.utils.io_gpu.polars
   pysrc.preprocessor.utils.io_gpu.NVCOMP_CODECS
   pysrc.preprocessor.utils.io_gpu.Frame


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.utils.io_gpu.ParquetOptions


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.utils.io_gpu.read_parquet_gpu
   pysrc.preprocessor.utils.io_gpu.write_parquet_gpu


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:data:: cudf
   :type:  Any

.. py:data:: polars
   :type:  Any

.. py:data:: NVCOMP_CODECS
   :type:  Any

.. py:data:: Frame
   :type:  Any

.. py:class:: ParquetOptions

   .. py:attribute:: columns
      :type:  Optional[list[str]]
      :value: Ellipsis



   .. py:attribute:: compression
      :type:  Optional[Literal['snappy', 'zstd', 'lz4', 'none']]
      :value: Ellipsis



   .. py:attribute:: filters
      :type:  Optional[Any]
      :value: Ellipsis



   .. py:attribute:: engine
      :type:  Optional[Literal['cudf', 'polars']]
      :value: Ellipsis



.. py:function:: read_parquet_gpu(path, opts = ...)

.. py:function:: write_parquet_gpu(df, path, opts = ..., **kwargs)

