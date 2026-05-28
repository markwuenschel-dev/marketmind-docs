pysrc.meta.task
===============

.. py:module:: pysrc.meta.task


Attributes
----------

.. autoapisummary::

   pysrc.meta.task.META_TASK_SCHEMA_VERSION


Classes
-------

.. autoapisummary::

   pysrc.meta.task.MetaTask


Module Contents
---------------

.. py:data:: META_TASK_SCHEMA_VERSION
   :type:  str
   :value: Ellipsis


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



   .. py:attribute:: t0
      :type:  str
      :value: Ellipsis



   .. py:attribute:: t1
      :type:  str
      :value: Ellipsis



   .. py:attribute:: pit_boundary
      :type:  str
      :value: Ellipsis



   .. py:attribute:: support_set
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: query_set
      :type:  tuple[str, Ellipsis]
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



   .. py:attribute:: horizon
      :type:  int
      :value: Ellipsis



   .. py:attribute:: active_k
      :type:  int
      :value: Ellipsis



   .. py:attribute:: regime_embedding
      :type:  Optional[NDArray[np.floating[Any]]]
      :value: Ellipsis



   .. py:method:: has_regime_embedding()


   .. py:method:: as_record()


