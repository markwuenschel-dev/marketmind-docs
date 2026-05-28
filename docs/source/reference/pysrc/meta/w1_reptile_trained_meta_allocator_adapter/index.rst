pysrc.meta.w1_reptile_trained_meta_allocator_adapter
====================================================

.. py:module:: pysrc.meta.w1_reptile_trained_meta_allocator_adapter


Attributes
----------

.. autoapisummary::

   pysrc.meta.w1_reptile_trained_meta_allocator_adapter.W1_LEARNED_CHECKPOINT_SCHEMA_V2
   pysrc.meta.w1_reptile_trained_meta_allocator_adapter.GOVERNED_W1_CHECKPOINT_TRAINED_BY_RUNNERS


Classes
-------

.. autoapisummary::

   pysrc.meta.w1_reptile_trained_meta_allocator_adapter.ReptileTrainedMetaAllocatorAdapter


Functions
---------

.. autoapisummary::

   pysrc.meta.w1_reptile_trained_meta_allocator_adapter.w1_learned_checkpoint_body_for_content_hash


Module Contents
---------------

.. py:data:: W1_LEARNED_CHECKPOINT_SCHEMA_V2
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: GOVERNED_W1_CHECKPOINT_TRAINED_BY_RUNNERS
   :type:  Final[frozenset[str]]
   :value: Ellipsis


.. py:function:: w1_learned_checkpoint_body_for_content_hash(raw)

.. py:class:: ReptileTrainedMetaAllocatorAdapter(checkpoint_path, *, expected_signal_set_version, expected_training_task_pool_hash, expected_training_data_fingerprint, expected_training_splits_fingerprint)

   .. py:method:: model_state_hash()


   .. py:method:: checkpoint_path()


   .. py:method:: governed_checkpoint_lineage_verified()


   .. py:method:: validated_checkpoint_metadata_block()


   .. py:method:: predict_query_scores(task, *, fold_index)


