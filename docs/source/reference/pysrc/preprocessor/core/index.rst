pysrc.preprocessor.core
=======================

.. py:module:: pysrc.preprocessor.core


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.core.load_ohlcv
   pysrc.preprocessor.core.add_returns
   pysrc.preprocessor.core.add_sma
   pysrc.preprocessor.core.add_rsi
   pysrc.preprocessor.core.build_features


Module Contents
---------------

.. py:function:: load_ohlcv(path, *, backend = ...)

.. py:function:: add_returns(df, column = ..., *, backend = ...)

.. py:function:: add_sma(df, column = ..., window = ..., *, backend = ...)

.. py:function:: add_rsi(df, column = ..., window = ..., *, backend = ...)

.. py:function:: build_features(df, *, sma_windows = ..., rsi_window = ..., backend = ...)

