pysrc.meta.indicators.diagnostics
=================================

.. py:module:: pysrc.meta.indicators.diagnostics


Classes
-------

.. autoapisummary::

   pysrc.meta.indicators.diagnostics.IndicatorDiagnosticsResult


Functions
---------

.. autoapisummary::

   pysrc.meta.indicators.diagnostics.build_indicator_diagnostics
   pysrc.meta.indicators.diagnostics.lag_outcome_diagnostic_by_horizon
   pysrc.meta.indicators.diagnostics.prune_redundant_indicators
   pysrc.meta.indicators.diagnostics.diagnostics_summary_markdown
   pysrc.meta.indicators.diagnostics.cast_mapping
   pysrc.meta.indicators.diagnostics.cast_list


Module Contents
---------------

.. py:class:: IndicatorDiagnosticsResult

   .. py:attribute:: diagnostics
      :type:  dict[str, dict[str, object]]
      :value: Ellipsis



   .. py:attribute:: orientations
      :type:  dict[str, int]
      :value: Ellipsis



   .. py:attribute:: active_indicators
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: redundancy
      :type:  dict[str, object]
      :value: Ellipsis



.. py:function:: build_indicator_diagnostics(rows, *, surface_id, indicator_columns, redundancy_rank_corr_threshold, indicator_scales = ...)

.. py:function:: lag_outcome_diagnostic_by_horizon(rows, *, value_column, horizon)

.. py:function:: prune_redundant_indicators(rows, *, indicator_columns, train_validation_scores, threshold)

.. py:function:: diagnostics_summary_markdown(report)

.. py:function:: cast_mapping(value)

.. py:function:: cast_list(value)

