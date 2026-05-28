pysrc.tuning.config.schemas.objective
=====================================

.. py:module:: pysrc.tuning.config.schemas.objective


Classes
-------

.. autoapisummary::

   pysrc.tuning.config.schemas.objective.ObjectiveConfig


Module Contents
---------------

.. py:class:: ObjectiveConfig

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: direction
      :type:  Literal['maximize', 'minimize']
      :value: Ellipsis



   .. py:attribute:: metrics
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: weights
      :type:  dict[str, float]
      :value: Ellipsis



   .. py:attribute:: penalty_refs
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: min_sharpe
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: max_turnover
      :type:  float | None
      :value: Ellipsis



