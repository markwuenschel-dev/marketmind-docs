statistical.cpcv
================

.. py:module:: statistical.cpcv


Attributes
----------

.. autoapisummary::

   statistical.cpcv.LOG
   statistical.cpcv.pl


Classes
-------

.. autoapisummary::

   statistical.cpcv.CPCVError
   statistical.cpcv.CPCVDataError
   statistical.cpcv.CPCVSplit
   statistical.cpcv.CPCVConfig
   statistical.cpcv.CPCVSplitter


Functions
---------

.. autoapisummary::

   statistical.cpcv.cpcv_splits


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:data:: pl
   :type:  Any

.. py:class:: CPCVError

   Bases: :py:obj:`BaseError`


.. py:class:: CPCVDataError

   Bases: :py:obj:`CPCVError`


.. py:class:: CPCVSplit

   .. py:attribute:: split_index
      :type:  int
      :value: Ellipsis



   .. py:attribute:: train_indices
      :type:  np.ndarray
      :value: Ellipsis



   .. py:attribute:: test_indices
      :type:  np.ndarray
      :value: Ellipsis



   .. py:attribute:: test_group_ids
      :type:  List[int]
      :value: Ellipsis



   .. py:attribute:: n_train
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_test
      :type:  int
      :value: Ellipsis



.. py:class:: CPCVConfig

   .. py:attribute:: n_splits
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_test_splits
      :type:  int
      :value: Ellipsis



   .. py:attribute:: purge_periods
      :type:  int
      :value: Ellipsis



   .. py:attribute:: embargo_periods
      :type:  int
      :value: Ellipsis



   .. py:attribute:: min_train_size
      :type:  int
      :value: Ellipsis



   .. py:method:: n_combinations()


.. py:class:: CPCVSplitter(config = ...)

   .. py:method:: split(data, *, return_splits_only = ...)


   .. py:method:: n_splits_total(n_obs)


.. py:function:: cpcv_splits(data, n_splits = ..., n_test_splits = ..., purge_periods = ..., embargo_periods = ..., min_train_size = ...)

