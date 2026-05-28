pysrc.tuning.core.ir.task_ir
============================

.. py:module:: pysrc.tuning.core.ir.task_ir


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.ir.task_ir.FoldBoundary
   pysrc.tuning.core.ir.task_ir.TaskIR


Module Contents
---------------

.. py:class:: FoldBoundary

   .. py:attribute:: fold_index
      :type:  int
      :value: Ellipsis



   .. py:attribute:: train_start
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: train_end
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: test_start
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: test_end
      :type:  datetime
      :value: Ellipsis



.. py:class:: TaskIR

   .. py:attribute:: task_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: candidate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: fold
      :type:  FoldBoundary
      :value: Ellipsis



   .. py:attribute:: params
      :type:  tuple[HParam, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: feature_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: meta
      :type:  IRMetadata
      :value: Ellipsis



   .. py:attribute:: symbol
      :type:  str
      :value: Ellipsis



   .. py:attribute:: regime_label
      :type:  str
      :value: Ellipsis



