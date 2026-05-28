pysrc.data.datasets.builders
============================

.. py:module:: pysrc.data.datasets.builders


Attributes
----------

.. autoapisummary::

   pysrc.data.datasets.builders.TargetType


Classes
-------

.. autoapisummary::

   pysrc.data.datasets.builders.TimeSeriesDataset


Functions
---------

.. autoapisummary::

   pysrc.data.datasets.builders.build_loader
   pysrc.data.datasets.builders.build_train_val_loaders


Module Contents
---------------

.. py:data:: TargetType
   :type:  Any

.. py:class:: TimeSeriesDataset(df, *, seq_len, horizon, target_col = ..., ticker_col = ..., target_type = ..., transform = ..., target_transform = ..., dtype = ..., device = ...)

   Bases: :py:obj:`Dataset`


.. py:function:: build_loader(df, *, seq_len, horizon, batch_size = ..., shuffle = ..., num_workers = ..., pin_memory = ..., drop_last = ..., target_col = ..., ticker_col = ..., target_type = ..., distributed = ..., rank = ..., world_size = ..., transform = ..., target_transform = ..., dtype = ..., device = ..., **loader_kwargs)

.. py:function:: build_train_val_loaders(train_df, val_df, *, seq_len, horizon, batch_size = ..., num_workers = ..., **common_kwargs)

