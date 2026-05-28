pysrc.preprocessor.graph.ops
============================

.. py:module:: pysrc.preprocessor.graph.ops


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.graph.ops.OpKind
   pysrc.preprocessor.graph.ops.Op
   pysrc.preprocessor.graph.ops.ElementwiseOp
   pysrc.preprocessor.graph.ops.RollingOp
   pysrc.preprocessor.graph.ops.SequenceOp
   pysrc.preprocessor.graph.ops.ScalingOp
   pysrc.preprocessor.graph.ops.ExternalOp


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.graph.ops.get_registry


Module Contents
---------------

.. py:class:: OpKind

   Bases: :py:obj:`str`, :py:obj:`Enum`


   str(object='') -> str
   str(bytes_or_buffer[, encoding[, errors]]) -> str

   Create a new string object from the given object. If encoding or
   errors is specified, then the object must expose a data buffer
   that will be decoded using the given encoding and error handler.
   Otherwise, returns the result of object.__str__() (if defined)
   or repr(object).
   encoding defaults to sys.getdefaultencoding().
   errors defaults to 'strict'.


   .. py:attribute:: elementwise
      :type:  Any


   .. py:attribute:: rolling
      :type:  Any


   .. py:attribute:: sequence
      :type:  Any


   .. py:attribute:: scaling
      :type:  Any


   .. py:attribute:: external
      :type:  Any


.. py:class:: Op(**params)

   Bases: :py:obj:`ABC`


   .. py:attribute:: NAME
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: KIND
      :type:  OpKind
      :value: Ellipsis



   .. py:method:: name()


   .. py:method:: validate_params()


   .. py:method:: requires()


   .. py:method:: provides()


   .. py:method:: is_fittable()


   .. py:method:: state_dict()


   .. py:method:: load_state_dict(state)


   .. py:method:: clone()


   .. py:method:: to_ir()


.. py:class:: ElementwiseOp(**params)

   Bases: :py:obj:`Op`


   .. py:attribute:: KIND
      :type:  Any


   .. py:method:: to_ir()


.. py:class:: RollingOp(**params)

   Bases: :py:obj:`Op`


   .. py:attribute:: KIND
      :type:  Any


   .. py:method:: to_ir()


.. py:class:: SequenceOp(**params)

   Bases: :py:obj:`Op`


   .. py:attribute:: KIND
      :type:  Any


   .. py:method:: to_ir()


.. py:class:: ScalingOp(**params)

   Bases: :py:obj:`Op`


   .. py:attribute:: KIND
      :type:  Any


   .. py:method:: is_fittable()


   .. py:method:: to_ir()


.. py:class:: ExternalOp(**params)

   Bases: :py:obj:`Op`


   .. py:attribute:: KIND
      :type:  Any


   .. py:method:: to_ir()


.. py:function:: get_registry()

