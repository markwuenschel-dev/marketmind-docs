pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader
=================================================================

.. py:module:: pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.MASSIVE_ENDPOINT
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.MASSIVE_BUCKET
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.DATASET_PREFIX
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.SOURCE_ID
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.MANIFEST_SCHEMA_VERSION
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.EXECUTION_PLAN_VERSION
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.DETERMINISM_TIER
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.S3_MISSING_OBJECT_CODES
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.DEFAULT_WORKERS
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.DEFAULT_OUTPUT_ROOT
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.LOADER_VERSION
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.logger


Exceptions
----------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.LoaderError
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.CredentialsMissingError
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.DownloadError
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.ParquetConversionError
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.MissingDependencyError


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.FileResult
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.LoaderConfig
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.StreamingBody
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.S3ObjectResponse
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.S3Client
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.Boto3Session
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.Boto3SessionFactory
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.Boto3Module
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.BotocoreConfigFactory
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.BotocoreConfigModule
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.ArrowTable
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.PyArrowModule
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.PyArrowCsvModule
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.PyArrowParquetModule


Functions
---------

.. autoapisummary::

   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.trading_dates
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.s3_key_for
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.parquet_path_for
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.partition_identity_for
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.csv_gz_bytes_to_parquet_table
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.blake2b_hex
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.atomic_write_json
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.dependency_versions
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.build_s3_client
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.ensure_runtime_dependencies
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.download_and_convert_one
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.run
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.write_manifest
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.configure_logging
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.parse_args
   pysrc.pipeline.stages.market_data.sources.massive_day_aggs_loader.main


Module Contents
---------------

.. py:data:: MASSIVE_ENDPOINT
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: MASSIVE_BUCKET
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: DATASET_PREFIX
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: SOURCE_ID
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: MANIFEST_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: EXECUTION_PLAN_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: DETERMINISM_TIER
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: S3_MISSING_OBJECT_CODES
   :type:  Final[frozenset[str]]
   :value: Ellipsis


.. py:data:: DEFAULT_WORKERS
   :type:  Final[int]
   :value: Ellipsis


.. py:data:: DEFAULT_OUTPUT_ROOT
   :type:  Final[Path]
   :value: Ellipsis


.. py:data:: LOADER_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: logger
   :type:  Any

.. py:exception:: LoaderError

   Bases: :py:obj:`Exception`


   Common base class for all non-exit exceptions.


.. py:exception:: CredentialsMissingError

   Bases: :py:obj:`LoaderError`


   Common base class for all non-exit exceptions.


.. py:exception:: DownloadError

   Bases: :py:obj:`LoaderError`


   Common base class for all non-exit exceptions.


.. py:exception:: ParquetConversionError

   Bases: :py:obj:`LoaderError`


   Common base class for all non-exit exceptions.


.. py:exception:: MissingDependencyError

   Bases: :py:obj:`LoaderError`


   Common base class for all non-exit exceptions.


.. py:class:: FileResult

   .. py:attribute:: trade_date
      :type:  str
      :value: Ellipsis



   .. py:attribute:: s3_key
      :type:  str
      :value: Ellipsis



   .. py:attribute:: parquet_path
      :type:  str
      :value: Ellipsis



   .. py:attribute:: status
      :type:  str
      :value: Ellipsis



   .. py:attribute:: rows
      :type:  int
      :value: Ellipsis



   .. py:attribute:: bytes_compressed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: bytes_parquet
      :type:  int
      :value: Ellipsis



   .. py:attribute:: s3_etag
      :type:  str
      :value: Ellipsis



   .. py:attribute:: content_blake2b
      :type:  str
      :value: Ellipsis



   .. py:attribute:: error
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: duration_seconds
      :type:  float
      :value: Ellipsis



   .. py:attribute:: partition_identity
      :type:  str
      :value: Ellipsis



   .. py:attribute:: knowledge_time_utc
      :type:  str | None
      :value: Ellipsis



.. py:class:: LoaderConfig

   .. py:attribute:: start_date
      :type:  date
      :value: Ellipsis



   .. py:attribute:: end_date
      :type:  date
      :value: Ellipsis



   .. py:attribute:: output_root
      :type:  Path
      :value: Ellipsis



   .. py:attribute:: workers
      :type:  int
      :value: Ellipsis



   .. py:attribute:: overwrite
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: verbose
      :type:  bool
      :value: Ellipsis



.. py:class:: StreamingBody

   Bases: :py:obj:`Protocol`


   .. py:method:: read()


.. py:class:: S3ObjectResponse

   Bases: :py:obj:`TypedDict`


   .. py:attribute:: Body
      :type:  StreamingBody
      :value: Ellipsis



   .. py:attribute:: ETag
      :type:  str
      :value: Ellipsis



.. py:class:: S3Client

   Bases: :py:obj:`Protocol`


   .. py:method:: get_object(*, Bucket, Key)


.. py:class:: Boto3Session

   Bases: :py:obj:`Protocol`


   .. py:method:: client(service_name, *, endpoint_url, config)


.. py:class:: Boto3SessionFactory

   Bases: :py:obj:`Protocol`


.. py:class:: Boto3Module

   Bases: :py:obj:`Protocol`


   .. py:attribute:: Session
      :type:  Boto3SessionFactory
      :value: Ellipsis



.. py:class:: BotocoreConfigFactory

   Bases: :py:obj:`Protocol`


.. py:class:: BotocoreConfigModule

   Bases: :py:obj:`Protocol`


   .. py:attribute:: Config
      :type:  BotocoreConfigFactory
      :value: Ellipsis



.. py:class:: ArrowTable

   Bases: :py:obj:`Protocol`


   .. py:method:: num_rows()


   .. py:method:: column_names()


   .. py:method:: column(name)


   .. py:method:: append_column(name, column)


.. py:class:: PyArrowModule

   Bases: :py:obj:`Protocol`


   .. py:attribute:: ArrowInvalid
      :type:  type[Exception]
      :value: Ellipsis



   .. py:attribute:: ArrowIOError
      :type:  type[Exception]
      :value: Ellipsis



   .. py:method:: array(values, *, type)


   .. py:method:: date32()


   .. py:method:: timestamp(unit, *, tz)


.. py:class:: PyArrowCsvModule

   Bases: :py:obj:`Protocol`


   .. py:method:: read_csv(source)


.. py:class:: PyArrowParquetModule

   Bases: :py:obj:`Protocol`


   .. py:method:: write_table(table, where, *, compression)


.. py:function:: trading_dates(start, end)

.. py:function:: s3_key_for(d)

.. py:function:: parquet_path_for(output_root, d)

.. py:function:: partition_identity_for(d)

.. py:function:: csv_gz_bytes_to_parquet_table(raw_gz, *, trade_date, knowledge_time)

.. py:function:: blake2b_hex(data)

.. py:function:: atomic_write_json(path, payload)

.. py:function:: dependency_versions()

.. py:function:: build_s3_client()

.. py:function:: ensure_runtime_dependencies()

.. py:function:: download_and_convert_one(s3, d, output_root, overwrite)

.. py:function:: run(config)

.. py:function:: write_manifest(config, results)

.. py:function:: configure_logging(verbose)

.. py:function:: parse_args(argv)

.. py:function:: main(argv)

