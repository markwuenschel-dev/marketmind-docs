pysrc.preprocessor.utils.torch_bridge
=====================================

.. py:module:: pysrc.preprocessor.utils.torch_bridge


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.utils.torch_bridge.logger


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.utils.torch_bridge.TorchBatch
   pysrc.preprocessor.utils.torch_bridge.BackendBridge
   pysrc.preprocessor.utils.torch_bridge.CuDFBridge
   pysrc.preprocessor.utils.torch_bridge.PolarsBridge


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.utils.torch_bridge.bridge_factory
   pysrc.preprocessor.utils.torch_bridge.profile_evolve
   pysrc.preprocessor.utils.torch_bridge.to_torch_batch
   pysrc.preprocessor.utils.torch_bridge.set_amp_precision
   pysrc.preprocessor.utils.torch_bridge.seed_everything


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:class:: TorchBatch

   .. py:attribute:: tensors
      :type:  Dict[str, torch.Tensor]
      :value: Ellipsis



   .. py:attribute:: lengths
      :type:  Optional[torch.Tensor]
      :value: Ellipsis



   .. py:attribute:: meta
      :type:  Dict[str, Any]
      :value: Ellipsis



.. py:class:: BackendBridge

   Bases: :py:obj:`ABC`


   .. py:method:: to_torch(df, cols, dtypes, include_lengths)


.. py:class:: CuDFBridge

   Bases: :py:obj:`BackendBridge`


   .. py:method:: to_torch(df, cols, dtypes, include_lengths)


.. py:class:: PolarsBridge

   Bases: :py:obj:`BackendBridge`


   .. py:method:: to_torch(df, cols, dtypes, include_lengths)


.. py:function:: bridge_factory(df)

.. py:function:: profile_evolve(func)

.. py:function:: to_torch_batch(df, cols, dtypes = ..., include_lengths = ...)

.. py:function:: set_amp_precision(precision = ...)

.. py:function:: seed_everything(seed = ...)

