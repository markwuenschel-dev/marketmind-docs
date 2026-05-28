pysrc.meta.phase2_broad_reset.p2_narrow
=======================================

.. py:module:: pysrc.meta.phase2_broad_reset.p2_narrow


Attributes
----------

.. autoapisummary::

   pysrc.meta.phase2_broad_reset.p2_narrow.LOG
   pysrc.meta.phase2_broad_reset.p2_narrow.DEFERRED_STRESS


Functions
---------

.. autoapisummary::

   pysrc.meta.phase2_broad_reset.p2_narrow.get_model_instance
   pysrc.meta.phase2_broad_reset.p2_narrow.train_and_predict
   pysrc.meta.phase2_broad_reset.p2_narrow.apply_decision_rule
   pysrc.meta.phase2_broad_reset.p2_narrow.tune_override_threshold
   pysrc.meta.phase2_broad_reset.p2_narrow.build_test_prediction_frame
   pysrc.meta.phase2_broad_reset.p2_narrow.train_best_child_index
   pysrc.meta.phase2_broad_reset.p2_narrow.w4b_comparators_to_baselines
   pysrc.meta.phase2_broad_reset.p2_narrow.evaluate_candidate_with_context
   pysrc.meta.phase2_broad_reset.p2_narrow.run_p2_narrow
   pysrc.meta.phase2_broad_reset.p2_narrow.generate_human_summary


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:data:: DEFERRED_STRESS
   :type:  Any

.. py:function:: get_model_instance(candidate, random_seed, *, sklearn_n_jobs = ...)

.. py:function:: train_and_predict(candidate, x_train, y_train, x_validation, x_test, random_seed, *, sklearn_n_jobs = ...)

.. py:function:: apply_decision_rule(preds, candidate, best_child_idx_train, min_delta_for_override, *, override_threshold = ...)

.. py:function:: tune_override_threshold(candidate, preds_validation, y_validation, *, best_child_idx_train, min_delta_for_override)

.. py:function:: build_test_prediction_frame(test_rows, chosen_indices, y_test, *, model_family)

.. py:function:: train_best_child_index(date_frame, child_policy_ids)

.. py:function:: w4b_comparators_to_baselines(comparators)

.. py:function:: evaluate_candidate_with_context(candidate, ctx)

.. py:function:: run_p2_narrow(config = ...)

.. py:function:: generate_human_summary(report, manifest, baselines)

