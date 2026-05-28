marketmind_gate.gates.schema
============================

.. py:module:: marketmind_gate.gates.schema


Classes
-------

.. autoapisummary::

   marketmind_gate.gates.schema.ValidationResult


Functions
---------

.. autoapisummary::

   marketmind_gate.gates.schema.validate_against_schema
   marketmind_gate.gates.schema.load_schema
   marketmind_gate.gates.schema.assert_all_objects_closed


Module Contents
---------------

.. py:class:: ValidationResult

   .. py:attribute:: valid
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: errors
      :type:  list[GateError]
      :value: Ellipsis



.. py:function:: validate_against_schema(instance, schema, *, file = ...)

.. py:function:: load_schema(schema_path)

.. py:function:: assert_all_objects_closed(schema, path = ...)

