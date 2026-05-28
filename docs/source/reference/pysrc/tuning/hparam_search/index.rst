pysrc.tuning.hparam_search
==========================

.. py:module:: pysrc.tuning.hparam_search


Attributes
----------

.. autoapisummary::

   pysrc.tuning.hparam_search.T


Classes
-------

.. autoapisummary::

   pysrc.tuning.hparam_search.Trial
   pysrc.tuning.hparam_search.SearchState
   pysrc.tuning.hparam_search.SearchAlgorithm
   pysrc.tuning.hparam_search.HparamSearch


Module Contents
---------------

.. py:data:: T
   :type:  Any

.. py:class:: Trial

   .. py:attribute:: trial_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: params
      :type:  Mapping[str, Any]
      :value: Ellipsis



   .. py:attribute:: metric
      :type:  float
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  Mapping[str, float] | None
      :value: Ellipsis



.. py:class:: SearchState

   .. py:attribute:: completed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: best_trial
      :type:  Trial | None
      :value: Ellipsis



   .. py:attribute:: history
      :type:  Sequence[Trial]
      :value: Ellipsis



.. py:class:: SearchAlgorithm

   Bases: :py:obj:`ABC`, :py:obj:`Generic`\ [\ :py:obj:`T`\ ]


   .. py:method:: suggest(state, space)


   .. py:method:: update(state, trial)


.. py:class:: HparamSearch

   Bases: :py:obj:`ABC`


   .. py:method:: execute(objective, space, algorithm, *, max_trials, early_stop_patience = ...)


   .. py:method:: resume(run_id)


