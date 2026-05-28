pysrc.tuning.live.runtime_state
===============================

.. py:module:: pysrc.tuning.live.runtime_state


Classes
-------

.. autoapisummary::

   pysrc.tuning.live.runtime_state.RuntimeState


Module Contents
---------------

.. py:class:: RuntimeState

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: active_artifact_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: activated_at
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: shadow_candidate_id
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: last_drift_score
      :type:  float
      :value: Ellipsis



   .. py:attribute:: last_retrain_at
      :type:  datetime | None
      :value: Ellipsis



   .. py:attribute:: tags
      :type:  dict[str, str]
      :value: Ellipsis



   .. py:method:: update_drift(score)


   .. py:method:: record_retrain(now)


