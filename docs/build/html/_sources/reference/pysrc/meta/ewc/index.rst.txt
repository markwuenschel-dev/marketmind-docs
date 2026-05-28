pysrc.meta.ewc
==============

.. py:module:: pysrc.meta.ewc


Attributes
----------

.. autoapisummary::

   pysrc.meta.ewc.LOG


Functions
---------

.. autoapisummary::

   pysrc.meta.ewc.compute_diagonal_fisher
   pysrc.meta.ewc.apply_ewc_correction
   pysrc.meta.ewc.pretrain_theta_meta
   pysrc.meta.ewc.run_from_scratch_arm
   pysrc.meta.ewc.run_ewc_arm
   pysrc.meta.ewc.run_ewc_sweep
   pysrc.meta.ewc.emit_ewc_forgetting_report_json
   pysrc.meta.ewc.load_ewc_forgetting_report_json
   pysrc.meta.ewc.recompute_content_hash_from_document


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:function:: compute_diagonal_fisher(theta, tasks, inner_cfg, rng)

.. py:function:: apply_ewc_correction(theta, theta_anchor, fisher, lambda_ewc)

.. py:function:: pretrain_theta_meta(config, historical_tasks, rng)

.. py:function:: run_from_scratch_arm(config, all_available_tasks_by_step, heldout_tasks, fresh_tasks, rng)

.. py:function:: run_ewc_arm(lambda_ewc, theta_initial, fisher, theta_anchor, config, update_task_batches, heldout_tasks, fresh_tasks, rng)

.. py:function:: run_ewc_sweep(config)

.. py:function:: emit_ewc_forgetting_report_json(path, report)

.. py:function:: load_ewc_forgetting_report_json(path)

.. py:function:: recompute_content_hash_from_document(doc)

