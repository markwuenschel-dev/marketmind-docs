pysrc.tuning.reports.tuning_report
==================================

.. py:module:: pysrc.tuning.reports.tuning_report


Classes
-------

.. autoapisummary::

   pysrc.tuning.reports.tuning_report.TuningReport


Functions
---------

.. autoapisummary::

   pysrc.tuning.reports.tuning_report.render_tuning_report


Module Contents
---------------

.. py:class:: TuningReport

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: spec_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: best_candidate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: best_score
      :type:  float
      :value: Ellipsis



   .. py:attribute:: n_trials
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_folds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: algorithm
      :type:  str
      :value: Ellipsis



   .. py:attribute:: gate_passed
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: tags
      :type:  dict[str, str]
      :value: Ellipsis



.. py:function:: render_tuning_report(artifact)

