pysrc.meta.phase2_broad_reset.p2_parallel
=========================================

.. py:module:: pysrc.meta.phase2_broad_reset.p2_parallel


Classes
-------

.. autoapisummary::

   pysrc.meta.phase2_broad_reset.p2_parallel.FoldSlice
   pysrc.meta.phase2_broad_reset.p2_parallel.NarrowEvalContext


Functions
---------

.. autoapisummary::

   pysrc.meta.phase2_broad_reset.p2_parallel.resolve_narrow_workers
   pysrc.meta.phase2_broad_reset.p2_parallel.resolve_sklearn_n_jobs
   pysrc.meta.phase2_broad_reset.p2_parallel.build_fold_slices
   pysrc.meta.phase2_broad_reset.p2_parallel.build_eval_context
   pysrc.meta.phase2_broad_reset.p2_parallel.narrow_worker_entry
   pysrc.meta.phase2_broad_reset.p2_parallel.evaluate_candidates_parallel


Module Contents
---------------

.. py:class:: FoldSlice

   .. py:attribute:: fold_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: x_train
      :type:  np.ndarray
      :value: Ellipsis



   .. py:attribute:: y_train
      :type:  np.ndarray
      :value: Ellipsis



   .. py:attribute:: x_validation
      :type:  np.ndarray
      :value: Ellipsis



   .. py:attribute:: y_validation
      :type:  np.ndarray
      :value: Ellipsis



   .. py:attribute:: x_test
      :type:  np.ndarray
      :value: Ellipsis



   .. py:attribute:: y_test
      :type:  np.ndarray
      :value: Ellipsis



   .. py:attribute:: test_meta
      :type:  pd.DataFrame
      :value: Ellipsis



.. py:class:: NarrowEvalContext

   .. py:attribute:: fold_slices
      :type:  tuple[FoldSlice, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: child_policy_ids
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: random_seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_delta_for_override
      :type:  float
      :value: Ellipsis



   .. py:attribute:: best_child_idx_train
      :type:  int
      :value: Ellipsis



   .. py:attribute:: best_child_test_utility
      :type:  float
      :value: Ellipsis



   .. py:attribute:: sklearn_n_jobs
      :type:  int
      :value: Ellipsis



.. py:function:: resolve_narrow_workers(config, *, candidate_count)

.. py:function:: resolve_sklearn_n_jobs(config, *, narrow_workers)

.. py:function:: build_fold_slices(supervision)

.. py:function:: build_eval_context(supervision, config, *, best_child_idx_train, best_child_test_utility, narrow_workers)

.. py:function:: narrow_worker_entry(candidate_payload)

.. py:function:: evaluate_candidates_parallel(candidates, context, *, max_workers)

