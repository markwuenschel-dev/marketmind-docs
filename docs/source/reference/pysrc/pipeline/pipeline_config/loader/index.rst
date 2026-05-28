pysrc.pipeline.pipeline_config.loader
=====================================

.. py:module:: pysrc.pipeline.pipeline_config.loader


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.pipeline_config.loader.BaseModel
   pysrc.pipeline.pipeline_config.loader.Field
   pysrc.pipeline.pipeline_config.loader.ValidationError
   pysrc.pipeline.pipeline_config.loader.ConfigDict
   pysrc.pipeline.pipeline_config.loader.model_validator
   pysrc.pipeline.pipeline_config.loader.logger
   pysrc.pipeline.pipeline_config.loader.BASE
   pysrc.pipeline.pipeline_config.loader.DEFAULT_CONFIG_PATH
   pysrc.pipeline.pipeline_config.loader.DEFAULT_SCHEMA_PATH
   pysrc.pipeline.pipeline_config.loader.CONFIG_PATH
   pysrc.pipeline.pipeline_config.loader.SCHEMA_PATH
   pysrc.pipeline.pipeline_config.loader.DataSource


Classes
-------

.. autoapisummary::

   pysrc.pipeline.pipeline_config.loader.Section
   pysrc.pipeline.pipeline_config.loader.CSVSource
   pysrc.pipeline.pipeline_config.loader.InfluxSource
   pysrc.pipeline.pipeline_config.loader.RSI
   pysrc.pipeline.pipeline_config.loader.MACD
   pysrc.pipeline.pipeline_config.loader.ATR
   pysrc.pipeline.pipeline_config.loader.Bollinger
   pysrc.pipeline.pipeline_config.loader.VWAP
   pysrc.pipeline.pipeline_config.loader.TechnicalIndicators
   pysrc.pipeline.pipeline_config.loader.Clip
   pysrc.pipeline.pipeline_config.loader.Normalization
   pysrc.pipeline.pipeline_config.loader.Calendar
   pysrc.pipeline.pipeline_config.loader.Sentiment
   pysrc.pipeline.pipeline_config.loader.ESGNormalized
   pysrc.pipeline.pipeline_config.loader.CustomFeatures
   pysrc.pipeline.pipeline_config.loader.Preprocessing
   pysrc.pipeline.pipeline_config.loader.CleaningCombo
   pysrc.pipeline.pipeline_config.loader.Cleaning
   pysrc.pipeline.pipeline_config.loader.Streaming
   pysrc.pipeline.pipeline_config.loader.RetryPolicy
   pysrc.pipeline.pipeline_config.loader.ValidationThresholds
   pysrc.pipeline.pipeline_config.loader.Fallback
   pysrc.pipeline.pipeline_config.loader.Alerting
   pysrc.pipeline.pipeline_config.loader.ErrorHandling
   pysrc.pipeline.pipeline_config.loader.ModelArchitecture
   pysrc.pipeline.pipeline_config.loader.Model
   pysrc.pipeline.pipeline_config.loader.FileOutput
   pysrc.pipeline.pipeline_config.loader.InfluxDBOutput
   pysrc.pipeline.pipeline_config.loader.Outputs
   pysrc.pipeline.pipeline_config.loader.MetricAggregation
   pysrc.pipeline.pipeline_config.loader.DashboardConfig
   pysrc.pipeline.pipeline_config.loader.Logging
   pysrc.pipeline.pipeline_config.loader.Encryption
   pysrc.pipeline.pipeline_config.loader.Credentials
   pysrc.pipeline.pipeline_config.loader.DataAnonymization
   pysrc.pipeline.pipeline_config.loader.Compliance
   pysrc.pipeline.pipeline_config.loader.Security
   pysrc.pipeline.pipeline_config.loader.RiskManagement
   pysrc.pipeline.pipeline_config.loader.DateRange
   pysrc.pipeline.pipeline_config.loader.PositionSizing
   pysrc.pipeline.pipeline_config.loader.Backtesting
   pysrc.pipeline.pipeline_config.loader.DistributedProcessing
   pysrc.pipeline.pipeline_config.loader.InteractiveBrokers
   pysrc.pipeline.pipeline_config.loader.Alpaca
   pysrc.pipeline.pipeline_config.loader.RealTimeMarketData
   pysrc.pipeline.pipeline_config.loader.RateLimit
   pysrc.pipeline.pipeline_config.loader.ExternalAPISource
   pysrc.pipeline.pipeline_config.loader.Twitter
   pysrc.pipeline.pipeline_config.loader.ESG
   pysrc.pipeline.pipeline_config.loader.FRED
   pysrc.pipeline.pipeline_config.loader.Bloomberg
   pysrc.pipeline.pipeline_config.loader.Weather
   pysrc.pipeline.pipeline_config.loader.AlternativeData
   pysrc.pipeline.pipeline_config.loader.AnomalyDetection
   pysrc.pipeline.pipeline_config.loader.PipelineConfig


