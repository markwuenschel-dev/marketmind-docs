pysrc.preprocessor.graph.expr
=============================

.. py:module:: pysrc.preprocessor.graph.expr


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.graph.expr.logger


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.graph.expr.ExprMeta
   pysrc.preprocessor.graph.expr.Expr
   pysrc.preprocessor.graph.expr.Column
   pysrc.preprocessor.graph.expr.Literal
   pysrc.preprocessor.graph.expr.OpExpr


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.graph.expr.register_expr
   pysrc.preprocessor.graph.expr.expr_factory
   pysrc.preprocessor.graph.expr.optimize
   pysrc.preprocessor.graph.expr.register_builtin_builders
   pysrc.preprocessor.graph.expr.create_sequence_lag
   pysrc.preprocessor.graph.expr.create_rolling_mean
   pysrc.preprocessor.graph.expr.create_rolling_std
   pysrc.preprocessor.graph.expr.fuse_expressions
   pysrc.preprocessor.graph.expr.register_polars_lowering
   pysrc.preprocessor.graph.expr.get_polars_lowering


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:function:: register_expr(op, builder)

.. py:class:: ExprMeta

   Bases: :py:obj:`ABCMeta`


.. py:class:: Expr(args = ..., params = ...)

   Bases: :py:obj:`ABC`


   .. py:attribute:: op
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: args
      :type:  Sequence[Expr]
      :value: Ellipsis



   .. py:attribute:: params
      :type:  Dict[str, Any]
      :value: Ellipsis



   .. py:method:: validate()


   .. py:method:: to_ir()


   .. py:method:: optimize()


.. py:class:: Column(name)

   Bases: :py:obj:`Expr`


   .. py:attribute:: op
      :type:  Any


   .. py:method:: validate()


   .. py:method:: to_ir()


.. py:class:: Literal(value)

   Bases: :py:obj:`Expr`


   .. py:attribute:: op
      :type:  Any


   .. py:method:: to_ir()


.. py:class:: OpExpr(op, args, params = ...)

   Bases: :py:obj:`Expr`


   .. py:method:: to_ir()


   .. py:method:: optimize()


.. py:function:: expr_factory(op, *args, **params)

.. py:function:: optimize(expr)

.. py:function:: register_builtin_builders()

.. py:function:: create_sequence_lag(col, k, prefix = ...)

.. py:function:: create_rolling_mean(col, window)

.. py:function:: create_rolling_std(col, window)

.. py:function:: fuse_expressions(exprs, fused_name = ...)

.. py:function:: register_polars_lowering(op_name, fn)

.. py:function:: get_polars_lowering(op_name)

