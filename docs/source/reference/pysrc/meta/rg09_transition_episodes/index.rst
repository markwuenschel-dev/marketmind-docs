pysrc.meta.rg09_transition_episodes
===================================

.. py:module:: pysrc.meta.rg09_transition_episodes


Classes
-------

.. autoapisummary::

   pysrc.meta.rg09_transition_episodes.TransitionAnchor


Functions
---------

.. autoapisummary::

   pysrc.meta.rg09_transition_episodes.derive_transition_anchored_episodes


Module Contents
---------------

.. py:class:: TransitionAnchor

   .. py:attribute:: entity_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: transition_start_ts
      :type:  pd.Timestamp
      :value: Ellipsis



   .. py:attribute:: transition_end_ts
      :type:  pd.Timestamp
      :value: Ellipsis



   .. py:attribute:: src_regime_class
      :type:  str
      :value: Ellipsis



   .. py:attribute:: dest_regime_class
      :type:  str
      :value: Ellipsis



   .. py:attribute:: stable_bars_before
      :type:  int
      :value: Ellipsis



   .. py:attribute:: stable_bars_after
      :type:  int
      :value: Ellipsis



.. py:function:: derive_transition_anchored_episodes(frame, config, *, fold_construction = ..., require_strict_geometry = ...)

