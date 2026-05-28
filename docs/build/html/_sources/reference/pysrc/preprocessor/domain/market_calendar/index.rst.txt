pysrc.preprocessor.domain.market_calendar
=========================================

.. py:module:: pysrc.preprocessor.domain.market_calendar


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.domain.market_calendar.logger


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.domain.market_calendar.MarketCalendar
   pysrc.preprocessor.domain.market_calendar.FallbackCalendar
   pysrc.preprocessor.domain.market_calendar.MarketCalendarFactory


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.domain.market_calendar.profile_calendar
   pysrc.preprocessor.domain.market_calendar.is_session
   pysrc.preprocessor.domain.market_calendar.next_session
   pysrc.preprocessor.domain.market_calendar.time_bucket
   pysrc.preprocessor.domain.market_calendar.resample_ohlcv


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:class:: MarketCalendar

   Bases: :py:obj:`ABC`


   .. py:method:: is_open_at(ts)


   .. py:method:: next_open(ts)


   .. py:method:: next_close(ts)


.. py:class:: FallbackCalendar

   Bases: :py:obj:`MarketCalendar`


   .. py:method:: is_open_at(ts)


   .. py:method:: next_open(ts)


   .. py:method:: next_close(ts)


.. py:function:: profile_calendar(func)

.. py:class:: MarketCalendarFactory

   .. py:method:: get_calendar(governed = ...)


.. py:function:: is_session(ts = ..., cal = ...)

.. py:function:: next_session(ts = ..., cal = ...)

.. py:function:: time_bucket(ts, seconds)

.. py:function:: resample_ohlcv(df, ts_col, seconds, engine = ...)

