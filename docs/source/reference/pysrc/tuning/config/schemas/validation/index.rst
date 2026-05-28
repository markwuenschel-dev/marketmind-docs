pysrc.tuning.config.schemas.validation
======================================

.. py:module:: pysrc.tuning.config.schemas.validation


Classes
-------

.. autoapisummary::

   pysrc.tuning.config.schemas.validation.ValidationConfig


Module Contents
---------------

.. py:class:: ValidationConfig

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: method
      :type:  Literal['walkforward', 'purged_cv', 'cpcv', 'crisis_holdout']
      :value: Ellipsis



   .. py:attribute:: n_splits
      :type:  int
      :value: Ellipsis



   .. py:attribute:: embargo_periods
      :type:  int
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



