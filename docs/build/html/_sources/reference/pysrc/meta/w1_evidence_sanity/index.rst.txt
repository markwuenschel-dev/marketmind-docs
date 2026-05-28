pysrc.meta.w1_evidence_sanity
=============================

.. py:module:: pysrc.meta.w1_evidence_sanity


Classes
-------

.. autoapisummary::

   pysrc.meta.w1_evidence_sanity.W1FoldSanityDiag


Functions
---------

.. autoapisummary::

   pysrc.meta.w1_evidence_sanity.w1_evidence_sanity_pool_target_stats
   pysrc.meta.w1_evidence_sanity.w1_evidence_sanity_per_fold_pred_rows
   pysrc.meta.w1_evidence_sanity.w1_evidence_sanity_closure_ok


Module Contents
---------------

.. py:class:: W1FoldSanityDiag

   .. py:attribute:: fold_index
      :type:  int
      :value: Ellipsis



   .. py:attribute:: query_target_variance
      :type:  float
      :value: Ellipsis



   .. py:attribute:: std_incumbent_preds
      :type:  float
      :value: Ellipsis



   .. py:attribute:: std_challenger_preds
      :type:  float | None
      :value: Ellipsis



.. py:function:: w1_evidence_sanity_pool_target_stats(tasks, task_query_targets, task_support_targets)

.. py:function:: w1_evidence_sanity_per_fold_pred_rows(fold_diags)

.. py:function:: w1_evidence_sanity_closure_ok(*, tasks, task_query_targets, task_support_targets, fold_diags, fold_results_inc, fold_results_ch, cfg)

