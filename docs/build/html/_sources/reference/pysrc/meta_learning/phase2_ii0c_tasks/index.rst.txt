pysrc.meta_learning.phase2_ii0c_tasks
=====================================

.. py:module:: pysrc.meta_learning.phase2_ii0c_tasks


Attributes
----------

.. autoapisummary::

   pysrc.meta_learning.phase2_ii0c_tasks.II0C_SCHEMATIC_VERSION


Classes
-------

.. autoapisummary::

   pysrc.meta_learning.phase2_ii0c_tasks.II0CMetaTaskRequest
   pysrc.meta_learning.phase2_ii0c_tasks.II0CMetaTaskPayload


Functions
---------

.. autoapisummary::

   pysrc.meta_learning.phase2_ii0c_tasks.build_ii0c_meta_task_payload
   pysrc.meta_learning.phase2_ii0c_tasks.build_ii0c_signal_surface
   pysrc.meta_learning.phase2_ii0c_tasks.build_ii0c_task_inputs
   pysrc.meta_learning.phase2_ii0c_tasks.build_ii0c_meta_task
   pysrc.meta_learning.phase2_ii0c_tasks.build_ii0c_task_manifest_input


Module Contents
---------------

.. py:data:: II0C_SCHEMATIC_VERSION
   :type:  str
   :value: Ellipsis


.. py:class:: II0CMetaTaskRequest

   .. py:attribute:: regime_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: regime_class
      :type:  str
      :value: Ellipsis



   .. py:attribute:: support_set
      :type:  Sequence[pd.Timestamp | str]
      :value: Ellipsis



   .. py:attribute:: query_set
      :type:  Sequence[pd.Timestamp | str]
      :value: Ellipsis



   .. py:attribute:: horizon
      :type:  int
      :value: Ellipsis



   .. py:attribute:: signal_bindings
      :type:  Mapping[int, str]
      :value: Ellipsis



   .. py:attribute:: signal_set_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: regime_embedding
      :type:  Sequence[float] | None
      :value: Ellipsis



   .. py:attribute:: purge_window
      :type:  pd.Timedelta
      :value: Ellipsis



   .. py:attribute:: embargo_window
      :type:  pd.Timedelta
      :value: Ellipsis



   .. py:attribute:: pit_boundary
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: t0
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: t1
      :type:  str | None
      :value: Ellipsis



.. py:class:: II0CMetaTaskPayload

   .. py:attribute:: meta_task
      :type:  MetaTask
      :value: Ellipsis



   .. py:attribute:: task_manifest_input
      :type:  TaskManifestTaskInput
      :value: Ellipsis



   .. py:attribute:: task_record
      :type:  dict[str, object]
      :value: Ellipsis



.. py:function:: build_ii0c_meta_task_payload(request)

.. py:function:: build_ii0c_signal_surface(slot_to_signal_id, *, max_signals = ...)

.. py:function:: build_ii0c_task_inputs(*, regime_id, regime_class, regime_embedding, support_set, query_set, horizon, slot_to_signal_id, signal_set_version, t0, t1, purge_window, embargo_window, pit_boundary = ...)

.. py:function:: build_ii0c_meta_task(*, regime_id, regime_class, regime_embedding, support_set, query_set, horizon, slot_to_signal_id, signal_set_version, t0, t1, purge_window, embargo_window, pit_boundary = ...)

.. py:function:: build_ii0c_task_manifest_input(*, regime_id, regime_class, regime_embedding, support_set, query_set, horizon, slot_to_signal_id, signal_set_version, t0, t1, purge_window, embargo_window, pit_boundary = ...)

