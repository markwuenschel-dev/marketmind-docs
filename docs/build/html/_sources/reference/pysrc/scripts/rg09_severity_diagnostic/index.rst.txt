pysrc.scripts.rg09_severity_diagnostic
======================================

.. py:module:: pysrc.scripts.rg09_severity_diagnostic


Attributes
----------

.. autoapisummary::

   pysrc.scripts.rg09_severity_diagnostic.REQUIRED_COLS


Exceptions
----------

.. autoapisummary::

   pysrc.scripts.rg09_severity_diagnostic.SeverityDiagnosticError


Classes
-------

.. autoapisummary::

   pysrc.scripts.rg09_severity_diagnostic.HighVolEpisodeRow


Functions
---------

.. autoapisummary::

   pysrc.scripts.rg09_severity_diagnostic.extract_high_vol_episodes
   pysrc.scripts.rg09_severity_diagnostic.pit_safe_threshold
   pysrc.scripts.rg09_severity_diagnostic.episode_eligible_for_pit
   pysrc.scripts.rg09_severity_diagnostic.classify_episode_severity
   pysrc.scripts.rg09_severity_diagnostic.cohens_d_two_sample
   pysrc.scripts.rg09_severity_diagnostic.parse_thresholds_arg
   pysrc.scripts.rg09_severity_diagnostic.discover_fixture_parquets
   pysrc.scripts.rg09_severity_diagnostic.run_severity_diagnostic
   pysrc.scripts.rg09_severity_diagnostic.main


Module Contents
---------------

.. py:data:: REQUIRED_COLS
   :type:  Any

.. py:exception:: SeverityDiagnosticError

   Bases: :py:obj:`RuntimeError`


   Unspecified run-time error.


.. py:class:: HighVolEpisodeRow

   .. py:attribute:: start_idx
      :type:  int
      :value: Ellipsis



   .. py:attribute:: end_idx
      :type:  int
      :value: Ellipsis



   .. py:attribute:: entity_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: peak_log_rv
      :type:  float
      :value: Ellipsis



   .. py:attribute:: mean_log_rv
      :type:  float
      :value: Ellipsis



   .. py:attribute:: mean_return
      :type:  float
      :value: Ellipsis



   .. py:attribute:: episode_length
      :type:  int
      :value: Ellipsis



   .. py:attribute:: episode_start
      :type:  pd.Timestamp
      :value: Ellipsis



   .. py:attribute:: episode_end
      :type:  pd.Timestamp
      :value: Ellipsis



.. py:function:: extract_high_vol_episodes(df, *, entity_id = ...)

.. py:function:: pit_safe_threshold(vol_series, k, percentile)

.. py:function:: episode_eligible_for_pit(ep, *, cold_start_burn_in)

.. py:function:: classify_episode_severity(ep, vol_series, percentile, *, cold_start_burn_in)

.. py:function:: cohens_d_two_sample(a, b)

.. py:function:: parse_thresholds_arg(value)

.. py:function:: discover_fixture_parquets(basket_dir)

.. py:function:: run_severity_diagnostic(basket_dir, *, thresholds = ..., dedup_window_days = ..., cold_start_burn_in = ..., sizing = ...)

.. py:function:: main(basket_dir, output_path, thresholds_raw, dedup_window_days, cold_start_burn_in)