Functions
---------

.. autoapisummary::

   pysrc.pipeline.pipeline_config.loader.ensure_pydantic
   pysrc.pipeline.pipeline_config.loader.ensure_polars
   pysrc.pipeline.pipeline_config.loader.ensure_influxdb_client
   pysrc.pipeline.pipeline_config.loader.load_config
   pysrc.pipeline.pipeline_config.loader.get_config
   pysrc.pipeline.pipeline_config.loader.reload_config
   pysrc.pipeline.pipeline_config.loader.reset_config_cache
   pysrc.pipeline.pipeline_config.loader.get_runtime_config
   pysrc.pipeline.pipeline_config.loader.get_dataset
   pysrc.pipeline.pipeline_config.loader.validate_runtime_requirements


Module Contents
---------------

.. py:function:: ensure_pydantic()

.. py:function:: ensure_polars()

.. py:function:: ensure_influxdb_client()

.. py:data:: BaseModel
   :type:  Any

.. py:data:: Field
   :type:  Any

.. py:data:: ValidationError
   :type:  Any

.. py:data:: ConfigDict
   :type:  Any

.. py:data:: model_validator
   :type:  Any

.. py:data:: logger
   :type:  Any

.. py:data:: BASE
   :type:  Path
   :value: Ellipsis


.. py:data:: DEFAULT_CONFIG_PATH
   :type:  Path
   :value: Ellipsis


.. py:data:: DEFAULT_SCHEMA_PATH
   :type:  Path
   :value: Ellipsis


.. py:data:: CONFIG_PATH
   :type:  Optional[Path]
   :value: Ellipsis


.. py:data:: SCHEMA_PATH
   :type:  Optional[Path]
   :value: Ellipsis


.. py:class:: Section

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:method:: validate_section()


.. py:class:: CSVSource

   Bases: :py:obj:`_PolarsMixin`, :py:obj:`_CSVSourceModel`


   .. py:method:: to_polars(**read_kwargs)


.. py:class:: InfluxSource

   Bases: :py:obj:`_PolarsMixin`, :py:obj:`_InfluxSourceModel`


   .. py:method:: to_polars(**read_kwargs)


.. py:data:: DataSource
   :type:  Any

.. py:class:: RSI

   Bases: :py:obj:`Section`


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: fillna_method
      :type:  str
      :value: Ellipsis



   .. py:method:: validate_section()


.. py:class:: MACD

   Bases: :py:obj:`Section`


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: fast_period
      :type:  int
      :value: Ellipsis



   .. py:attribute:: slow_period
      :type:  int
      :value: Ellipsis



   .. py:attribute:: signal_period
      :type:  int
      :value: Ellipsis



   .. py:attribute:: fillna_method
      :type:  str
      :value: Ellipsis



   .. py:method:: validate_section()


.. py:class:: ATR

   Bases: :py:obj:`Section`


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: fillna_method
      :type:  str
      :value: Ellipsis



.. py:class:: Bollinger

   Bases: :py:obj:`Section`


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: std_dev
      :type:  float
      :value: Ellipsis



   .. py:attribute:: fillna_method
      :type:  str
      :value: Ellipsis



.. py:class:: VWAP

   Bases: :py:obj:`Section`


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: reset_period
      :type:  str
      :value: Ellipsis



   .. py:attribute:: fillna_method
      :type:  str
      :value: Ellipsis



