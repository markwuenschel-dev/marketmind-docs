pysrc.meta_learning.aq09_ablation_harness
=========================================

.. py:module:: pysrc.meta_learning.aq09_ablation_harness


Attributes
----------

.. autoapisummary::

   pysrc.meta_learning.aq09_ablation_harness.AQ09_ABLATION_REPORT_SCHEMA_VERSION
   pysrc.meta_learning.aq09_ablation_harness.EXPLICIT_LABEL_ARM_NAME
   pysrc.meta_learning.aq09_ablation_harness.REGIME_EMBEDDING_ARM_NAME
   pysrc.meta_learning.aq09_ablation_harness.COMBINED_ARM_NAME


Classes
-------

.. autoapisummary::

   pysrc.meta_learning.aq09_ablation_harness.AQ09AblationArm


Functions
---------

.. autoapisummary::

   pysrc.meta_learning.aq09_ablation_harness.build_aq09_arms_from_tasks
   pysrc.meta_learning.aq09_ablation_harness.run_aq09_ablation_harness
   pysrc.meta_learning.aq09_ablation_harness.write_aq09_ablation_report


Module Contents
---------------

.. py:data:: AQ09_ABLATION_REPORT_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: EXPLICIT_LABEL_ARM_NAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: REGIME_EMBEDDING_ARM_NAME
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: COMBINED_ARM_NAME
   :type:  Final[str]
   :value: Ellipsis


.. py:class:: AQ09AblationArm

   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: features
      :type:  np.ndarray[Any, np.dtype[np.float32]]
      :value: Ellipsis



.. py:function:: build_aq09_arms_from_tasks(tasks, *, include_combined = ...)

.. py:function:: run_aq09_ablation_harness(*, arms, regime_labels, downstream_targets, seed = ..., n_splits = ...)

.. py:function:: write_aq09_ablation_report(path, report)

