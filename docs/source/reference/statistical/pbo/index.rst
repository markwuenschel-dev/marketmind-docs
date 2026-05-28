statistical.pbo
===============

.. py:module:: statistical.pbo


Exceptions
----------

.. autoapisummary::

   statistical.pbo.PBOError
   statistical.pbo.PBODataError
   statistical.pbo.PBOComputationError


Classes
-------

.. autoapisummary::

   statistical.pbo.PBOConfig


Functions
---------

.. autoapisummary::

   statistical.pbo.compute_pbo_from_matrices
   statistical.pbo.compute_pbo_from_records
   statistical.pbo.compute_pbo_from_path_pairs
   statistical.pbo.compute_pbo


Module Contents
---------------

.. py:exception:: PBOError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: PBODataError

   Bases: :py:obj:`PBOError`


   Common base class for all non-exit exceptions.


.. py:exception:: PBOComputationError

   Bases: :py:obj:`PBOError`


   Common base class for all non-exit exceptions.


.. py:class:: PBOConfig

   .. py:attribute:: warn_threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: fail_threshold
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_trials
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_paths
      :type:  int
      :value: Ellipsis



   .. py:attribute:: include_diagnostics
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: score_basis
      :type:  str
      :value: Ellipsis



   .. py:method:: validate()


.. py:function:: compute_pbo_from_matrices(in_sample_scores, out_of_sample_scores, *, config = ..., score_higher_is_better = ...)

.. py:function:: compute_pbo_from_records(records, *, config = ..., score_higher_is_better = ...)

.. py:function:: compute_pbo_from_path_pairs(path_pairs, *, config = ..., score_higher_is_better = ...)

.. py:function:: compute_pbo(data, *, mode = ..., config = ..., score_higher_is_better = ..., out_of_sample_scores = ...)

