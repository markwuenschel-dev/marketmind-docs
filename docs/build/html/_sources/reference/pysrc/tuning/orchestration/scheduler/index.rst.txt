pysrc.tuning.orchestration.scheduler
====================================

.. py:module:: pysrc.tuning.orchestration.scheduler


Classes
-------

.. autoapisummary::

   pysrc.tuning.orchestration.scheduler.ScheduledJob
   pysrc.tuning.orchestration.scheduler.Scheduler


Module Contents
---------------

.. py:class:: ScheduledJob

   .. py:attribute:: job_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: priority
      :type:  int
      :value: Ellipsis



   .. py:attribute:: tags
      :type:  dict[str, str]
      :value: Ellipsis



.. py:class:: Scheduler

   .. py:method:: enqueue(job)


   .. py:method:: next()


   .. py:method:: pending()


