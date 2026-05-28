pysrc.meta.indicators.scaling
=============================

.. py:module:: pysrc.meta.indicators.scaling


Classes
-------

.. autoapisummary::

   pysrc.meta.indicators.scaling.IndicatorRobustScale


Functions
---------

.. autoapisummary::

   pysrc.meta.indicators.scaling.sanitize_indicator_series
   pysrc.meta.indicators.scaling.fit_robust_indicator_scales
   pysrc.meta.indicators.scaling.apply_robust_indicator_scales
   pysrc.meta.indicators.scaling.robust_scale_metadata_payload


Module Contents
---------------

.. py:class:: IndicatorRobustScale

   .. py:attribute:: indicator_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: median
      :type:  float
      :value: Ellipsis



   .. py:attribute:: iqr
      :type:  float
      :value: Ellipsis



   .. py:attribute:: mad
      :type:  float
      :value: Ellipsis



   .. py:attribute:: lower_clip
      :type:  float
      :value: Ellipsis



   .. py:attribute:: upper_clip
      :type:  float
      :value: Ellipsis



   .. py:attribute:: scale_denominator
      :type:  float
      :value: Ellipsis



   .. py:attribute:: train_validation_fit_only
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: iqr_multiplier
      :type:  float
      :value: Ellipsis



   .. py:method:: as_metadata()


.. py:function:: sanitize_indicator_series(values)

.. py:function:: fit_robust_indicator_scales(rows, indicator_columns, *, iqr_multiplier = ..., min_iqr = ...)

.. py:function:: apply_robust_indicator_scales(rows, scales, *, copy = ...)

.. py:function:: robust_scale_metadata_payload(scales)

