pysrc.tuning.reports.gate_report
================================

.. py:module:: pysrc.tuning.reports.gate_report


Classes
-------

.. autoapisummary::

   pysrc.tuning.reports.gate_report.GateReport


Functions
---------

.. autoapisummary::

   pysrc.tuning.reports.gate_report.render_gate_report


Module Contents
---------------

.. py:class:: GateReport

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: candidate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: overall_passed
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: gate_scores
      :type:  dict[str, float]
      :value: Ellipsis



   .. py:attribute:: gate_passed
      :type:  dict[str, bool]
      :value: Ellipsis



   .. py:attribute:: dsr
      :type:  float
      :value: Ellipsis



   .. py:attribute:: t_stat
      :type:  float
      :value: Ellipsis



.. py:function:: render_gate_report(artifact)

