pysrc.preprocessor.api
======================

.. py:module:: pysrc.preprocessor.api


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.api.logger
   pysrc.preprocessor.api.Backend


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.api.PlanSpec
   pysrc.preprocessor.api.ModelRegistry
   pysrc.preprocessor.api.Plan
   pysrc.preprocessor.api.PreprocessorBuilder


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.api.merge_specs
   pysrc.preprocessor.api.resolve_models_in_ops
   pysrc.preprocessor.api.get_executor
   pysrc.preprocessor.api.run
   pysrc.preprocessor.api.stream


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:data:: Backend
   :type:  Any

.. py:class:: PlanSpec

   .. py:attribute:: ops
      :type:  List[Dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: target
      :type:  Optional[Dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: sequence
      :type:  Optional[Dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: scaling
      :type:  Optional[Dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: meta
      :type:  Optional[Dict[str, Any]]
      :value: Ellipsis



.. py:function:: merge_specs(*specs)

.. py:class:: ModelRegistry

   .. py:method:: register(name, obj)


   .. py:method:: get(name)


   .. py:method:: clear()


.. py:function:: resolve_models_in_ops(ops)

.. py:class:: Plan

   .. py:attribute:: ops
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: params
      :type:  Dict[str, List[Dict[str, Any]]]
      :value: Ellipsis



   .. py:attribute:: group_by
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: version
      :type:  str
      :value: Ellipsis



.. py:function:: get_executor(backend = ...)

.. py:function:: run(df, plan, *, backend = ..., optimize = ..., pressure = ..., **_ignored)

.. py:function:: stream(plan, *, backend = ...)

.. py:class:: PreprocessorBuilder(backend = ...)

   .. py:method:: add_op(op_symbol, **params)


   .. py:method:: set_group_by(cols)


   .. py:method:: set_backend(backend)


   .. py:method:: from_dict(cfg)


   .. py:method:: build_plan()


   .. py:method:: build_runner()


   .. py:method:: add_dsl_op(op_symbol, backend_hint = ..., **params)


   .. py:method:: add_sequence(*ops)


   .. py:method:: add_parallel(*builders)


   .. py:method:: add_transform(transform_name, **params)


