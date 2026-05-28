pysrc.preprocessor.utils.plan_costs
===================================

.. py:module:: pysrc.preprocessor.utils.plan_costs


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.utils.plan_costs.logger


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.utils.plan_costs.PlanSegment
   pysrc.preprocessor.utils.plan_costs.HeuristicPlanner


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.utils.plan_costs.estimate_compute_cost
   pysrc.preprocessor.utils.plan_costs.score_segment


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:class:: PlanSegment

   .. py:attribute:: ops
      :type:  list[Callable]
      :value: Ellipsis



   .. py:attribute:: spec
      :type:  Optional[Spec]
      :value: Ellipsis



   .. py:attribute:: estimated_cost
      :type:  float
      :value: Ellipsis



.. py:function:: estimate_compute_cost(op, backend)

.. py:function:: score_segment(segment, sample_data, backend = ...)

.. py:class:: HeuristicPlanner

   .. py:attribute:: metrics
      :type:  Dict[str, float]
      :value: Ellipsis



   .. py:method:: select_plan(segments, sample_data)


   .. py:method:: optimize(segments, sample_data)


