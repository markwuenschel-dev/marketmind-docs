pysrc.tuning.core.ir.promotion_ir
=================================

.. py:module:: pysrc.tuning.core.ir.promotion_ir


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.ir.promotion_ir.PromotionIR


Module Contents
---------------

.. py:class:: PromotionIR

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: candidate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: mode
      :type:  Literal['shadow', 'capped_blend', 'full']
      :value: Ellipsis



   .. py:attribute:: shadow_duration_days
      :type:  int
      :value: Ellipsis



   .. py:attribute:: rollback_policy
      :type:  Literal['auto', 'manual', 'none']
      :value: Ellipsis



   .. py:attribute:: approval_required
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: meta
      :type:  IRMetadata
      :value: Ellipsis



   .. py:attribute:: blend_cap
      :type:  float | None
      :value: Ellipsis



