pysrc.preprocessor.utils.expr_builders
======================================

.. py:module:: pysrc.preprocessor.utils.expr_builders


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.utils.expr_builders.Expr
   pysrc.preprocessor.utils.expr_builders.ExprFactory


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.utils.expr_builders.register_expr
   pysrc.preprocessor.utils.expr_builders.safe_div_builder
   pysrc.preprocessor.utils.expr_builders.zscore_builder
   pysrc.preprocessor.utils.expr_builders.bollinger_builder


Module Contents
---------------

.. py:function:: register_expr(name, builder)

.. py:class:: Expr(func)

.. py:class:: ExprFactory

   .. py:attribute:: registry
      :type:  Dict[str, Callable[Ellipsis, Any]]
      :value: Ellipsis



   .. py:method:: register(name, builder)


   .. py:method:: build(name, **kwargs)


.. py:function:: safe_div_builder(eps = ..., backend = ...)

.. py:function:: zscore_builder(col, mean = ..., std = ..., backend = ...)

.. py:function:: bollinger_builder(col, window = ..., num_std = ..., backend = ...)

