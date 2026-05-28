pysrc.strategies.stat_arb.entry
===============================

.. py:module:: pysrc.strategies.stat_arb.entry


Classes
-------

.. autoapisummary::

   pysrc.strategies.stat_arb.entry.StatArbRunConfig


Functions
---------

.. autoapisummary::

   pysrc.strategies.stat_arb.entry.run_stat_arb_pairs


Module Contents
---------------

.. py:class:: StatArbRunConfig

   .. py:attribute:: leg_a
      :type:  str
      :value: Ellipsis



   .. py:attribute:: leg_b
      :type:  str
      :value: Ellipsis



   .. py:attribute:: start
      :type:  str
      :value: Ellipsis



   .. py:attribute:: end
      :type:  str
      :value: Ellipsis



   .. py:attribute:: config
      :type:  PairsConfig
      :value: Ellipsis



   .. py:attribute:: bundle_dir
      :type:  Path | None
      :value: Ellipsis



   .. py:attribute:: prices
      :type:  pd.DataFrame | None
      :value: Ellipsis



.. py:function:: run_stat_arb_pairs(leg_a, leg_b, *, run_cfg)

