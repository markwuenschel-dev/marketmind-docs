pysrc.strategies.momentum.validation.production_v1
==================================================

.. py:module:: pysrc.strategies.momentum.validation.production_v1


Attributes
----------

.. autoapisummary::

   pysrc.strategies.momentum.validation.production_v1.PRODUCTION_V1_PROFILE


Classes
-------

.. autoapisummary::

   pysrc.strategies.momentum.validation.production_v1.CPCVConfig
   pysrc.strategies.momentum.validation.production_v1.ProductionValidationProfile


Module Contents
---------------

.. py:class:: CPCVConfig

   .. py:attribute:: n_splits
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_test_paths
      :type:  int
      :value: Ellipsis



.. py:class:: ProductionValidationProfile

   .. py:attribute:: profile_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: dsr_p_value_max
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_trl_target_confidence
      :type:  float
      :value: Ellipsis



   .. py:attribute:: pbo_max
      :type:  float
      :value: Ellipsis



   .. py:attribute:: cpcv
      :type:  CPCVConfig
      :value: Ellipsis



   .. py:method:: to_dict()


.. py:data:: PRODUCTION_V1_PROFILE
   :type:  Any

