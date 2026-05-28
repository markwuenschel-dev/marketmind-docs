pysrc.meta_learning.contracts.task_registry
===========================================

.. py:module:: pysrc.meta_learning.contracts.task_registry


Exceptions
----------

.. autoapisummary::

   pysrc.meta_learning.contracts.task_registry.TaskRegistryError
   pysrc.meta_learning.contracts.task_registry.TaskNotFoundError
   pysrc.meta_learning.contracts.task_registry.TaskRegistryDuplicateError


Classes
-------

.. autoapisummary::

   pysrc.meta_learning.contracts.task_registry.TaskRegistryProtocol


Module Contents
---------------

.. py:exception:: TaskRegistryError(message, *, details = ...)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: TaskNotFoundError(message, *, details = ...)

   Bases: :py:obj:`TaskRegistryError`


   Common base class for all non-exit exceptions.


.. py:exception:: TaskRegistryDuplicateError(message, *, details = ...)

   Bases: :py:obj:`TaskRegistryError`


   Common base class for all non-exit exceptions.


.. py:class:: TaskRegistryProtocol

   Bases: :py:obj:`Protocol`


   .. py:attribute:: CONTRACT_VERSION
      :type:  ClassVar[str]
      :value: Ellipsis



   .. py:method:: append(task)


   .. py:method:: get(task_id)


   .. py:method:: query(regime_id = ..., since = ...)


