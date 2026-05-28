pysrc.meta.allocator_benchmark.w3_c_surface_d_audit
===================================================

.. py:module:: pysrc.meta.allocator_benchmark.w3_c_surface_d_audit


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_c_surface_d_audit.W3_C_DEFAULT_OUTPUT_DIR
   pysrc.meta.allocator_benchmark.w3_c_surface_d_audit.W3_B_DEFAULT_CHILD_REPORT
   pysrc.meta.allocator_benchmark.w3_c_surface_d_audit.REFERENCE_LIQUIDITY
   pysrc.meta.allocator_benchmark.w3_c_surface_d_audit.MAX_PENALTY_TERM_CAP


Classes
-------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_c_surface_d_audit.W3CSurfaceDAuditResult


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.w3_c_surface_d_audit.run_w3_c_surface_d_audit
   pysrc.meta.allocator_benchmark.w3_c_surface_d_audit.load_penalty_spec_from_audit
   pysrc.meta.allocator_benchmark.w3_c_surface_d_audit.load_w3_c_config_from_audit


Module Contents
---------------

.. py:data:: W3_C_DEFAULT_OUTPUT_DIR
   :type:  Path
   :value: Ellipsis


.. py:data:: W3_B_DEFAULT_CHILD_REPORT
   :type:  Path
   :value: Ellipsis


.. py:data:: REFERENCE_LIQUIDITY
   :type:  float
   :value: Ellipsis


.. py:data:: MAX_PENALTY_TERM_CAP
   :type:  float
   :value: Ellipsis


.. py:class:: W3CSurfaceDAuditResult

   .. py:attribute:: audit_path
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: audit_report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: penalty_multiplier_spec
      :type:  PenaltyMultiplierSpec
      :value: Ellipsis



.. py:function:: run_w3_c_surface_d_audit(*, w3_b_report_path = ..., output_path = ..., source_path = ..., source_panel = ..., w2_config = ...)

.. py:function:: load_penalty_spec_from_audit(audit_path)

.. py:function:: load_w3_c_config_from_audit(audit_path, *, base = ...)

