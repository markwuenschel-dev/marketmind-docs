pysrc.preprocessor.graph.factory
================================

.. py:module:: pysrc.preprocessor.graph.factory


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.graph.factory.logger
   pysrc.preprocessor.graph.factory.ExprFactory
   pysrc.preprocessor.graph.factory.TransformFactory


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.graph.factory.OpSpec


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.graph.factory.register
   pysrc.preprocessor.graph.factory.register_alias
   pysrc.preprocessor.graph.factory.resolve_name
   pysrc.preprocessor.graph.factory.build_graph
   pysrc.preprocessor.graph.factory.registry_snapshot
   pysrc.preprocessor.graph.factory.register_builtin_ops


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:data:: ExprFactory
   :type:  Any

.. py:data:: TransformFactory
   :type:  Any

.. py:class:: OpSpec

   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: params
      :type:  Dict[str, Any]
      :value: Ellipsis



.. py:function:: register(name, op_cls)

.. py:function:: register_alias(alias, target)

.. py:function:: resolve_name(name)

.. py:function:: build_graph(ops, params)

.. py:function:: registry_snapshot()

.. py:function:: register_builtin_ops()

