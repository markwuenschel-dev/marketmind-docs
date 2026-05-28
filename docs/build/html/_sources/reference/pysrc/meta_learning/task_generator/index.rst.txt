pysrc.meta_learning.task_generator
==================================

.. py:module:: pysrc.meta_learning.task_generator


Attributes
----------

.. autoapisummary::

   pysrc.meta_learning.task_generator.LOG
   pysrc.meta_learning.task_generator.TASK_ID_HMAC_KEY_VERSION
   pysrc.meta_learning.task_generator.TASK_ID_HMAC_KEY_MATERIAL


Classes
-------

.. autoapisummary::

   pysrc.meta_learning.task_generator.MetaTask


Functions
---------

.. autoapisummary::

   pysrc.meta_learning.task_generator.compute_task_id
   pysrc.meta_learning.task_generator.derive_signal_ids_hash
   pysrc.meta_learning.task_generator.build_meta_task
   pysrc.meta_learning.task_generator.meta_task_to_task_manifest_input
   pysrc.meta_learning.task_generator.meta_task_to_record
   pysrc.meta_learning.task_generator.meta_task_from_record


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:data:: TASK_ID_HMAC_KEY_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: TASK_ID_HMAC_KEY_MATERIAL
   :type:  Final[bytes]
   :value: Ellipsis


.. py:function:: compute_task_id(*, regime_id, t0, t1, signal_ids_hash)

.. py:function:: derive_signal_ids_hash(*, signal_ids, signal_mask)

.. py:class:: MetaTask

   .. py:attribute:: task_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: regime_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: regime_class
      :type:  str
      :value: Ellipsis



   .. py:attribute:: regime_embedding
      :type:  tuple[float, Ellipsis] | None
      :value: Ellipsis



   .. py:attribute:: support_set
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: query_set
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: horizon
      :type:  int
      :value: Ellipsis



   .. py:attribute:: signal_ids
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: signal_mask
      :type:  tuple[bool, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: signal_set_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: signal_ids_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: pit_boundary
      :type:  str
      :value: Ellipsis



   .. py:attribute:: t0
      :type:  str
      :value: Ellipsis



   .. py:attribute:: t1
      :type:  str
      :value: Ellipsis



   .. py:attribute:: active_k
      :type:  int
      :value: Ellipsis



.. py:function:: build_meta_task(*, regime_id, regime_class, regime_embedding, support_set, query_set, horizon, signal_ids, signal_mask, signal_set_version, t0, t1, purge_window, embargo_window, pit_boundary = ...)

.. py:function:: meta_task_to_task_manifest_input(task)

.. py:function:: meta_task_to_record(task)

.. py:function:: meta_task_from_record(record)

