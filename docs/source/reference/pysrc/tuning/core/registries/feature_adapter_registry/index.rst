pysrc.tuning.core.registries.feature_adapter_registry
=====================================================

.. py:module:: pysrc.tuning.core.registries.feature_adapter_registry


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.registries.feature_adapter_registry.FeatureAdapterProtocol


Functions
---------

.. autoapisummary::

   pysrc.tuning.core.registries.feature_adapter_registry.register
   pysrc.tuning.core.registries.feature_adapter_registry.get
   pysrc.tuning.core.registries.feature_adapter_registry.list_registered


Module Contents
---------------

.. py:class:: FeatureAdapterProtocol

   Bases: :py:obj:`Protocol`


   .. py:method:: transform(data, params)


.. py:function:: register(name, version)

.. py:function:: get(name, version = ...)

.. py:function:: list_registered()

