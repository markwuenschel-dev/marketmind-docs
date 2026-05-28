pysrc.scripts.download_rg09_market_data
=======================================

.. py:module:: pysrc.scripts.download_rg09_market_data


Attributes
----------

.. autoapisummary::

   pysrc.scripts.download_rg09_market_data.LOG
   pysrc.scripts.download_rg09_market_data.REQUIRED_ROWS


Functions
---------

.. autoapisummary::

   pysrc.scripts.download_rg09_market_data.ticker_safe_filename
   pysrc.scripts.download_rg09_market_data.sha256_file
   pysrc.scripts.download_rg09_market_data.normalize_close_frame
   pysrc.scripts.download_rg09_market_data.download_ticker_to_parquet
   pysrc.scripts.download_rg09_market_data.main


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:data:: REQUIRED_ROWS
   :type:  Final[int]
   :value: Ellipsis


.. py:function:: ticker_safe_filename(ticker)

.. py:function:: sha256_file(path)

.. py:function:: normalize_close_frame(raw, *, ticker)

.. py:function:: download_ticker_to_parquet(*, ticker, start, end, output_path)

.. py:function:: main(output_dir, start, end, tickers)

