pysrc.preprocessor.graph.ops_custom
===================================

.. py:module:: pysrc.preprocessor.graph.ops_custom


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.graph.ops_custom.lower_rsi_polars
   pysrc.preprocessor.graph.ops_custom.lower_sma_polars
   pysrc.preprocessor.graph.ops_custom.lower_ema_polars
   pysrc.preprocessor.graph.ops_custom.lower_macd_line_signal_polars
   pysrc.preprocessor.graph.ops_custom.lower_bollinger_polars
   pysrc.preprocessor.graph.ops_custom.lower_atr_polars
   pysrc.preprocessor.graph.ops_custom.lower_obv_polars
   pysrc.preprocessor.graph.ops_custom.lower_vwap_polars
   pysrc.preprocessor.graph.ops_custom.lower_zscore_roll_polars
   pysrc.preprocessor.graph.ops_custom.lower_rolling_std_polars


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.graph.ops_custom.RSI
   pysrc.preprocessor.graph.ops_custom.SMA
   pysrc.preprocessor.graph.ops_custom.EMA
   pysrc.preprocessor.graph.ops_custom.MACDLineSignal
   pysrc.preprocessor.graph.ops_custom.Bollinger
   pysrc.preprocessor.graph.ops_custom.ATR
   pysrc.preprocessor.graph.ops_custom.OBV
   pysrc.preprocessor.graph.ops_custom.VWAP
   pysrc.preprocessor.graph.ops_custom.RollingStd
   pysrc.preprocessor.graph.ops_custom.Lags
   pysrc.preprocessor.graph.ops_custom.ZScore
   pysrc.preprocessor.graph.ops_custom.RobustScaler
   pysrc.preprocessor.graph.ops_custom.SentimentLexicon
   pysrc.preprocessor.graph.ops_custom.PairBeta
   pysrc.preprocessor.graph.ops_custom.PairSpread
   pysrc.preprocessor.graph.ops_custom.HalfLife
   pysrc.preprocessor.graph.ops_custom.RollingZ
   pysrc.preprocessor.graph.ops_custom.RollingVol
   pysrc.preprocessor.graph.ops_custom.XSecRank
   pysrc.preprocessor.graph.ops_custom.VolScale
   pysrc.preprocessor.graph.ops_custom.ResidualOLS
   pysrc.preprocessor.graph.ops_custom.ResidualKF
   pysrc.preprocessor.graph.ops_custom.IndustryScore
   pysrc.preprocessor.graph.ops_custom.FeatureReturns
   pysrc.preprocessor.graph.ops_custom.FeatureSMA
   pysrc.preprocessor.graph.ops_custom.FeatureRSI
   pysrc.preprocessor.graph.ops_custom.DataLoadCSV


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.graph.ops_custom.lower_pairs_beta_polars
   pysrc.preprocessor.graph.ops_custom.lower_pairs_spread_polars
   pysrc.preprocessor.graph.ops_custom.lower_half_life_polars
   pysrc.preprocessor.graph.ops_custom.lower_rolling_vol_polars
   pysrc.preprocessor.graph.ops_custom.lower_xsec_rank_polars
   pysrc.preprocessor.graph.ops_custom.lower_vol_scale_polars
   pysrc.preprocessor.graph.ops_custom.lower_residual_ols_polars
   pysrc.preprocessor.graph.ops_custom.lower_residual_kf_polars
   pysrc.preprocessor.graph.ops_custom.lower_industry_score_polars


Module Contents
---------------

.. py:class:: RSI

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:class:: SMA

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:class:: EMA

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:class:: MACDLineSignal

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:class:: Bollinger

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:class:: ATR

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:class:: OBV

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`ElementwiseOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:class:: VWAP

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`ElementwiseOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:class:: RollingStd

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:class:: Lags

   Bases: :py:obj:`SequenceOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


.. py:class:: ZScore

   Bases: :py:obj:`ScalingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: state_dict()


.. py:class:: RobustScaler

   Bases: :py:obj:`ScalingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: state_dict()


.. py:class:: SentimentLexicon

   Bases: :py:obj:`ElementwiseOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


.. py:class:: PairBeta

   Bases: :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


.. py:class:: PairSpread

   Bases: :py:obj:`ElementwiseOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


.. py:class:: HalfLife

   Bases: :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


.. py:class:: RollingZ

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`ScalingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:class:: RollingVol

   Bases: :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


.. py:class:: XSecRank

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:class:: VolScale

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:class:: ResidualOLS

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:class:: ResidualKF

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:class:: IndustryScore

   Bases: :py:obj:`_ProvidesMixin`, :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


   .. py:method:: to_ir()


.. py:function:: lower_pairs_beta_polars(ir, lf, *, group_by = ...)

.. py:function:: lower_pairs_spread_polars(ir, lf, *, group_by = ...)

.. py:function:: lower_half_life_polars(ir, lf, *, group_by = ...)

.. py:function:: lower_rolling_vol_polars(*args, **kwargs)

.. py:function:: lower_xsec_rank_polars(ir, lf, *, group_by = ...)

.. py:function:: lower_vol_scale_polars(ir, lf, *, group_by = ...)

.. py:function:: lower_residual_ols_polars(ir, lf, *, group_by = ...)

.. py:function:: lower_residual_kf_polars(ir, lf, *, group_by = ...)

.. py:function:: lower_industry_score_polars(ir, lf, *, group_by = ...)

.. py:data:: lower_rsi_polars
   :type:  Any

.. py:data:: lower_sma_polars
   :type:  Any

.. py:data:: lower_ema_polars
   :type:  Any

.. py:data:: lower_macd_line_signal_polars
   :type:  Any

.. py:data:: lower_bollinger_polars
   :type:  Any

.. py:data:: lower_atr_polars
   :type:  Any

.. py:data:: lower_obv_polars
   :type:  Any

.. py:data:: lower_vwap_polars
   :type:  Any

.. py:data:: lower_zscore_roll_polars
   :type:  Any

.. py:data:: lower_rolling_std_polars
   :type:  Any

.. py:class:: FeatureReturns

   Bases: :py:obj:`ElementwiseOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


.. py:class:: FeatureSMA

   Bases: :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


.. py:class:: FeatureRSI

   Bases: :py:obj:`RollingOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


.. py:class:: DataLoadCSV

   Bases: :py:obj:`ElementwiseOp`


   .. py:attribute:: NAME
      :type:  Any


   .. py:method:: validate_params()


