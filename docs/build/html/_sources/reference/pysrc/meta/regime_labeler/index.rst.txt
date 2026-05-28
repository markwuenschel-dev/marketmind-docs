pysrc.meta.regime_labeler
=========================

.. py:module:: pysrc.meta.regime_labeler


Classes
-------

.. autoapisummary::

   pysrc.meta.regime_labeler.RegimeLabeler


Functions
---------

.. autoapisummary::

   pysrc.meta.regime_labeler.validate_regime_id
   pysrc.meta.regime_labeler.annualized_log_rv_from_returns


Module Contents
---------------

.. py:class:: RegimeLabeler(config)

   .. py:method:: compute_trend_regime(returns, pit_boundary_idx)


   .. py:method:: compute_vol_regime(log_rv_history, pit_boundary_idx)


   .. py:method:: compute_regime_id(trend, vol, bocpd_state)


   .. py:method:: compute_severity_flag_vol_score_raw(vol_score_history, pit_boundary_idx)


   .. py:method:: project_regime_class(trend, vol, bocpd_state, *, severity_flag)


   .. py:method:: project_regime_class_bocpd_gated_reference(vol, bocpd_state)


   .. py:method:: project_regime_class_extended(trend, vol, bocpd_state)


.. py:function:: validate_regime_id(regime_id)

.. py:function:: annualized_log_rv_from_returns(returns, pit_idx, vol_window)

