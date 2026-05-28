pysrc.tuning.core.ir.objective_ir
=================================

.. py:module:: pysrc.tuning.core.ir.objective_ir


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.ir.objective_ir.PenaltySpec
   pysrc.tuning.core.ir.objective_ir.ObjectiveIR


Module Contents
---------------

.. py:class:: PenaltySpec

   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: coefficient
      :type:  float
      :value: Ellipsis



.. py:class:: ObjectiveIR

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: direction
      :type:  Literal['maximize', 'minimize']
      :value: Ellipsis



   .. py:attribute:: metrics
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: weights
      :type:  dict[str, float]
      :value: Ellipsis



   .. py:attribute:: penalties
      :type:  tuple[PenaltySpec, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: constraints
      :type:  tuple[Scalar, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: meta
      :type:  IRMetadata
      :value: Ellipsis