.. py:class:: TechnicalIndicators

   Bases: :py:obj:`Section`


   .. py:attribute:: rsi
      :type:  Optional[RSI]
      :value: Ellipsis



   .. py:attribute:: macd
      :type:  Optional[MACD]
      :value: Ellipsis



   .. py:attribute:: atr
      :type:  Optional[ATR]
      :value: Ellipsis



   .. py:attribute:: vwap
      :type:  Optional[VWAP]
      :value: Ellipsis



   .. py:attribute:: bollinger_bands
      :type:  Optional[Bollinger]
      :value: Ellipsis



   .. py:attribute:: extra_indicators
      :type:  Dict[str, Dict[str, Any]]
      :value: Ellipsis



   .. py:method:: validate_section()


.. py:class:: Clip

   Bases: :py:obj:`Section`


   .. py:attribute:: min
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max
      :type:  float
      :value: Ellipsis



.. py:class:: Normalization

   Bases: :py:obj:`Section`


   .. py:attribute:: method
      :type:  str
      :value: Ellipsis



   .. py:attribute:: rolling_window
      :type:  int
      :value: Ellipsis



   .. py:attribute:: clip_extremes
      :type:  Clip
      :value: Ellipsis



   .. py:method:: validate_section()


.. py:class:: Calendar

   Bases: :py:obj:`Section`


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: day_of_week
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: holidays
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: timezones
      :type:  List[str]
      :value: Ellipsis



   .. py:method:: is_holiday(dt)


.. py:class:: Sentiment

   Bases: :py:obj:`Section`


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: source
      :type:  str
      :value: Ellipsis



   .. py:attribute:: sentiment_model
      :type:  str
      :value: Ellipsis



.. py:class:: ESGNormalized

   Bases: :py:obj:`Section`


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: method
      :type:  str
      :value: Ellipsis



.. py:class:: CustomFeatures

   Bases: :py:obj:`Section`


   .. py:attribute:: sentiment
      :type:  Optional[Sentiment]
      :value: Ellipsis



   .. py:attribute:: esg_normalized
      :type:  Optional[ESGNormalized]
      :value: Ellipsis



