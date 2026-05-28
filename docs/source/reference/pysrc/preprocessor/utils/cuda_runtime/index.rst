pysrc.preprocessor.utils.cuda_runtime
=====================================

.. py:module:: pysrc.preprocessor.utils.cuda_runtime


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.utils.cuda_runtime.logger


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.utils.cuda_runtime.GpuCapabilities
   pysrc.preprocessor.utils.cuda_runtime.StreamFactory
   pysrc.preprocessor.utils.cuda_runtime.StreamPool


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.utils.cuda_runtime.capabilities
   pysrc.preprocessor.utils.cuda_runtime.init_rmm_pool
   pysrc.preprocessor.utils.cuda_runtime.pinned_array
   pysrc.preprocessor.utils.cuda_runtime.device_synchronize
   pysrc.preprocessor.utils.cuda_runtime.maybe_stream


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:class:: GpuCapabilities

   .. py:attribute:: has_cuda
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: has_rmm
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: has_cudf
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: has_polars_gpu
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: has_nvtabular
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: has_kvikio
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: device_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: compute_capability
      :type:  Optional[str]
      :value: Ellipsis



.. py:function:: capabilities()

.. py:function:: init_rmm_pool(pool_size = ..., managed_memory = ..., async_alloc = ..., logging = ..., release_threshold = ...)

.. py:class:: StreamFactory

   .. py:method:: create()


.. py:class:: StreamPool(size = ..., non_blocking = ...)

   .. py:method:: lease()


.. py:function:: pinned_array(shape, dtype = ...)

.. py:function:: device_synchronize()

.. py:function:: maybe_stream(stream)

