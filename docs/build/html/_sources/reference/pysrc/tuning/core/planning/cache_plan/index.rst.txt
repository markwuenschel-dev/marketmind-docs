pysrc.tuning.core.planning.cache_plan
=====================================

.. py:module:: pysrc.tuning.core.planning.cache_plan


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.planning.cache_plan.CacheEntry
   pysrc.tuning.core.planning.cache_plan.CachePlan


Module Contents
---------------

.. py:class:: CacheEntry

   .. py:attribute:: key
      :type:  str
      :value: Ellipsis



   .. py:attribute:: scope
      :type:  Literal['spec', 'ir', 'plan', 'feature', 'artifact']
      :value: Ellipsis



   .. py:attribute:: ttl_seconds
      :type:  int | None
      :value: Ellipsis



.. py:class:: CachePlan

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: entries
      :type:  tuple[CacheEntry, Ellipsis]
      :value: Ellipsis



   .. py:attribute:: default_ttl_seconds
      :type:  int | None
      :value: Ellipsis



