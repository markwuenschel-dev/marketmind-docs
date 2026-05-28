pysrc.meta.regime_config
========================

.. py:module:: pysrc.meta.regime_config


Classes
-------

.. autoapisummary::

   pysrc.meta.regime_config.BOCPDConfig


Module Contents
---------------

.. py:class:: BOCPDConfig

   .. py:attribute:: hazard_rate
      :type:  float
      :value: Ellipsis



   .. py:attribute:: observation_model
      :type:  Literal['student_t', 'gaussian']
      :value: Ellipsis



   .. py:attribute:: prior_mu0
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: prior_kappa0
      :type:  float
      :value: Ellipsis



   .. py:attribute:: prior_alpha0
      :type:  float
      :value: Ellipsis



   .. py:attribute:: prior_beta0
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: max_run_length
      :type:  int
      :value: Ellipsis



   .. py:attribute:: vol_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: trend_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: trend_flat_epsilon
      :type:  float
      :value: Ellipsis



   .. py:attribute:: vol_bucket_method
      :type:  Literal['tercile', 'quintile']
      :value: Ellipsis



   .. py:attribute:: cp_threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: transition_threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: transition_max_rl
      :type:  int
      :value: Ellipsis



   .. py:attribute:: cold_start_burn_in
      :type:  int
      :value: Ellipsis



   .. py:attribute:: crisis_vol_score_percentile
      :type:  float
      :value: Ellipsis



   .. py:attribute:: config_version
      :type:  str
      :value: Ellipsis



   .. py:method:: to_dict()


   .. py:method:: content_hash()


