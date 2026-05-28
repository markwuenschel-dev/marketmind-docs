pysrc.preprocessor.graph.backends.registry
==========================================

.. py:module:: pysrc.preprocessor.graph.backends.registry


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.graph.backends.registry.logger


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.graph.backends.registry.register
   pysrc.preprocessor.graph.backends.registry.get
   pysrc.preprocessor.graph.backends.registry.list_ops
   pysrc.preprocessor.graph.backends.registry.auto_register_from_utils


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:function:: register(backend, op, fn)

.. py:function:: get(backend, op)

.. py:function:: list_ops(backend = ...)

.. py:function:: auto_register_from_utils()

