pysrc.meta.anti_signal_autopsy
==============================

.. py:module:: pysrc.meta.anti_signal_autopsy


Attributes
----------

.. autoapisummary::

   pysrc.meta.anti_signal_autopsy.ALERT_DUPLICATE_TASK_ID_IN_EVAL
   pysrc.meta.anti_signal_autopsy.ALERT_MISSING_QUERY_TARGET
   pysrc.meta.anti_signal_autopsy.ALERT_MISSING_CHALLENGER_SCORE
   pysrc.meta.anti_signal_autopsy.ALERT_MISSING_BASELINE_SCORE
   pysrc.meta.anti_signal_autopsy.ALERT_TRAIN_EVAL_OVERLAP
   pysrc.meta.anti_signal_autopsy.ALERT_SUPPORT_END_AFTER_QUERY_START
   pysrc.meta.anti_signal_autopsy.ALERT_TASK_ID_JOIN_MISMATCH
   pysrc.meta.anti_signal_autopsy.ALERT_FOLD_ID_JOIN_MISMATCH
   pysrc.meta.anti_signal_autopsy.ALERT_MANY_TO_ONE_JOIN_EXPANSION
   pysrc.meta.anti_signal_autopsy.PRIMARY_INVALID_ALIGNMENT
   pysrc.meta.anti_signal_autopsy.PRIMARY_INCONCLUSIVE
   pysrc.meta.anti_signal_autopsy.PRIMARY_SIGN_INVERSION
   pysrc.meta.anti_signal_autopsy.PRIMARY_SUPPORT_QUERY_REVERSAL
   pysrc.meta.anti_signal_autopsy.PRIMARY_COST_INVERSION
   pysrc.meta.anti_signal_autopsy.PRIMARY_UNCLASSIFIED


Classes
-------

.. autoapisummary::

   pysrc.meta.anti_signal_autopsy.AutopsyContext
   pysrc.meta.anti_signal_autopsy.CanonicalTaskTable


Functions
---------

.. autoapisummary::

   pysrc.meta.anti_signal_autopsy.choose_latest_governed_w1_run
   pysrc.meta.anti_signal_autopsy.load_autopsy_context
   pysrc.meta.anti_signal_autopsy.build_canonical_task_table
   pysrc.meta.anti_signal_autopsy.run_alignment_audit
   pysrc.meta.anti_signal_autopsy.assemble_final_report
   pysrc.meta.anti_signal_autopsy.run_lane
   pysrc.meta.anti_signal_autopsy.main


Module Contents
---------------

.. py:data:: ALERT_DUPLICATE_TASK_ID_IN_EVAL
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_MISSING_QUERY_TARGET
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_MISSING_CHALLENGER_SCORE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_MISSING_BASELINE_SCORE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_TRAIN_EVAL_OVERLAP
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_SUPPORT_END_AFTER_QUERY_START
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_TASK_ID_JOIN_MISMATCH
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_FOLD_ID_JOIN_MISMATCH
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: ALERT_MANY_TO_ONE_JOIN_EXPANSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: PRIMARY_INVALID_ALIGNMENT
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: PRIMARY_INCONCLUSIVE
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: PRIMARY_SIGN_INVERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: PRIMARY_SUPPORT_QUERY_REVERSAL
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: PRIMARY_COST_INVERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: PRIMARY_UNCLASSIFIED
   :type:  Final[str]
   :value: Ellipsis


.. py:class:: AutopsyContext

   .. py:attribute:: repo_root
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: phase_ii_root
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: run_root
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: comparison_run_root
      :type:  Path | None
      :value: Ellipsis



   .. py:attribute:: output_root
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: agent_output_root
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: task_manifest
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: meta_validity_report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: execution_assumptions
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: baseline_report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: challenger_surface
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: close_by_day
      :type:  dict[str, float]
      :value: Ellipsis



.. py:class:: CanonicalTaskTable

   .. py:attribute:: rows
      :type:  tuple[dict[str, object], Ellipsis]
      :value: Ellipsis



   .. py:attribute:: schema
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: missing_fields
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



.. py:function:: choose_latest_governed_w1_run(phase_ii_root = ...)

.. py:function:: load_autopsy_context(run_root = ...)

.. py:function:: build_canonical_task_table(ctx)

.. py:function:: run_alignment_audit(ctx, table)

.. py:function:: assemble_final_report(agent_payloads)

.. py:function:: run_lane(lane, run_root = ...)

.. py:function:: main(argv = ...)

