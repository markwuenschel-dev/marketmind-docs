pysrc.tuning.specs
==================

.. py:module:: pysrc.tuning.specs


Attributes
----------

.. autoapisummary::

   pysrc.tuning.specs.ObjectiveDirection
   pysrc.tuning.specs.ParamValue
   pysrc.tuning.specs.ParamPoint


Classes
-------

.. autoapisummary::

   pysrc.tuning.specs.TunerSpec
   pysrc.tuning.specs.TrialRecord
   pysrc.tuning.specs.TuningResult
   pysrc.tuning.specs.TuningEngine


Module Contents
---------------

.. py:data:: ObjectiveDirection
   :type:  Any

.. py:data:: ParamValue
   :type:  Any

.. py:data:: ParamPoint
   :type:  Any

.. py:class:: TunerSpec

   .. py:attribute:: engine
      :type:  str
      :value: Ellipsis



   .. py:attribute:: direction
      :type:  ObjectiveDirection
      :value: Ellipsis



   .. py:attribute:: budget
      :type:  int
      :value: Ellipsis



   .. py:attribute:: cv
      :type:  int
      :value: Ellipsis



   .. py:attribute:: scoring
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: seed
      :type:  Optional[int]
      :value: Ellipsis



   .. py:attribute:: engine_kwargs
      :type:  Dict[str, Any]
      :value: Ellipsis



.. py:class:: TrialRecord

   .. py:attribute:: params
      :type:  ParamPoint
      :value: Ellipsis



   .. py:attribute:: score
      :type:  float
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  Dict[str, Any]
      :value: Ellipsis



.. py:class:: TuningResult

   .. py:attribute:: best_params
      :type:  ParamPoint
      :value: Ellipsis



   .. py:attribute:: best_score
      :type:  float
      :value: Ellipsis



   .. py:attribute:: best_model
      :type:  Optional[Any]
      :value: Ellipsis



   .. py:attribute:: trials
      :type:  List[TrialRecord]
      :value: Ellipsis



   .. py:attribute:: engine
      :type:  str
      :value: Ellipsis



   .. py:attribute:: direction
      :type:  ObjectiveDirection
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  Dict[str, Any]
      :value: Ellipsis



.. py:class:: TuningEngine

