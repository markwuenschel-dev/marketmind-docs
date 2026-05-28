pysrc.meta.rg09_boundary_treatment
==================================

.. py:module:: pysrc.meta.rg09_boundary_treatment


Attributes
----------

.. autoapisummary::

   pysrc.meta.rg09_boundary_treatment.RG09BoundaryRecoveryMode
   pysrc.meta.rg09_boundary_treatment.BASELINE_MODE
   pysrc.meta.rg09_boundary_treatment.V1_HYSTERESIS
   pysrc.meta.rg09_boundary_treatment.V2_DWELL
   pysrc.meta.rg09_boundary_treatment.V3_BURST
   pysrc.meta.rg09_boundary_treatment.EPISODE_GROUP_REGIME_COL


Classes
-------

.. autoapisummary::

   pysrc.meta.rg09_boundary_treatment.RG09BoundaryRecoverySpec


Functions
---------

.. autoapisummary::

   pysrc.meta.rg09_boundary_treatment.causal_hysteresis_labels
   pysrc.meta.rg09_boundary_treatment.merge_tiny_transition_bursts
   pysrc.meta.rg09_boundary_treatment.build_entity_local_time_block_frame
   pysrc.meta.rg09_boundary_treatment.attach_episode_group_regime


Module Contents
---------------

.. py:data:: RG09BoundaryRecoveryMode
   :type:  Any

.. py:data:: BASELINE_MODE
   :type:  Final[RG09BoundaryRecoveryMode]
   :value: Ellipsis


.. py:data:: V1_HYSTERESIS
   :type:  Final[RG09BoundaryRecoveryMode]
   :value: Ellipsis


.. py:data:: V2_DWELL
   :type:  Final[RG09BoundaryRecoveryMode]
   :value: Ellipsis


.. py:data:: V3_BURST
   :type:  Final[RG09BoundaryRecoveryMode]
   :value: Ellipsis


.. py:data:: EPISODE_GROUP_REGIME_COL
   :type:  Final[str]
   :value: Ellipsis


.. py:class:: RG09BoundaryRecoverySpec

   .. py:attribute:: mode
      :type:  RG09BoundaryRecoveryMode
      :value: Ellipsis



   .. py:attribute:: max_burst_merge_bars
      :type:  int
      :value: Ellipsis



   .. py:method:: enforce_min_dwell()


   .. py:method:: apply_burst_merge()


   .. py:method:: apply_hysteresis()


.. py:function:: causal_hysteresis_labels(regime_ids, *, confirm_bars)

.. py:function:: merge_tiny_transition_bursts(regime_ids, *, max_burst_bars)

.. py:function:: build_entity_local_time_block_frame(non_cold)

.. py:function:: attach_episode_group_regime(non_cold, config, spec)

