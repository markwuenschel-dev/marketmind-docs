common.columns
==============

.. py:module:: common.columns


Attributes
----------

.. autoapisummary::

   common.columns.logger


Classes
-------

.. autoapisummary::

   common.columns.ColumnOp
   common.columns.CastNumeric
   common.columns.PromoteCategorical
   common.columns.ColumnOpFactory


Functions
---------

.. autoapisummary::

   common.columns.profile_op
   common.columns.op_chain
   common.columns.live_after
   common.columns.ensure_unique
   common.columns.save_metrics


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:class:: ColumnOp

   Bases: :py:obj:`ABC`


   .. py:method:: apply(df, cols, **kwargs)


   .. py:method:: validate(df, cols)


.. py:function:: profile_op(func)

.. py:class:: CastNumeric

   Bases: :py:obj:`ColumnOp`


   .. py:method:: apply(df, cols, dtype = ..., governed = ...)


.. py:class:: PromoteCategorical

   Bases: :py:obj:`ColumnOp`


   .. py:method:: apply(df, cols, ordered = ..., governed = ..., **kwargs)


.. py:class:: ColumnOpFactory

   .. py:attribute:: registry
      :type:  Dict[str, Callable[Ellipsis, ColumnOp]]
      :value: Ellipsis



   .. py:method:: register(name, op_class)


   .. py:method:: build(name, **kwargs)


.. py:function:: op_chain(*op_names, **kwargs)

.. py:function:: live_after(cols)

.. py:function:: ensure_unique(cols, sep = ...)

.. py:function:: save_metrics(file = ...)

