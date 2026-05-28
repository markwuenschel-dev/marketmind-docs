pysrc.tuning.core.specs.objective_spec
======================================

.. py:module:: pysrc.tuning.core.specs.objective_spec


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.specs.objective_spec.ObjectiveSpec


Module Contents
---------------

.. py:class:: ObjectiveSpec

   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: spec_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: direction
      :type:  Literal['maximize', 'minimize']
      :value: Ellipsis



   .. py:attribute:: metrics
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: weights
      :type:  dict[str, float]
      :value: Ellipsis



   .. py:attribute:: penalty_refs
      :type:  tuple[str, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: min_sharpe
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: max_turnover
      :type:  float | None
      :value: Ellipsis



