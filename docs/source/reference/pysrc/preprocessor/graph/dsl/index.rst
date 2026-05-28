pysrc.preprocessor.graph.dsl
============================

.. py:module:: pysrc.preprocessor.graph.dsl


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.graph.dsl.BackendAwareOp
   pysrc.preprocessor.graph.dsl.OpFactory


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.graph.dsl.op
   pysrc.preprocessor.graph.dsl.sequence
   pysrc.preprocessor.graph.dsl.parallel
   pysrc.preprocessor.graph.dsl.combine_ops


Module Contents
---------------

.. py:class:: BackendAwareOp(**params)

   Bases: :py:obj:`Op`


   .. py:method:: to_ir()


.. py:class:: OpFactory

   .. py:method:: create(**params)


.. py:function:: op(op_symbol, backend_hint = ..., **params)

.. py:function:: sequence(*ops)

.. py:function:: parallel(*subgraphs)

.. py:function:: combine_ops(name, *sub_ops, backend_selector = ...)

