pysrc.analytics.statistics.base
===============================

.. py:module:: pysrc.analytics.statistics.base


Attributes
----------

.. autoapisummary::

   pysrc.analytics.statistics.base.pl
   pysrc.analytics.statistics.base.mlflow


Classes
-------

.. autoapisummary::

   pysrc.analytics.statistics.base.StatisticalComputationError
   pysrc.analytics.statistics.base.StatisticalDataError
   pysrc.analytics.statistics.base.StatisticalBackendError
   pysrc.analytics.statistics.base.StatTest
   pysrc.analytics.statistics.base.StatTestFactory
   pysrc.analytics.statistics.base.GrangercausalityTest
   pysrc.analytics.statistics.base.JohansencointegrationTest
   pysrc.analytics.statistics.base.AdfTest
   pysrc.analytics.statistics.base.KpssTest
   pysrc.analytics.statistics.base.LjungboxTest


Functions
---------

.. autoapisummary::

   pysrc.analytics.statistics.base.register_test
   pysrc.analytics.statistics.base.run_tests
   pysrc.analytics.statistics.base.adf_test
   pysrc.analytics.statistics.base.kpss_test
   pysrc.analytics.statistics.base.ljung_box_test
   pysrc.analytics.statistics.base.granger_causality_test
   pysrc.analytics.statistics.base.johansen_cointegration_test


Module Contents
---------------

.. py:data:: pl
   :type:  Any
   :value: Ellipsis


.. py:data:: mlflow
   :type:  _MlflowLike | Any
   :value: Ellipsis


.. py:class:: StatisticalComputationError

   Bases: :py:obj:`StatisticalTestError`


.. py:class:: StatisticalDataError

   Bases: :py:obj:`StatisticalTestError`


.. py:class:: StatisticalBackendError

   Bases: :py:obj:`StatisticalTestError`


.. py:function:: register_test(name = ...)

.. py:class:: StatTest

   Bases: :py:obj:`ABC`


   .. py:method:: run(data, **kwargs)


.. py:class:: StatTestFactory

   .. py:method:: get_test(test_name)


   .. py:method:: run_test(test_name, data, **kwargs)


.. py:class:: GrangercausalityTest

   Bases: :py:obj:`StatTest`


   .. py:method:: run(data, *, maxlag = ..., significance_level = ..., verbose = ..., **_)


.. py:class:: JohansencointegrationTest

   Bases: :py:obj:`StatTest`


   .. py:method:: run(data, *, det_order = ..., k_ar_diff = ..., significance_level = ..., **_)


.. py:class:: AdfTest

   Bases: :py:obj:`StatTest`


   .. py:method:: run(data, *, significance_level = ..., regression = ..., autolag = ..., maxlag = ..., **_)


.. py:class:: KpssTest

   Bases: :py:obj:`StatTest`


   .. py:method:: run(data, *, significance_level = ..., nlags = ..., regression = ..., **_)


.. py:class:: LjungboxTest

   Bases: :py:obj:`StatTest`


   .. py:method:: run(data, *, lags = ..., significance_level = ..., model_df = ..., **_)


.. py:function:: run_tests(tests, data, parallel = ..., max_workers = ...)

.. py:function:: adf_test(series, **kwargs)

.. py:function:: kpss_test(series, **kwargs)

.. py:function:: ljung_box_test(series, **kwargs)

.. py:function:: granger_causality_test(x, y, **kwargs)

.. py:function:: johansen_cointegration_test(data, **kwargs)

