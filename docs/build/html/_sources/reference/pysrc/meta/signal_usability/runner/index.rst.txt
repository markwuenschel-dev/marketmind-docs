pysrc.meta.signal_usability.runner
==================================

.. py:module:: pysrc.meta.signal_usability.runner


Classes
-------

.. autoapisummary::

   pysrc.meta.signal_usability.runner.SignalUsabilityRunResult


Functions
---------

.. autoapisummary::

   pysrc.meta.signal_usability.runner.load_signal_usability_market_data
   pysrc.meta.signal_usability.runner.build_default_signal_usability_market_data
   pysrc.meta.signal_usability.runner.run_signal_usability_diagnostic
   pysrc.meta.signal_usability.runner.interpret_learnability
   pysrc.meta.signal_usability.runner.run_default_signal_usability_diagnostic


Module Contents
---------------

.. py:class:: SignalUsabilityRunResult

   .. py:attribute:: panel
      :type:  pd.DataFrame
      :value: Ellipsis



   .. py:attribute:: missing_signal_reasons
      :type:  dict[str, str]
      :value: Ellipsis



   .. py:attribute:: baselines
      :type:  dict[str, dict[str, object]]
      :value: Ellipsis



   .. py:attribute:: models
      :type:  dict[str, dict[str, object]]
      :value: Ellipsis



   .. py:attribute:: metrics
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: report_path
      :type:  Path
      :value: Ellipsis



.. py:function:: load_signal_usability_market_data(path)

.. py:function:: build_default_signal_usability_market_data()

.. py:function:: run_signal_usability_diagnostic(*, market_data, config)

.. py:function:: interpret_learnability(*, classification, baselines, metrics, config)

.. py:function:: run_default_signal_usability_diagnostic(*, output_dir = ..., seed = ..., timestamp_utc = ...)

