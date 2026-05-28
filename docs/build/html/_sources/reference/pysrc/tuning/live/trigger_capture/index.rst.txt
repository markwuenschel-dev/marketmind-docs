pysrc.tuning.live.trigger_capture
=================================

.. py:module:: pysrc.tuning.live.trigger_capture


Classes
-------

.. autoapisummary::

   pysrc.tuning.live.trigger_capture.DriftTrigger
   pysrc.tuning.live.trigger_capture.TriggerCapture


Module Contents
---------------

.. py:class:: DriftTrigger

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: drift_score
      :type:  float
      :value: Ellipsis



   .. py:attribute:: threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: detected_at
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: feature_hash
      :type:  str
      :value: Ellipsis



.. py:class:: TriggerCapture(threshold, job_id)

   .. py:method:: evaluate(drift_score, feature_hash, now)


