pysrc.meta.w1_challenger_surface
================================

.. py:module:: pysrc.meta.w1_challenger_surface


Attributes
----------

.. autoapisummary::

   pysrc.meta.w1_challenger_surface.W1_CHALLENGER_SURFACE_SCHEMA_VERSION
   pysrc.meta.w1_challenger_surface.KNOWN_LEAKAGE_POLICIES


Exceptions
----------

.. autoapisummary::

   pysrc.meta.w1_challenger_surface.W1ChallengerSurfaceValidationError


Classes
-------

.. autoapisummary::

   pysrc.meta.w1_challenger_surface.W1ChallengerPrediction
   pysrc.meta.w1_challenger_surface.W1ChallengerSurface
   pysrc.meta.w1_challenger_surface.W1FoldPlan


Functions
---------

.. autoapisummary::

   pysrc.meta.w1_challenger_surface.derive_w1_fold_plan
   pysrc.meta.w1_challenger_surface.valid_learned_model_state_hash
   pysrc.meta.w1_challenger_surface.w1_challenger_surface_closure_eligible
   pysrc.meta.w1_challenger_surface.validate_w1_challenger_surface
   pysrc.meta.w1_challenger_surface.challenger_mean_query_scores_for_tasks
   pysrc.meta.w1_challenger_surface.w1_challenger_surface_summary_dict
   pysrc.meta.w1_challenger_surface.w1_challenger_surface_to_canonical_dict


Module Contents
---------------

.. py:data:: W1_CHALLENGER_SURFACE_SCHEMA_VERSION
   :type:  Any

.. py:data:: KNOWN_LEAKAGE_POLICIES
   :type:  frozenset[str]
   :value: Ellipsis


.. py:exception:: W1ChallengerSurfaceValidationError(message, *, details = ...)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:class:: W1ChallengerPrediction

   .. py:attribute:: task_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: fold_index
      :type:  int
      :value: Ellipsis



   .. py:attribute:: query_scores
      :type:  tuple[float, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: prediction_time_utc
      :type:  str
      :value: Ellipsis



   .. py:attribute:: pit_boundary
      :type:  str
      :value: Ellipsis



.. py:class:: W1ChallengerSurface

   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: source
      :type:  str
      :value: Ellipsis



   .. py:attribute:: model_family
      :type:  str
      :value: Ellipsis



   .. py:attribute:: predictions
      :type:  tuple[W1ChallengerPrediction, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: task_pool_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: data_fingerprint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: splits_fingerprint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: cost_assumptions_fingerprint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: signal_set_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: created_at_utc
      :type:  str
      :value: Ellipsis



   .. py:attribute:: leakage_policy
      :type:  str
      :value: Ellipsis



   .. py:attribute:: uses_query_labels
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: uses_xgboost_outputs
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: uses_post_query_metrics
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: model_state_hash
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: governed_checkpoint_lineage_verified
      :type:  bool
      :value: Ellipsis



.. py:class:: W1FoldPlan

   .. py:attribute:: warmup_bars
      :type:  int
      :value: Ellipsis



   .. py:attribute:: fold_length_bars
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_walk_forward_folds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: train_task_ids_by_fold
      :type:  tuple[tuple[str, Ellipsis], Ellipsis]
      :value: Ellipsis



   .. py:attribute:: task_ids_by_fold
      :type:  tuple[tuple[str, Ellipsis], Ellipsis]
      :value: Ellipsis



.. py:function:: derive_w1_fold_plan(sorted_tasks, config)

.. py:function:: valid_learned_model_state_hash(h)

.. py:function:: w1_challenger_surface_closure_eligible(surface)

.. py:function:: validate_w1_challenger_surface(surface, *, expected_task_ids_by_fold, expected_query_lengths, task_pool_hash, data_fingerprint, splits_fingerprint, cost_assumptions_fingerprint, signal_set_version)

.. py:function:: challenger_mean_query_scores_for_tasks(surface, tasks, fold_index)

.. py:function:: w1_challenger_surface_summary_dict(surface)

.. py:function:: w1_challenger_surface_to_canonical_dict(surface)

