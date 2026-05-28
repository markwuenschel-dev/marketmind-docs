pysrc.tuning.result
===================

.. py:module:: pysrc.tuning.result


Exceptions
----------

.. autoapisummary::

   pysrc.tuning.result.TuningError
   pysrc.tuning.result.EngineNotAvailableError


Functions
---------

.. autoapisummary::

   pysrc.tuning.result.best_trial
   pysrc.tuning.result.merge_metadata


Module Contents
---------------

.. py:exception:: TuningError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: EngineNotAvailableError(engine, package)

   Bases: :py:obj:`TuningError`


   Common base class for all non-exit exceptions.


.. py:function:: best_trial(result)

.. py:function:: merge_metadata(base, extra)

