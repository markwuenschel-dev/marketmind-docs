pysrc.registry.signal_catalog
=============================

.. py:module:: pysrc.registry.signal_catalog


Classes
-------

.. autoapisummary::

   pysrc.registry.signal_catalog.SignalProtocol
   pysrc.registry.signal_catalog.RegisteredSignal
   pysrc.registry.signal_catalog.SignalCatalog


Functions
---------

.. autoapisummary::

   pysrc.registry.signal_catalog.create_starter_spread_zscore
   pysrc.registry.signal_catalog.create_starter_hedge_ratio
   pysrc.registry.signal_catalog.create_starter_TSMOM
   pysrc.registry.signal_catalog.create_starter_XSMOM
   pysrc.registry.signal_catalog.create_starter_RSI_baseline
   pysrc.registry.signal_catalog.get_catalog


Module Contents
---------------

.. py:class:: SignalProtocol

   Bases: :py:obj:`Protocol`


   .. py:method:: signal_embedding()


   .. py:method:: slot_index()


.. py:class:: RegisteredSignal(impl, slot_index, spec_hash, signal_name)

   .. py:method:: signal_embedding()


   .. py:method:: slot_index()


   .. py:method:: spec_hash()


   .. py:method:: signal_name()


.. py:class:: SignalCatalog

   .. py:method:: register(signal, spec_hash = ..., signal_name = ...)


   .. py:method:: get_by_spec_hash(spec_hash)


   .. py:method:: get_by_slot(slot_index)


.. py:function:: create_starter_spread_zscore()

.. py:function:: create_starter_hedge_ratio()

.. py:function:: create_starter_TSMOM()

.. py:function:: create_starter_XSMOM()

.. py:function:: create_starter_RSI_baseline()

.. py:function:: get_catalog()

