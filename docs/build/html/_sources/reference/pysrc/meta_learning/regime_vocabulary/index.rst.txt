pysrc.meta_learning.regime_vocabulary
=====================================

.. py:module:: pysrc.meta_learning.regime_vocabulary


Attributes
----------

.. autoapisummary::

   pysrc.meta_learning.regime_vocabulary.RegimeClassLabel
   pysrc.meta_learning.regime_vocabulary.TrendBucket
   pysrc.meta_learning.regime_vocabulary.VolBucket
   pysrc.meta_learning.regime_vocabulary.BocpdState
   pysrc.meta_learning.regime_vocabulary.REGIME_CLASS_BULL
   pysrc.meta_learning.regime_vocabulary.REGIME_CLASS_BEAR
   pysrc.meta_learning.regime_vocabulary.REGIME_CLASS_SIDEWAYS
   pysrc.meta_learning.regime_vocabulary.REGIME_CLASS_HIGH_VOL
   pysrc.meta_learning.regime_vocabulary.REGIME_CLASS_CRISIS
   pysrc.meta_learning.regime_vocabulary.REGIME_CLASSES
   pysrc.meta_learning.regime_vocabulary.REGIME_CLASS_ORDER
   pysrc.meta_learning.regime_vocabulary.VOL_RISING_REGIME_CLASSES
   pysrc.meta_learning.regime_vocabulary.TREND_STABLE_REGIME_CLASSES
   pysrc.meta_learning.regime_vocabulary.PROJECTION_RULE_LOGIC_ID_DEFAULT
   pysrc.meta_learning.regime_vocabulary.PROJECTION_RULE_REFERENCE_BOCPD_ID
   pysrc.meta_learning.regime_vocabulary.PROJECTION_RULE_EXTENDED_ABLATION_ID
   pysrc.meta_learning.regime_vocabulary.DEFAULT_CRISIS_VOL_SCORE_PERCENTILE


Functions
---------

.. autoapisummary::

   pysrc.meta_learning.regime_vocabulary.projection_rule_display
   pysrc.meta_learning.regime_vocabulary.projection_rule_version_id
   pysrc.meta_learning.regime_vocabulary.validate_regime_class
   pysrc.meta_learning.regime_vocabulary.is_valid_compositional_regime_id
   pysrc.meta_learning.regime_vocabulary.validate_compositional_regime_id
   pysrc.meta_learning.regime_vocabulary.validate_meta_task_regime_id
   pysrc.meta_learning.regime_vocabulary.validate_row_count_dict_keys
   pysrc.meta_learning.regime_vocabulary.project_regime_class
   pysrc.meta_learning.regime_vocabulary.project_regime_class_bocpd_reference
   pysrc.meta_learning.regime_vocabulary.project_regime_class_extended_ablation


Module Contents
---------------

.. py:data:: RegimeClassLabel
   :type:  Any

.. py:data:: TrendBucket
   :type:  Any

.. py:data:: VolBucket
   :type:  Any

.. py:data:: BocpdState
   :type:  Any

.. py:data:: REGIME_CLASS_BULL
   :type:  RegimeClassLabel
   :value: Ellipsis


.. py:data:: REGIME_CLASS_BEAR
   :type:  RegimeClassLabel
   :value: Ellipsis


.. py:data:: REGIME_CLASS_SIDEWAYS
   :type:  RegimeClassLabel
   :value: Ellipsis


.. py:data:: REGIME_CLASS_HIGH_VOL
   :type:  RegimeClassLabel
   :value: Ellipsis


.. py:data:: REGIME_CLASS_CRISIS
   :type:  RegimeClassLabel
   :value: Ellipsis


.. py:data:: REGIME_CLASSES
   :type:  Final[frozenset[str]]
   :value: Ellipsis


.. py:data:: REGIME_CLASS_ORDER
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:data:: VOL_RISING_REGIME_CLASSES
   :type:  Final[frozenset[str]]
   :value: Ellipsis


.. py:data:: TREND_STABLE_REGIME_CLASSES
   :type:  Final[frozenset[str]]
   :value: Ellipsis


.. py:data:: PROJECTION_RULE_LOGIC_ID_DEFAULT
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: PROJECTION_RULE_REFERENCE_BOCPD_ID
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: PROJECTION_RULE_EXTENDED_ABLATION_ID
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: DEFAULT_CRISIS_VOL_SCORE_PERCENTILE
   :type:  Final[float]
   :value: Ellipsis


.. py:function:: projection_rule_display(*, severity_percentile)

.. py:function:: projection_rule_version_id(*, severity_percentile)

.. py:function:: validate_regime_class(value)

.. py:function:: is_valid_compositional_regime_id(regime_id)

.. py:function:: validate_compositional_regime_id(regime_id)

.. py:function:: validate_meta_task_regime_id(regime_id)

.. py:function:: validate_row_count_dict_keys(counts)

.. py:function:: project_regime_class(trend, vol, bocpd_state, *, severity_flag)

.. py:function:: project_regime_class_bocpd_reference(trend, vol, bocpd_state)

.. py:function:: project_regime_class_extended_ablation(trend, vol, bocpd_state)

