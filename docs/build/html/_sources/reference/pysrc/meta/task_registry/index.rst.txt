pysrc.meta.task_registry
========================

.. py:module:: pysrc.meta.task_registry


Attributes
----------

.. autoapisummary::

   pysrc.meta.task_registry.LOG


Classes
-------

.. autoapisummary::

   pysrc.meta.task_registry.DurableTaskStore
   pysrc.meta.task_registry.NullDurableStore
   pysrc.meta.task_registry.JsonLinesDurableStore
   pysrc.meta.task_registry.TaskRegistry


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:class:: DurableTaskStore

   Bases: :py:obj:`Protocol`


   .. py:method:: persist(task_id, record)


   .. py:method:: iter_records()


.. py:class:: NullDurableStore

   .. py:method:: persist(task_id, record)


   .. py:method:: iter_records()


.. py:class:: JsonLinesDurableStore(path)

   .. py:method:: path()


   .. py:method:: persist(task_id, record)


   .. py:method:: iter_records()


.. py:class:: TaskRegistry(durable_store = ...)

   Bases: :py:obj:`TaskRegistryProtocol`


   .. py:attribute:: CONTRACT_VERSION
      :type:  ClassVar[str]
      :value: Ellipsis



   .. py:method:: append(task)


   .. py:method:: get(task_id)


   .. py:method:: get_by_stable(*, regime_id, t0)


   .. py:method:: contains_stable(*, regime_id, t0)


   .. py:method:: query(regime_id = ..., since = ...)


   .. py:method:: iter_stable_keys()


   .. py:method:: durable_store()


