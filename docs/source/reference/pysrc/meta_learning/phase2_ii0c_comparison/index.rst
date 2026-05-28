pysrc.meta_learning.phase2_ii0c_comparison
==========================================

.. py:module:: pysrc.meta_learning.phase2_ii0c_comparison


Attributes
----------

.. autoapisummary::

   pysrc.meta_learning.phase2_ii0c_comparison.XGBOOST_INCUMBENT_BASELINE_KIND
   pysrc.meta_learning.phase2_ii0c_comparison.NOT_EVALUATED_NON_PROMOTABLE
   pysrc.meta_learning.phase2_ii0c_comparison.II0C_COMPARISON_LANE
   pysrc.meta_learning.phase2_ii0c_comparison.GOVERNED_BASELINE_COMPARISON_KEYS


Exceptions
----------

.. autoapisummary::

   pysrc.meta_learning.phase2_ii0c_comparison.Phase2II0CComparisonError


Classes
-------

.. autoapisummary::

   pysrc.meta_learning.phase2_ii0c_comparison.Phase2II0CComparisonSpec
   pysrc.meta_learning.phase2_ii0c_comparison.Phase2II0CComparisonBundle
   pysrc.meta_learning.phase2_ii0c_comparison.II0CComparisonContext


Functions
---------

.. autoapisummary::

   pysrc.meta_learning.phase2_ii0c_comparison.validate_phase2_ii0c_comparison_spec
   pysrc.meta_learning.phase2_ii0c_comparison.build_phase2_ii0c_baseline_comparison
   pysrc.meta_learning.phase2_ii0c_comparison.build_phase2_ii0c_shared_comparison_context
   pysrc.meta_learning.phase2_ii0c_comparison.build_phase2_ii0c_comparison_bundle
   pysrc.meta_learning.phase2_ii0c_comparison.validate_ii0c_governed_baseline_and_shared_context
   pysrc.meta_learning.phase2_ii0c_comparison.build_ii0c_comparison_payload


Module Contents
---------------

.. py:data:: XGBOOST_INCUMBENT_BASELINE_KIND
   :type:  str
   :value: Ellipsis


.. py:data:: NOT_EVALUATED_NON_PROMOTABLE
   :type:  str
   :value: Ellipsis


.. py:data:: II0C_COMPARISON_LANE
   :type:  str
   :value: Ellipsis


.. py:data:: GOVERNED_BASELINE_COMPARISON_KEYS
   :type:  frozenset[str]
   :value: Ellipsis


.. py:exception:: Phase2II0CComparisonError

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:class:: Phase2II0CComparisonSpec

   .. py:attribute:: challenger_run_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: baseline_run_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: splits_fingerprint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: data_fingerprint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: cost_assumptions_fingerprint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: baseline_kind
      :type:  str
      :value: Ellipsis



   .. py:attribute:: data_parity
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: split_parity
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: cost_parity
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: net_result_against_incumbent
      :type:  str
      :value: Ellipsis



.. py:class:: Phase2II0CComparisonBundle

   .. py:attribute:: baseline_comparison
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: shared_comparison_context
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:class:: II0CComparisonContext

   .. py:attribute:: baseline_run_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: challenger_run_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: incumbent_data_fingerprint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: challenger_data_fingerprint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: incumbent_splits_fingerprint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: challenger_splits_fingerprint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: incumbent_cost_assumptions_fingerprint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: challenger_cost_assumptions_fingerprint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: baseline_kind
      :type:  str
      :value: Ellipsis



   .. py:attribute:: net_result_against_incumbent
      :type:  str
      :value: Ellipsis



.. py:function:: validate_phase2_ii0c_comparison_spec(spec)

.. py:function:: build_phase2_ii0c_baseline_comparison(spec)

.. py:function:: build_phase2_ii0c_shared_comparison_context(spec)

.. py:function:: build_phase2_ii0c_comparison_bundle(spec)

.. py:function:: validate_ii0c_governed_baseline_and_shared_context(*, baseline_comparison, shared_comparison_context)

.. py:function:: build_ii0c_comparison_payload(context)

