pysrc.meta.execution_assumptions_config
=======================================

.. py:module:: pysrc.meta.execution_assumptions_config


Attributes
----------

.. autoapisummary::

   pysrc.meta.execution_assumptions_config.DEFAULT_OUTPUT_DIR
   pysrc.meta.execution_assumptions_config.GOVERNED_SCHEMA_VERSION


Classes
-------

.. autoapisummary::

   pysrc.meta.execution_assumptions_config.ExecutionParityDeclaration
   pysrc.meta.execution_assumptions_config.ExecutionAssumptionsConfig


Module Contents
---------------

.. py:data:: DEFAULT_OUTPUT_DIR
   :type:  Any

.. py:data:: GOVERNED_SCHEMA_VERSION
   :type:  Any

.. py:class:: ExecutionParityDeclaration

   .. py:attribute:: cost_assumptions_match_baseline
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: split_assumptions_match_baseline
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: data_assumptions_match_baseline
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: parity_note
      :type:  str
      :value: Ellipsis



   .. py:method:: to_json_obj()


.. py:class:: ExecutionAssumptionsConfig

   .. py:attribute:: run_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: cost_bps
      :type:  float
      :value: Ellipsis



   .. py:attribute:: slippage_model
      :type:  str
      :value: Ellipsis



   .. py:attribute:: slippage_bps_estimate
      :type:  float
      :value: Ellipsis



   .. py:attribute:: borrow_rate_annual_bps
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: latency_model
      :type:  str
      :value: Ellipsis



   .. py:attribute:: fill_assumption
      :type:  str
      :value: Ellipsis



   .. py:attribute:: parity
      :type:  ExecutionParityDeclaration
      :value: Ellipsis



   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: output_dir
      :type:  str
      :value: Ellipsis



   .. py:method:: with_updates(**changes)


