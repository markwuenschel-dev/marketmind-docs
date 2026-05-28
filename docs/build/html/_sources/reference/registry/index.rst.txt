registry
========

.. py:module:: registry


Attributes
----------

.. autoapisummary::

   registry.Factory


Functions
---------

.. autoapisummary::

   registry.register_engine
   registry.resolve_engine
   registry.list_engines
   registry.register_execution_model
   registry.resolve_execution_model
   registry.list_execution_models
   registry.register_cost_model
   registry.resolve_cost_model
   registry.list_cost_models
   registry.register_ledger
   registry.resolve_ledger
   registry.list_ledgers
   registry.register_validator
   registry.resolve_validator
   registry.list_validators
   registry.register_store
   registry.resolve_store
   registry.list_stores


Module Contents
---------------

.. py:data:: Factory
   :type:  Any

.. py:function:: register_engine(component_id, factory)

.. py:function:: resolve_engine(component_id)

.. py:function:: list_engines()

.. py:function:: register_execution_model(component_id, factory)

.. py:function:: resolve_execution_model(component_id)

.. py:function:: list_execution_models()

.. py:function:: register_cost_model(component_id, factory)

.. py:function:: resolve_cost_model(component_id)

.. py:function:: list_cost_models()

.. py:function:: register_ledger(component_id, factory)

.. py:function:: resolve_ledger(component_id)

.. py:function:: list_ledgers()

.. py:function:: register_validator(component_id, factory)

.. py:function:: resolve_validator(component_id)

.. py:function:: list_validators()

.. py:function:: register_store(component_id, factory)

.. py:function:: resolve_store(component_id)

.. py:function:: list_stores()

