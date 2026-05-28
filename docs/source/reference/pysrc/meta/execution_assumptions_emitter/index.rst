pysrc.meta.execution_assumptions_emitter
========================================

.. py:module:: pysrc.meta.execution_assumptions_emitter


Attributes
----------

.. autoapisummary::

   pysrc.meta.execution_assumptions_emitter.SCHEMA_VERSION
   pysrc.meta.execution_assumptions_emitter.GOVERNED_SCHEMA_VERSION
   pysrc.meta.execution_assumptions_emitter.CONTENT_HASH_ALGORITHM
   pysrc.meta.execution_assumptions_emitter.CONTENT_HASH_CANONICALIZATION
   pysrc.meta.execution_assumptions_emitter.GOVERNED_CONTENT_HASH_ALGORITHM
   pysrc.meta.execution_assumptions_emitter.GOVERNED_CONTENT_HASH_CANONICALIZATION


Classes
-------

.. autoapisummary::

   pysrc.meta.execution_assumptions_emitter.ExecutionAssumptionsReport


Functions
---------

.. autoapisummary::

   pysrc.meta.execution_assumptions_emitter.build_execution_assumptions_document
   pysrc.meta.execution_assumptions_emitter.emit_execution_assumptions
   pysrc.meta.execution_assumptions_emitter.recompute_execution_assumptions_content_hash_from_document
   pysrc.meta.execution_assumptions_emitter.emit_governed_execution_assumptions
   pysrc.meta.execution_assumptions_emitter.build_governed_execution_assumptions_document
   pysrc.meta.execution_assumptions_emitter.validate_governed_execution_assumptions_document


Module Contents
---------------

.. py:data:: SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: GOVERNED_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: CONTENT_HASH_ALGORITHM
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: CONTENT_HASH_CANONICALIZATION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: GOVERNED_CONTENT_HASH_ALGORITHM
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: GOVERNED_CONTENT_HASH_CANONICALIZATION
   :type:  Final[str]
   :value: Ellipsis


.. py:class:: ExecutionAssumptionsReport

   .. py:attribute:: document
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: content_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:method:: to_json_document()


.. py:function:: build_execution_assumptions_document(*, run_identity)

.. py:function:: emit_execution_assumptions(output_path, *, seed)

.. py:function:: recompute_execution_assumptions_content_hash_from_document(document)

.. py:function:: emit_governed_execution_assumptions(config)

.. py:function:: build_governed_execution_assumptions_document(config)

.. py:function:: validate_governed_execution_assumptions_document(document)

