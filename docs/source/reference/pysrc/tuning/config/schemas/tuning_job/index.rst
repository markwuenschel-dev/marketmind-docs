pysrc.tuning.config.schemas.tuning_job
======================================

.. py:module:: pysrc.tuning.config.schemas.tuning_job


Classes
-------

.. autoapisummary::

   pysrc.tuning.config.schemas.tuning_job.TuningJobConfig


Module Contents
---------------

.. py:class:: TuningJobConfig

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: search_space_ref
      :type:  str
      :value: Ellipsis



   .. py:attribute:: objective_ref
      :type:  str
      :value: Ellipsis



   .. py:attribute:: validation_ref
      :type:  str
      :value: Ellipsis



   .. py:attribute:: promotion_ref
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: max_trials
      :type:  int
      :value: Ellipsis



   .. py:attribute:: timeout_seconds
      :type:  int | None
      :value: Ellipsis



   .. py:attribute:: determinism_tier
      :type:  Literal['d0', 'd1', 'd2', 'd3']
      :value: Ellipsis



   .. py:attribute:: tags
      :type:  dict[str, str]
      :value: Ellipsis



   .. py:attribute:: crisis_holdout
      :type:  bool
      :value: Ellipsis