.. py:class:: Preprocessing

   Bases: :py:obj:`Section`


   .. py:attribute:: technical_indicators
      :type:  TechnicalIndicators
      :value: Ellipsis



   .. py:attribute:: normalization
      :type:  Normalization
      :value: Ellipsis



   .. py:attribute:: custom_features
      :type:  CustomFeatures
      :value: Ellipsis



   .. py:attribute:: calendar_features
      :type:  Calendar
      :value: Ellipsis



   .. py:attribute:: steps
      :type:  List[Dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: step_macros
      :type:  Dict[str, Dict[str, Any]]
      :value: Ellipsis



   .. py:method:: validate_section()


   .. py:method:: expand_macros()


.. py:class:: CleaningCombo

   Bases: :py:obj:`Section`


   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: when
      :type:  Optional[Dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: steps
      :type:  List[Dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: order
      :type:  Dict[str, Dict[str, List[str]]]
      :value: Ellipsis



   .. py:attribute:: determinism_tier
      :type:  str
      :value: Ellipsis



   .. py:attribute:: governance_mode
      :type:  str
      :value: Ellipsis



   .. py:attribute:: seed_lineage
      :type:  str
      :value: Ellipsis



   .. py:attribute:: pit_boundary
      :type:  str
      :value: Ellipsis



   .. py:attribute:: metadata
      :type:  Dict[str, Any]
      :value: Ellipsis



.. py:class:: Cleaning

   Bases: :py:obj:`Section`


   .. py:attribute:: combos
      :type:  List[CleaningCombo]
      :value: Ellipsis



   .. py:attribute:: use
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: determinism_tier
      :type:  str
      :value: Ellipsis



   .. py:attribute:: governance_mode
      :type:  str
      :value: Ellipsis



   .. py:attribute:: seed_lineage
      :type:  str
      :value: Ellipsis



   .. py:attribute:: pit_boundary
      :type:  str
      :value: Ellipsis



   .. py:attribute:: missing_values
      :type:  Dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: outliers
      :type:  Dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: denoising
      :type:  Dict[str, Any]
      :value: Ellipsis



.. py:class:: Streaming

   Bases: :py:obj:`Section`


   .. py:attribute:: batch_size
      :type:  int
      :value: Ellipsis



   .. py:attribute:: update_interval_seconds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: buffer_size
      :type:  int
      :value: Ellipsis



   .. py:attribute:: max_latency_ms
      :type:  int
      :value: Ellipsis



   .. py:attribute:: buffer_retention_seconds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: event_triggers
      :type:  Dict[str, str]
      :value: Ellipsis



   .. py:attribute:: priority_queue
      :type:  str
      :value: Ellipsis



   .. py:attribute:: failure_recovery
      :type:  Dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: sync_interval_seconds
      :type:  int
      :value: Ellipsis



.. py:class:: RetryPolicy

   Bases: :py:obj:`Section`


   .. py:attribute:: max_attempts
      :type:  int
      :value: Ellipsis



   .. py:attribute:: initial_backoff_seconds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: max_backoff_seconds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: retry_strategy
      :type:  str
      :value: Ellipsis



.. py:class:: ValidationThresholds

   Bases: :py:obj:`Section`


   .. py:attribute:: max_missing_ratio
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_outlier_ratio
      :type:  float
      :value: Ellipsis



.. py:class:: Fallback

   Bases: :py:obj:`Section`


   .. py:attribute:: twitter
      :type:  str
      :value: Ellipsis



   .. py:attribute:: esg
      :type:  str
      :value: Ellipsis



   .. py:attribute:: data_source
      :type:  str
      :value: Ellipsis



.. py:class:: Alerting

   Bases: :py:obj:`Section`


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: channel
      :type:  str
      :value: Ellipsis



   .. py:attribute:: critical_failures
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: alert_severity
      :type:  List[str]
      :value: Ellipsis



.. py:class:: ErrorHandling

   Bases: :py:obj:`Section`


   .. py:attribute:: retry_policy
      :type:  RetryPolicy
      :value: Ellipsis



   .. py:attribute:: validation_thresholds
      :type:  ValidationThresholds
      :value: Ellipsis



   .. py:attribute:: fallback
      :type:  Fallback
      :value: Ellipsis



   .. py:attribute:: alerting
      :type:  Alerting
      :value: Ellipsis



   .. py:attribute:: fallback_timeout_seconds
      :type:  int
      :value: Ellipsis



.. py:class:: ModelArchitecture

   Bases: :py:obj:`Section`


   .. py:attribute:: num_layers
      :type:  int
      :value: Ellipsis



   .. py:attribute:: hidden_size
      :type:  int
      :value: Ellipsis



   .. py:attribute:: dropout
      :type:  float
      :value: Ellipsis



.. py:class:: Model

   Bases: :py:obj:`Section`


   .. py:attribute:: model_type
      :type:  str
      :value: Ellipsis



   .. py:attribute:: architecture
      :type:  ModelArchitecture
      :value: Ellipsis



   .. py:attribute:: sequence_length
      :type:  int
      :value: Ellipsis



   .. py:attribute:: prediction_horizon
      :type:  int
      :value: Ellipsis



   .. py:attribute:: feature_list
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: training_device
      :type:  str
      :value: Ellipsis



   .. py:attribute:: model_checkpoint
      :type:  Dict[str, int]
      :value: Ellipsis



   .. py:attribute:: feature_importance
      :type:  Dict[str, str]
      :value: Ellipsis



   .. py:attribute:: onnx_export
      :type:  Dict[str, Any]
      :value: Ellipsis



.. py:class:: FileOutput

   Bases: :py:obj:`Section`


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: path
      :type:  str
      :value: Ellipsis



   .. py:attribute:: rotation
      :type:  str
      :value: Ellipsis



.. py:class:: InfluxDBOutput

   Bases: :py:obj:`Section`


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: host
      :type:  str
      :value: Ellipsis



   .. py:attribute:: port
      :type:  int
      :value: Ellipsis



   .. py:attribute:: token
      :type:  str
      :value: Ellipsis



   .. py:attribute:: org
      :type:  str
      :value: Ellipsis



   .. py:attribute:: bucket
      :type:  str
      :value: Ellipsis



.. py:class:: Outputs

   Bases: :py:obj:`Section`


   .. py:attribute:: console
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: file
      :type:  FileOutput
      :value: Ellipsis



   .. py:attribute:: influxdb
      :type:  InfluxDBOutput
      :value: Ellipsis



.. py:class:: MetricAggregation

   Bases: :py:obj:`Section`


   .. py:attribute:: aggregation_window_seconds
      :type:  int
      :value: Ellipsis



.. py:class:: DashboardConfig

   Bases: :py:obj:`Section`


   .. py:attribute:: grafana_url
      :type:  str
      :value: Ellipsis



.. py:class:: Logging

   Bases: :py:obj:`Section`


   .. py:attribute:: level
      :type:  str
      :value: Ellipsis



   .. py:attribute:: outputs
      :type:  Outputs
      :value: Ellipsis



   .. py:attribute:: metrics_report_interval_seconds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: custom_metrics
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: model_metrics
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: metric_aggregation
      :type:  MetricAggregation
      :value: Ellipsis



   .. py:attribute:: log_sampling_rate
      :type:  float
      :value: Ellipsis



   .. py:attribute:: dashboard_config
      :type:  DashboardConfig
      :value: Ellipsis



.. py:class:: Encryption

   Bases: :py:obj:`Section`


   .. py:attribute:: at_rest
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: in_transit
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: encryption_algorithm
      :type:  str
      :value: Ellipsis



.. py:class:: Credentials

   Bases: :py:obj:`Section`


   .. py:attribute:: twitter_api_key
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: esg_api_key
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: fred_api_key
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: bloomberg_api_key
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: weather_api_key
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: alpha_vantage_api_key
      :type:  Optional[str]
      :value: Ellipsis



   .. py:method:: validate_secrets()


.. py:class:: DataAnonymization

   Bases: :py:obj:`Section`


   .. py:attribute:: anonymize_pii
      :type:  bool
      :value: Ellipsis



.. py:class:: Compliance

   Bases: :py:obj:`Section`


   .. py:attribute:: audit_log
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: retention_days
      :type:  int
      :value: Ellipsis



   .. py:attribute:: audit_frequency_days
      :type:  int
      :value: Ellipsis



   .. py:attribute:: data_anonymization
      :type:  DataAnonymization
      :value: Ellipsis



.. py:class:: Security

   Bases: :py:obj:`Section`


   .. py:attribute:: encryption
      :type:  Encryption
      :value: Ellipsis



   .. py:attribute:: key_management
      :type:  str
      :value: Ellipsis



   .. py:attribute:: credentials
      :type:  Credentials
      :value: Ellipsis



   .. py:attribute:: compliance
      :type:  Compliance
      :value: Ellipsis



.. py:class:: RiskManagement

   Bases: :py:obj:`Section`


   .. py:attribute:: stop_loss
      :type:  float
      :value: Ellipsis



   .. py:attribute:: max_drawdown
      :type:  float
      :value: Ellipsis



.. py:class:: DateRange

   Bases: :py:obj:`Section`


   .. py:attribute:: start
      :type:  str
      :value: Ellipsis



   .. py:attribute:: end
      :type:  str
      :value: Ellipsis



.. py:class:: PositionSizing

   Bases: :py:obj:`Section`


   .. py:attribute:: method
      :type:  str
      :value: Ellipsis



.. py:class:: Backtesting

   Bases: :py:obj:`Section`


   .. py:attribute:: initial_capital
      :type:  float
      :value: Ellipsis



   .. py:attribute:: transaction_cost_rate
      :type:  float
      :value: Ellipsis



   .. py:attribute:: slippage_rate
      :type:  float
      :value: Ellipsis



   .. py:attribute:: strategy_list
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: risk_management
      :type:  RiskManagement
      :value: Ellipsis



   .. py:attribute:: date_range
      :type:  DateRange
      :value: Ellipsis



   .. py:attribute:: performance_metrics
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: position_sizing
      :type:  PositionSizing
      :value: Ellipsis



   .. py:attribute:: benchmark_index
      :type:  str
      :value: Ellipsis



   .. py:attribute:: backtest_frequency
      :type:  str
      :value: Ellipsis



.. py:class:: DistributedProcessing

   Bases: :py:obj:`Section`


   .. py:attribute:: framework
      :type:  str
      :value: Ellipsis



   .. py:attribute:: num_workers
      :type:  int
      :value: Ellipsis



   .. py:attribute:: memory_per_worker
      :type:  str
      :value: Ellipsis



   .. py:attribute:: cluster_type
      :type:  str
      :value: Ellipsis



   .. py:attribute:: min_rows_for_distributed
      :type:  int
      :value: Ellipsis



.. py:class:: InteractiveBrokers

   Bases: :py:obj:`Section`


   .. py:attribute:: host
      :type:  str
      :value: Ellipsis



   .. py:attribute:: port
      :type:  int
      :value: Ellipsis



   .. py:attribute:: client_id
      :type:  int
      :value: Ellipsis



   .. py:attribute:: subscription_topics
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: api_key
      :type:  str
      :value: Ellipsis



   .. py:attribute:: endpoint
      :type:  str
      :value: Ellipsis



   .. py:attribute:: connection_timeout_seconds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: priority
      :type:  int
      :value: Ellipsis



   .. py:attribute:: what_to_show
      :type:  str
      :value: Ellipsis



   .. py:attribute:: use_rth
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: format_date
      :type:  int
      :value: Ellipsis



.. py:class:: Alpaca

   Bases: :py:obj:`Section`


   .. py:attribute:: api_key
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: secret_key
      :type:  str
      :value: Ellipsis



   .. py:attribute:: endpoint
      :type:  str
      :value: Ellipsis



.. py:class:: RealTimeMarketData

   Bases: :py:obj:`Section`


   .. py:attribute:: interactive_brokers
      :type:  Optional[InteractiveBrokers]
      :value: Ellipsis



   .. py:attribute:: alpaca
      :type:  Optional[Alpaca]
      :value: Ellipsis



.. py:class:: RateLimit

   Bases: :py:obj:`Section`


   .. py:attribute:: per_minute
      :type:  Optional[int]
      :value: Ellipsis



   .. py:attribute:: max_calls_per_window
      :type:  Optional[int]
      :value: Ellipsis



   .. py:attribute:: window_seconds
      :type:  Optional[int]
      :value: Ellipsis



.. py:class:: ExternalAPISource

   Bases: :py:obj:`Section`


   .. py:attribute:: base_url
      :type:  str
      :value: Ellipsis



   .. py:attribute:: api_key
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: authentication_type
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: endpoints
      :type:  Dict[str, str]
      :value: Ellipsis



   .. py:attribute:: default_params
      :type:  Dict[str, str]
      :value: Ellipsis



   .. py:attribute:: rate_limit
      :type:  Optional[RateLimit]
      :value: Ellipsis



   .. py:attribute:: timeout_seconds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: cache_duration_hours
      :type:  int
      :value: Ellipsis



   .. py:attribute:: data_resolution
      :type:  Optional[str]
      :value: Ellipsis



   .. py:method:: validate_section()


.. py:class:: Twitter

   Bases: :py:obj:`Section`


   .. py:attribute:: base_url
      :type:  str
      :value: Ellipsis



   .. py:attribute:: bearer_token
      :type:  str
      :value: Ellipsis



   .. py:attribute:: authentication_type
      :type:  str
      :value: Ellipsis



   .. py:attribute:: endpoints
      :type:  Dict[str, str]
      :value: Ellipsis



   .. py:attribute:: default_params
      :type:  Dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: rate_limit
      :type:  RateLimit
      :value: Ellipsis



   .. py:attribute:: retry_after_header
      :type:  str
      :value: Ellipsis



   .. py:attribute:: timeout_seconds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: cache_duration_hours
      :type:  int
      :value: Ellipsis



   .. py:attribute:: data_resolution
      :type:  str
      :value: Ellipsis



   .. py:attribute:: api_key
      :type:  Optional[str]
      :value: Ellipsis



.. py:class:: ESG

   Bases: :py:obj:`Section`


   .. py:attribute:: base_url
      :type:  str
      :value: Ellipsis



   .. py:attribute:: api_key
      :type:  str
      :value: Ellipsis



   .. py:attribute:: authentication_type
      :type:  str
      :value: Ellipsis



   .. py:attribute:: endpoints
      :type:  Dict[str, str]
      :value: Ellipsis



   .. py:attribute:: default_params
      :type:  Dict[str, str]
      :value: Ellipsis



   .. py:attribute:: timeout_seconds
      :type:  int
      :value: Ellipsis



   .. py:attribute:: cache_duration_hours
      :type:  int
      :value: Ellipsis



   .. py:attribute:: data_resolution
      :type:  str
      :value: Ellipsis



.. py:class:: FRED

   Bases: :py:obj:`ExternalAPISource`


.. py:class:: Bloomberg

   Bases: :py:obj:`ExternalAPISource`


.. py:class:: Weather

   Bases: :py:obj:`ExternalAPISource`


.. py:class:: AlternativeData

   Bases: :py:obj:`Section`


   .. py:attribute:: twitter
      :type:  Optional[Twitter]
      :value: Ellipsis



   .. py:attribute:: alpaca
      :type:  Optional[Alpaca]
      :value: Ellipsis



   .. py:attribute:: esg
      :type:  Optional[ESG]
      :value: Ellipsis



   .. py:attribute:: fred
      :type:  Optional[FRED]
      :value: Ellipsis



   .. py:attribute:: bloomberg
      :type:  Optional[Bloomberg]
      :value: Ellipsis



   .. py:attribute:: weather
      :type:  Optional[Weather]
      :value: Ellipsis



.. py:class:: AnomalyDetection

   Bases: :py:obj:`Section`


   .. py:attribute:: enabled
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: method
      :type:  Optional[str]
      :value: Ellipsis



   .. py:attribute:: params
      :type:  Optional[Dict[str, Any]]
      :value: Ellipsis



.. py:class:: PipelineConfig

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: schema_uri
      :type:  str
      :value: Ellipsis



   .. py:attribute:: data_source
      :type:  DataSource
      :value: Ellipsis



   .. py:attribute:: preprocessing
      :type:  Preprocessing
      :value: Ellipsis



   .. py:attribute:: cleaning
      :type:  Cleaning
      :value: Ellipsis



   .. py:attribute:: streaming
      :type:  Streaming
      :value: Ellipsis



   .. py:attribute:: error_handling
      :type:  ErrorHandling
      :value: Ellipsis



   .. py:attribute:: model
      :type:  Model
      :value: Ellipsis



   .. py:attribute:: logging
      :type:  Logging
      :value: Ellipsis



   .. py:attribute:: security
      :type:  Security
      :value: Ellipsis



   .. py:attribute:: backtesting
      :type:  Backtesting
      :value: Ellipsis



   .. py:attribute:: distributed_processing
      :type:  DistributedProcessing
      :value: Ellipsis



   .. py:attribute:: alternative_data
      :type:  AlternativeData
      :value: Ellipsis



   .. py:attribute:: market_data_sources
      :type:  List[Dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: real_time_market_data
      :type:  RealTimeMarketData
      :value: Ellipsis



   .. py:attribute:: anomaly_detection
      :type:  AnomalyDetection
      :value: Ellipsis



   .. py:attribute:: includes
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: profiles
      :type:  Dict[str, Dict[str, Any]]
      :value: Ellipsis



   .. py:attribute:: active_profiles
      :type:  List[str]
      :value: Ellipsis



   .. py:attribute:: list_merge_strategy
      :type:  str
      :value: Ellipsis



   .. py:method:: merged(*overlays, list_strategy = ...)


   .. py:method:: with_profile(*profile_names)


.. py:function:: load_config(path = ..., schema_path = ..., *, apply_env = ..., env_prefix = ..., list_strategy = ...)

.. py:function:: get_config(path = ...)

.. py:function:: reload_config(path = ...)

.. py:function:: reset_config_cache()

.. py:function:: get_runtime_config()

.. py:function:: get_dataset(**kwargs)

.. py:function:: validate_runtime_requirements(conf = ...)

