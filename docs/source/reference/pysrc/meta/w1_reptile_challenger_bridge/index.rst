pysrc.meta.w1_reptile_challenger_bridge
=======================================

.. py:module:: pysrc.meta.w1_reptile_challenger_bridge


Exceptions
----------

.. autoapisummary::

   pysrc.meta.w1_reptile_challenger_bridge.W1ChallengerUnavailableError


Classes
-------

.. autoapisummary::

   pysrc.meta.w1_reptile_challenger_bridge.W1MetaAllocatorProtocol


Functions
---------

.. autoapisummary::

   pysrc.meta.w1_reptile_challenger_bridge.build_reptile_w1_challenger_surface


Module Contents
---------------

.. py:exception:: W1ChallengerUnavailableError(message, *, details = ...)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:class:: W1MetaAllocatorProtocol

   Bases: :py:obj:`Protocol`


   .. py:method:: predict_query_scores(task, *, fold_index)


.. py:function:: build_reptile_w1_challenger_surface(*, task_pool, fold_plan, trained_state, task_pool_hash, data_fingerprint, splits_fingerprint, cost_assumptions_fingerprint, signal_set_version, created_at_utc, source = ..., model_family = ..., leakage_policy = ..., model_state_hash = ...)

