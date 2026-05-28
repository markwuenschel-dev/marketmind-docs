pysrc.preprocessor.utils.specs
==============================

.. py:module:: pysrc.preprocessor.utils.specs


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.utils.specs.logger


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.utils.specs.Spec
   pysrc.preprocessor.utils.specs.WindowSpec
   pysrc.preprocessor.utils.specs.GroupSpec
   pysrc.preprocessor.utils.specs.SpecFactory


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.utils.specs.profile_spec


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:class:: Spec

   Bases: :py:obj:`ABC`, :py:obj:`Hashable`


   .. py:method:: to_backend_spec(backend)


   .. py:method:: validate()


.. py:class:: WindowSpec

   Bases: :py:obj:`Spec`


   .. py:attribute:: partition_by
      :type:  Optional[list[str]]
      :value: Ellipsis



   .. py:attribute:: order_by
      :type:  Optional[list[str]]
      :value: Ellipsis



   .. py:attribute:: preceding
      :type:  Optional[int]
      :value: Ellipsis



   .. py:attribute:: following
      :type:  Optional[int]
      :value: Ellipsis



   .. py:attribute:: min_periods
      :type:  int
      :value: Ellipsis



   .. py:method:: validate()


   .. py:method:: to_backend_spec(backend)


.. py:class:: GroupSpec

   Bases: :py:obj:`Spec`


   .. py:attribute:: by
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: as_index
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: sort
      :type:  bool
      :value: Ellipsis



   .. py:method:: validate()


   .. py:method:: to_backend_spec(backend)


.. py:class:: SpecFactory

   .. py:attribute:: registry
      :type:  Dict[str, Callable[Ellipsis, Spec]]
      :value: Ellipsis



   .. py:method:: register(name, builder)


   .. py:method:: build(name, **kwargs)


   .. py:method:: compose(*specs)


.. py:function:: profile_spec(func)

