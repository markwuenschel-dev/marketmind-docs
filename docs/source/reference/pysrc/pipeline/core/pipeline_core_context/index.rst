pysrc.pipeline.core.pipeline_core_context
=========================================

.. py:module:: pysrc.pipeline.core.pipeline_core_context


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.core.pipeline_core_context.pd
   pysrc.pipeline.core.pipeline_core_context.pl
   pysrc.pipeline.core.pipeline_core_context.TimeFreq


Classes
-------

.. autoapisummary::

   pysrc.pipeline.core.pipeline_core_context.PipelineContext


Module Contents
---------------

.. py:data:: pd
   :type:  Any

.. py:data:: pl
   :type:  Any

.. py:data:: TimeFreq
   :type:  Any

.. py:class:: PipelineContext

   .. py:attribute:: frequency
      :type:  TimeFreq
      :value: Ellipsis



   .. py:attribute:: asset_class
      :type:  str
      :value: Ellipsis



   .. py:attribute:: latency
      :type:  Literal['ultra', 'low', 'batch']
      :value: Ellipsis



   .. py:attribute:: streaming
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: time_col
      :type:  str
      :value: Ellipsis



   .. py:attribute:: df
      :type:  Optional[Union[pl, pl, pd]]
      :value: Ellipsis



   .. py:attribute:: assume_sorted
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: sample
      :type:  int
      :value: Ellipsis



   .. py:attribute:: backend
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: executor
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: optimize
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: cache
      :type:  bool
      :value: Ellipsis



   .. py:method:: as_lazy()


   .. py:method:: infer_frequency()


   .. py:method:: refine(**kwargs)


