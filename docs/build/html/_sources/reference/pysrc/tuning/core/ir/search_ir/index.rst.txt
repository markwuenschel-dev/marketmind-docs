pysrc.tuning.core.ir.search_ir
==============================

.. py:module:: pysrc.tuning.core.ir.search_ir


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.ir.search_ir.Trial
   pysrc.tuning.core.ir.search_ir.SearchIR


Module Contents
---------------

.. py:class:: Trial

   .. py:attribute:: trial_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: params
      :type:  tuple[HParam, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: scores
      :type:  dict[str, float]
      :value: Ellipsis



   .. py:attribute:: feasible
      :type:  bool
      :value: Ellipsis



.. py:class:: SearchIR

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: algorithm
      :type:  str
      :value: Ellipsis



   .. py:attribute:: space_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: meta
      :type:  IRMetadata
      :value: Ellipsis



   .. py:attribute:: trials
      :type:  tuple[Trial, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: best_trial_id
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: n_pending
      :type:  int
      :value: Ellipsis



