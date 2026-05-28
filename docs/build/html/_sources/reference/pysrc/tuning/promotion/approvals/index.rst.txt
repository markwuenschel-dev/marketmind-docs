pysrc.tuning.promotion.approvals
================================

.. py:module:: pysrc.tuning.promotion.approvals


Classes
-------

.. autoapisummary::

   pysrc.tuning.promotion.approvals.ApprovalRecord


Functions
---------

.. autoapisummary::

   pysrc.tuning.promotion.approvals.require_approval


Module Contents
---------------

.. py:class:: ApprovalRecord

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: candidate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: approved
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: approver_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: approved_at
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: notes
      :type:  str
      :value: Ellipsis



.. py:function:: require_approval(job_id, candidate_id, context)

