pysrc.meta.reptile_proxy_alignment
==================================

.. py:module:: pysrc.meta.reptile_proxy_alignment


Attributes
----------

.. autoapisummary::

   pysrc.meta.reptile_proxy_alignment.LOG


Functions
---------

.. autoapisummary::

   pysrc.meta.reptile_proxy_alignment.partition_training_and_heldout
   pysrc.meta.reptile_proxy_alignment.compute_proxy_loss
   pysrc.meta.reptile_proxy_alignment.run_alignment_arm
   pysrc.meta.reptile_proxy_alignment.run_proxy_alignment
   pysrc.meta.reptile_proxy_alignment.emit_proxy_alignment_report_json
   pysrc.meta.reptile_proxy_alignment.load_proxy_alignment_report_json
   pysrc.meta.reptile_proxy_alignment.recompute_content_hash_from_document


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:function:: partition_training_and_heldout(pool, *, heldout_partition_seed)

.. py:function:: compute_proxy_loss(proxy_kind, theta_adapted, task, *, soft_rank_temperature = ...)

.. py:function:: run_alignment_arm(config, arm, theta_initial, training_tasks, heldout_tasks, rng)

.. py:function:: run_proxy_alignment(config)

.. py:function:: emit_proxy_alignment_report_json(path, report)

.. py:function:: load_proxy_alignment_report_json(path)

.. py:function:: recompute_content_hash_from_document(doc)

