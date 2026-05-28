pysrc.meta.bocpd_service
========================

.. py:module:: pysrc.meta.bocpd_service


Classes
-------

.. autoapisummary::

   pysrc.meta.bocpd_service.NIGPrior
   pysrc.meta.bocpd_service.SufficientStats
   pysrc.meta.bocpd_service.ServiceSnapshot
   pysrc.meta.bocpd_service.RegimeLabelRecord
   pysrc.meta.bocpd_service.BOCPDRegimeService


Functions
---------

.. autoapisummary::

   pysrc.meta.bocpd_service.nig_update_obs
   pysrc.meta.bocpd_service.merge_nig_tail
   pysrc.meta.bocpd_service.predictive_logpdf
   pysrc.meta.bocpd_service.bocpd_update
   pysrc.meta.bocpd_service.state_snapshot_id


Module Contents
---------------

.. py:class:: NIGPrior

   .. py:attribute:: mu0
      :type:  float
      :value: Ellipsis



   .. py:attribute:: kappa0
      :type:  float
      :value: Ellipsis



   .. py:attribute:: alpha0
      :type:  float
      :value: Ellipsis



   .. py:attribute:: beta0
      :type:  float
      :value: Ellipsis



.. py:class:: SufficientStats

   .. py:attribute:: mu
      :type:  NDArray[np.float64]
      :value: Ellipsis



   .. py:attribute:: kappa
      :type:  NDArray[np.float64]
      :value: Ellipsis



   .. py:attribute:: alpha
      :type:  NDArray[np.float64]
      :value: Ellipsis



   .. py:attribute:: beta
      :type:  NDArray[np.float64]
      :value: Ellipsis



.. py:function:: nig_update_obs(mu, kappa, alpha, beta, x)

.. py:function:: merge_nig_tail(mus, kappas, alphas, betas, prior)

.. py:function:: predictive_logpdf(x, mu, kappa, alpha, beta, observation_model)

.. py:function:: bocpd_update(x, log_posterior, sufficient_stats, config, prior)

.. py:class:: ServiceSnapshot

   .. py:attribute:: log_posterior
      :type:  NDArray[np.float64]
      :value: Ellipsis



   .. py:attribute:: sufficient_stats
      :type:  SufficientStats
      :value: Ellipsis



   .. py:attribute:: observation_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: config_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: prior
      :type:  NIGPrior
      :value: Ellipsis



.. py:function:: state_snapshot_id(snapshot)

.. py:class:: RegimeLabelRecord

   .. py:attribute:: entity_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: decision_ts
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: regime_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: regime_label
      :type:  str
      :value: Ellipsis



   .. py:attribute:: effective_at
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: state_snapshot_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: input_snapshot_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: config_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: change_probability
      :type:  float
      :value: Ellipsis



   .. py:attribute:: boundary_flag
      :type:  Literal['cold_start', 'change_point', 'transition', 'stable']
      :value: Ellipsis



   .. py:attribute:: regime_class
      :type:  RegimeClassLabel
      :value: Ellipsis



   .. py:attribute:: diag_regime_class_bocpd_gated
      :type:  RegimeClassLabel
      :value: Ellipsis



   .. py:attribute:: diag_regime_class_extended
      :type:  RegimeClassLabel
      :value: Ellipsis



   .. py:attribute:: run_length_mode
      :type:  int
      :value: Ellipsis



   .. py:attribute:: run_length_expectation
      :type:  float
      :value: Ellipsis



   .. py:attribute:: transition_probability
      :type:  float
      :value: Ellipsis



   .. py:attribute:: posterior_entropy
      :type:  float
      :value: Ellipsis



   .. py:attribute:: trend_score_raw
      :type:  float
      :value: Ellipsis



   .. py:attribute:: vol_score_raw
      :type:  float
      :value: Ellipsis



   .. py:attribute:: cold_start
      :type:  bool
      :value: Ellipsis



.. py:class:: BOCPDRegimeService(config)

   .. py:method:: initialize(historical_log_rv)


   .. py:method:: update(decision_ts, log_rv, *, log_return, entity_id = ..., pit_boundary_idx, log_rv_history, returns_history)


   .. py:method:: snapshot()


   .. py:method:: from_snapshot(snapshot, config)


