pysrc.tuning.config.schemas.promotion
=====================================

.. py:module:: pysrc.tuning.config.schemas.promotion


Classes
-------

.. autoapisummary::

   pysrc.tuning.config.schemas.promotion.PromotionConfig


Module Contents
---------------

.. py:class:: PromotionConfig

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: mode
      :type:  Literal['shadow', 'capped_blend', 'full']
      :value: Ellipsis



   .. py:attribute:: blend_cap
      :type:  float | None
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



