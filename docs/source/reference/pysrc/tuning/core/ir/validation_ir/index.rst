pysrc.tuning.core.ir.validation_ir
==================================

.. py:module:: pysrc.tuning.core.ir.validation_ir


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.ir.validation_ir.EmbargoSpec
   pysrc.tuning.core.ir.validation_ir.ValidationIR


Module Contents
---------------

.. py:class:: EmbargoSpec

   .. py:attribute:: periods
      :type:  int
      :value: Ellipsis



   .. py:attribute:: unit
      :type:  Literal['bars', 'days']
      :value: Ellipsis



.. py:class:: ValidationIR

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: method
      :type:  Literal['walkforward', 'purged_cv', 'cpcv', 'crisis_holdout']
      :value: Ellipsis



   .. py:attribute:: n_splits
      :type:  int
      :value: Ellipsis



   .. py:attribute:: embargo
      :type:  EmbargoSpec
      :value: Ellipsis



   .. py:attribute:: crisis_holdout
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: cost_stress_bps
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_train_periods
      :type:  int
      :value: Ellipsis



   .. py:attribute:: meta
      :type:  IRMetadata
      :value: Ellipsis



