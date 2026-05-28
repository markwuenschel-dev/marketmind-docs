pysrc.tuning.api.schemas
========================

.. py:module:: pysrc.tuning.api.schemas


Classes
-------

.. autoapisummary::

   pysrc.tuning.api.schemas.TuningJobRequest
   pysrc.tuning.api.schemas.TuningJobResponse
   pysrc.tuning.api.schemas.PromotionRequest
   pysrc.tuning.api.schemas.PromotionResponse
   pysrc.tuning.api.schemas.SearchStatusResponse
   pysrc.tuning.api.schemas.GateResultResponse


Module Contents
---------------

.. py:class:: TuningJobRequest

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: job_id
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



   .. py:attribute:: tags
      :type:  dict[str, str]
      :value: Ellipsis



.. py:class:: TuningJobResponse

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: status
      :type:  str
      :value: Ellipsis



   .. py:attribute:: run_id
      :type:  str | None
      :value: Ellipsis



.. py:class:: PromotionRequest

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: candidate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: mode
      :type:  str
      :value: Ellipsis



.. py:class:: PromotionResponse

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: candidate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: promotion_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: status
      :type:  str
      :value: Ellipsis



.. py:class:: SearchStatusResponse

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: status
      :type:  str
      :value: Ellipsis



   .. py:attribute:: trials_complete
      :type:  int
      :value: Ellipsis



   .. py:attribute:: best_score
      :type:  float | None
      :value: Ellipsis



.. py:class:: GateResultResponse

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: candidate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: passed
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: gate_scores
      :type:  dict[str, float]
      :value: Ellipsis



