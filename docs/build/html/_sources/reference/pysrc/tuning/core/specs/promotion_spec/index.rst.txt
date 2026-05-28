pysrc.tuning.core.specs.promotion_spec
======================================

.. py:module:: pysrc.tuning.core.specs.promotion_spec


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.specs.promotion_spec.PromotionSpec


Module Contents
---------------

.. py:class:: PromotionSpec

   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: spec_hash
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



   .. py:attribute:: blend_cap
      :type:  float | None
      :value: Ellipsis



