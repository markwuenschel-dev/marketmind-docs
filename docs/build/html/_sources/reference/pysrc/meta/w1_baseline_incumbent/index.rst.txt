pysrc.meta.w1_baseline_incumbent
================================

.. py:module:: pysrc.meta.w1_baseline_incumbent


Classes
-------

.. autoapisummary::

   pysrc.meta.w1_baseline_incumbent.XGBoostIncumbentConfig
   pysrc.meta.w1_baseline_incumbent.XGBoostIncumbentBaseline


Functions
---------

.. autoapisummary::

   pysrc.meta.w1_baseline_incumbent.challenger_proxy_scores_for_tasks


Module Contents
---------------

.. py:class:: XGBoostIncumbentConfig

   .. py:attribute:: random_state
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_estimators
      :type:  int
      :value: Ellipsis



   .. py:attribute:: max_depth
      :type:  int
      :value: Ellipsis



   .. py:attribute:: learning_rate
      :type:  float
      :value: Ellipsis



   .. py:attribute:: tree_method
      :type:  str
      :value: Ellipsis



.. py:class:: XGBoostIncumbentBaseline(cfg = ...)

   .. py:method:: fit_for_training_tasks(tasks, *, rng_seed, training_targets = ...)


   .. py:method:: predict_scores(task, *, fold_index, rng_seed, use_hash_score_jitter = ...)


   .. py:method:: describe()


.. py:function:: challenger_proxy_scores_for_tasks(tasks, *, fold_index, rng_seed)

