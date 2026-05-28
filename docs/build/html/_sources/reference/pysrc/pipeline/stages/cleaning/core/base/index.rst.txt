pysrc.pipeline.stages.cleaning.core.base
========================================

.. py:module:: pysrc.pipeline.stages.cleaning.core.base


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.core.base.pd
   pysrc.pipeline.stages.cleaning.core.base.pl


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.core.base.CleaningStep


Module Contents
---------------

.. py:data:: pd
   :type:  Any

.. py:data:: pl
   :type:  Any

.. py:class:: CleaningStep(*, spec, params, registration = ...)

   Bases: :py:obj:`ABC`


   .. py:attribute:: STEP_TYPE
      :type:  Any


   .. py:attribute:: STEP_VERSION
      :type:  Any


   .. py:method:: apply(df, *, state = ..., context = ...)


