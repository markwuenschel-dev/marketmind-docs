pysrc.meta.indicators.pandas_ta_classic_provider
================================================

.. py:module:: pysrc.meta.indicators.pandas_ta_classic_provider


Classes
-------

.. autoapisummary::

   pysrc.meta.indicators.pandas_ta_classic_provider.IndicatorProviderResult


Functions
---------

.. autoapisummary::

   pysrc.meta.indicators.pandas_ta_classic_provider.compute_pandas_ta_classic_features


Module Contents
---------------

.. py:class:: IndicatorProviderResult

   .. py:attribute:: features
      :type:  pd.DataFrame
      :value: Ellipsis



   .. py:attribute:: indicator_columns
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: provider_mappings
      :type:  dict[str, dict[str, object]]
      :value: Ellipsis



   .. py:attribute:: warmup
      :type:  dict[str, int]
      :value: Ellipsis



.. py:function:: compute_pandas_ta_classic_features(panel, config = ..., *, workers = ...)

