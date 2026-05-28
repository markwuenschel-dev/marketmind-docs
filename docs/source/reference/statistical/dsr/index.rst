statistical.dsr
===============

.. py:module:: statistical.dsr


Attributes
----------

.. autoapisummary::

   statistical.dsr.LOG
   statistical.dsr.pl


Classes
-------

.. autoapisummary::

   statistical.dsr.DSRError
   statistical.dsr.DSRDataError
   statistical.dsr.DSRComputationError


Functions
---------

.. autoapisummary::

   statistical.dsr.compute_dsr
   statistical.dsr.compute_min_trl
   statistical.dsr.compute_bootstrap_ci


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:data:: pl
   :type:  Any

.. py:class:: DSRError

   Bases: :py:obj:`BaseError`


.. py:class:: DSRDataError

   Bases: :py:obj:`DSRError`


.. py:class:: DSRComputationError

   Bases: :py:obj:`DSRError`


.. py:function:: compute_dsr(returns, n_trials = ..., periods_per_year = ..., benchmark_sr = ...)

.. py:function:: compute_min_trl(returns, target_confidence = ..., benchmark_sr = ..., periods_per_year = ...)

.. py:function:: compute_bootstrap_ci(returns, n_resamples = ..., block_size = ..., periods_per_year = ..., ci_levels = ..., random_state = ...)

