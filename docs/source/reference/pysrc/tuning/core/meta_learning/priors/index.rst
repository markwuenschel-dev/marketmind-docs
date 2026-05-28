pysrc.tuning.core.meta_learning.priors
======================================

.. py:module:: pysrc.tuning.core.meta_learning.priors


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.meta_learning.priors.HParamPrior
   pysrc.tuning.core.meta_learning.priors.SearchPrior


Functions
---------

.. autoapisummary::

   pysrc.tuning.core.meta_learning.priors.uniform_prior


Module Contents
---------------

.. py:class:: HParamPrior

   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: mean
      :type:  float
      :value: Ellipsis



   .. py:attribute:: std
      :type:  float
      :value: Ellipsis



   .. py:attribute:: weight
      :type:  float
      :value: Ellipsis



.. py:class:: SearchPrior

   .. py:attribute:: space_hash
      :type:  str
      :value: Ellipsis



   .. py:attribute:: priors
      :type:  tuple[HParamPrior, Ellipsis]
      :value: Ellipsis



.. py:function:: uniform_prior(name, low, high)

