pysrc.preprocessor.graph.graph
==============================

.. py:module:: pysrc.preprocessor.graph.graph


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.graph.graph.Node
   pysrc.preprocessor.graph.graph.SimpleNode
   pysrc.preprocessor.graph.graph.FusedNode
   pysrc.preprocessor.graph.graph.Graph


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.graph.graph.register_node_factory
   pysrc.preprocessor.graph.graph.serialize
   pysrc.preprocessor.graph.graph.deserialize


Module Contents
---------------

.. py:class:: Node(op)

   Bases: :py:obj:`ABC`


   .. py:method:: to_ir()


.. py:class:: SimpleNode(op)

   Bases: :py:obj:`Node`


   .. py:method:: to_ir()


.. py:class:: FusedNode(sub_ops, fused_kind)

   Bases: :py:obj:`Node`


   .. py:method:: to_ir()


.. py:function:: register_node_factory(key, factory)

.. py:class:: Graph

   .. py:method:: add_op(op)


   .. py:method:: merge(other)


   .. py:method:: optimize()


   .. py:method:: topological_sort()


   .. py:method:: has_cycle()


   .. py:method:: shortest_path(start, end)


   .. py:method:: connected_components()


.. py:function:: serialize(graph)

.. py:function:: deserialize(data)

