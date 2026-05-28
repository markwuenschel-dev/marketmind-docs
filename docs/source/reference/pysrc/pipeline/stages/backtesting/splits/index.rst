pysrc.pipeline.stages.backtesting.splits
========================================

.. py:module:: pysrc.pipeline.stages.backtesting.splits


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.stages.backtesting.splits.pl


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.backtesting.splits.BacktestingSplitNormalizerStep


Module Contents
---------------

.. py:data:: pl
   :type:  Any

.. py:class:: BacktestingSplitNormalizerStep(cfg)

   Bases: :py:obj:`PipelineStep`


   .. py:attribute:: is_fast
      :type:  Any


   .. py:method:: apply_batch(lf, ctx)


   .. py:method:: apply_batch_pandas(df, ctx)


