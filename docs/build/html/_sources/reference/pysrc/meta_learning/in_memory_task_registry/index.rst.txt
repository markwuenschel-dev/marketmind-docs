pysrc.meta_learning.in_memory_task_registry
===========================================

.. py:module:: pysrc.meta_learning.in_memory_task_registry


Classes
-------

.. autoapisummary::

   pysrc.meta_learning.in_memory_task_registry.AppendOnlyTaskRegistry


Module Contents
---------------

.. py:class:: AppendOnlyTaskRegistry

   .. py:attribute:: CONTRACT_VERSION
      :type:  ClassVar[str]
      :value: Ellipsis



   .. py:method:: append(task)


   .. py:method:: get(task_id)


   .. py:method:: get_by_stable(*, regime_id, t0)


   .. py:method:: query(regime_id = ..., since = ...)


   .. py:method:: to_records()


