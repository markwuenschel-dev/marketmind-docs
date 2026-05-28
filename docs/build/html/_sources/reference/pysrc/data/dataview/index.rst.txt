pysrc.data.dataview
===================

.. py:module:: pysrc.data.dataview


Classes
-------

.. autoapisummary::

   pysrc.data.dataview.DataView


Module Contents
---------------

.. py:class:: DataView(universe = ..., pit_config = ..., *, pit_required = ...)

   .. py:method:: register_source(df, *, valid_time_col = ..., knowledge_time_col = ..., seed_fixture_membership = ...)


   .. py:method:: as_of(symbols, fields, knowledge_date)


   .. py:method:: universe_as_of(knowledge_date, filters = ...)


