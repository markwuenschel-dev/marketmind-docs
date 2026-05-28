pysrc.pipeline.core.pipeline_core_base
======================================

.. py:module:: pysrc.pipeline.core.pipeline_core_base


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.core.pipeline_core_base.pd
   pysrc.pipeline.core.pipeline_core_base.pl
   pysrc.pipeline.core.pipeline_core_base.InT
   pysrc.pipeline.core.pipeline_core_base.OutT
   pysrc.pipeline.core.pipeline_core_base.Engine


Exceptions
----------

.. autoapisummary::

   pysrc.pipeline.core.pipeline_core_base.PipelineError
   pysrc.pipeline.core.pipeline_core_base.PipelineGraphError
   pysrc.pipeline.core.pipeline_core_base.PipelineConfigError
   pysrc.pipeline.core.pipeline_core_base.DataError
   pysrc.pipeline.core.pipeline_core_base.MissingDataError
   pysrc.pipeline.core.pipeline_core_base.InvalidSchemaError


Classes
-------

.. autoapisummary::

   pysrc.pipeline.core.pipeline_core_base.ErrorCode
   pysrc.pipeline.core.pipeline_core_base.DataSource
   pysrc.pipeline.core.pipeline_core_base.PipelineStep
   pysrc.pipeline.core.pipeline_core_base.CompositeStep


Module Contents
---------------

.. py:data:: pd
   :type:  Any

.. py:data:: pl
   :type:  Any

.. py:data:: InT
   :type:  Any

.. py:data:: OutT
   :type:  Any

.. py:data:: Engine
   :type:  Any

.. py:exception:: PipelineError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


   .. py:attribute:: code
      :type:  Any


   .. py:method:: to_dict()


.. py:exception:: PipelineGraphError

   Bases: :py:obj:`PipelineError`


   Common base class for all non-exit exceptions.


   .. py:attribute:: code
      :type:  Any


.. py:exception:: PipelineConfigError

   Bases: :py:obj:`PipelineError`


   Common base class for all non-exit exceptions.


   .. py:attribute:: code
      :type:  Any


.. py:class:: ErrorCode

   Bases: :py:obj:`Enum`


   .. py:attribute:: MISSING_DATA
      :type:  Any


   .. py:attribute:: INVALID_SCHEMA
      :type:  Any


   .. py:attribute:: OUTLIER_DETECTED
      :type:  Any


   .. py:attribute:: DRIFT_DETECTED
      :type:  Any


   .. py:attribute:: PROCESSING_FAILURE
      :type:  Any


   .. py:attribute:: RESOURCE_EXHAUSTED
      :type:  Any


.. py:exception:: DataError(message, code, details = ...)

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


   .. py:method:: to_dict()


.. py:exception:: MissingDataError(message, code, details = ...)

   Bases: :py:obj:`DataError`


   Common base class for all non-exit exceptions.


.. py:exception:: InvalidSchemaError(message, code, details = ...)

   Bases: :py:obj:`DataError`


   Common base class for all non-exit exceptions.


.. py:class:: DataSource(config)

   Bases: :py:obj:`ABC`


   .. py:method:: load_data(*args, **kwargs)
      :async:



   .. py:method:: stream_data()
      :async:



.. py:class:: PipelineStep(name = ..., **_)

   Bases: :py:obj:`Generic`\ [\ :py:obj:`InT`\ , :py:obj:`OutT`\ ], :py:obj:`ABC`


   .. py:attribute:: STEP_NAME
      :type:  Any


   .. py:attribute:: STEP_VERSION
      :type:  Any


   .. py:attribute:: requires
      :type:  Set[str]
      :value: Ellipsis



   .. py:attribute:: produces
      :type:  Set[str]
      :value: Ellipsis



   .. py:attribute:: preferred_engine
      :type:  Optional[Engine]
      :value: Ellipsis



   .. py:method:: execute(data, context)
      :async:



   .. py:method:: apply_batch(lf, ctx)


   .. py:method:: apply_batch_pandas(df, ctx)


   .. py:method:: apply_stream(aiter, ctx)
      :async:



   .. py:method:: compose(*steps)


.. py:class:: CompositeStep(steps, **kwargs)

   Bases: :py:obj:`PipelineStep`


   .. py:method:: apply_batch(lf, ctx)


