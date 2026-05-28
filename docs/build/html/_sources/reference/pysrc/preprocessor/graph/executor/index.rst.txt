pysrc.preprocessor.graph.executor
=================================

.. py:module:: pysrc.preprocessor.graph.executor


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.graph.executor.logger
   pysrc.preprocessor.graph.executor.Engine


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.graph.executor.Executor
   pysrc.preprocessor.graph.executor.PolarsExecutor
   pysrc.preprocessor.graph.executor.CuDFExecutor
   pysrc.preprocessor.graph.executor.ExecutorFactory


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:data:: Engine
   :type:  Any

.. py:class:: Executor(backend, cache_size = ...)

   Bases: :py:obj:`abc.ABC`


   .. py:method:: execute(plan, data, group_by)


   .. py:method:: evolve(threshold = ...)


.. py:class:: PolarsExecutor(engine_pref = ...)

   Bases: :py:obj:`Executor`


   .. py:method:: execute(plan, data, group_by)


.. py:class:: CuDFExecutor(pool_size = ...)

   Bases: :py:obj:`Executor`


   .. py:method:: execute(plan, data, group_by)


.. py:class:: ExecutorFactory

   .. py:method:: register(backend, executor_cls)


   .. py:method:: create(backend = ..., **kwargs)


