pysrc.meta.phase2_broad_reset.p2_contracts
==========================================

.. py:module:: pysrc.meta.phase2_broad_reset.p2_contracts


Attributes
----------

.. autoapisummary::

   pysrc.meta.phase2_broad_reset.p2_contracts.SurfaceStatus
   pysrc.meta.phase2_broad_reset.p2_contracts.ModelStatus
   pysrc.meta.phase2_broad_reset.p2_contracts.CandidateStatus
   pysrc.meta.phase2_broad_reset.p2_contracts.RouterTarget
   pysrc.meta.phase2_broad_reset.p2_contracts.DecisionRule
   pysrc.meta.phase2_broad_reset.p2_contracts.NarrowClassification
   pysrc.meta.phase2_broad_reset.p2_contracts.SplitPolicy
   pysrc.meta.phase2_broad_reset.p2_contracts.FeaturePolicy
   pysrc.meta.phase2_broad_reset.p2_contracts.NarrowDataMode


Classes
-------

.. autoapisummary::

   pysrc.meta.phase2_broad_reset.p2_contracts.RunPhase
   pysrc.meta.phase2_broad_reset.p2_contracts.RunMetadata
   pysrc.meta.phase2_broad_reset.p2_contracts.PrimaryDataPanelEntry
   pysrc.meta.phase2_broad_reset.p2_contracts.DerivedSupervisionSurfaceEntry
   pysrc.meta.phase2_broad_reset.p2_contracts.SurfaceRegistryEntry
   pysrc.meta.phase2_broad_reset.p2_contracts.ModelFamilyEntry
   pysrc.meta.phase2_broad_reset.p2_contracts.SignalFamilyEntry
   pysrc.meta.phase2_broad_reset.p2_contracts.ArchitectureMap
   pysrc.meta.phase2_broad_reset.p2_contracts.ModelFamilyRegistry
   pysrc.meta.phase2_broad_reset.p2_contracts.SignalFamilyRegistry
   pysrc.meta.phase2_broad_reset.p2_contracts.SurfaceMarketRegistry
   pysrc.meta.phase2_broad_reset.p2_contracts.CandidateSpec
   pysrc.meta.phase2_broad_reset.p2_contracts.CandidateMatrix
   pysrc.meta.phase2_broad_reset.p2_contracts.SurfaceStressResult
   pysrc.meta.phase2_broad_reset.p2_contracts.BaselineMetrics
   pysrc.meta.phase2_broad_reset.p2_contracts.CandidateResult
   pysrc.meta.phase2_broad_reset.p2_contracts.NarrowingReport
   pysrc.meta.phase2_broad_reset.p2_contracts.SurvivorManifest
   pysrc.meta.phase2_broad_reset.p2_contracts.HumanSummary
   pysrc.meta.phase2_broad_reset.p2_contracts.P2Config


Module Contents
---------------

.. py:data:: SurfaceStatus
   :type:  Any

.. py:data:: ModelStatus
   :type:  Any

.. py:data:: CandidateStatus
   :type:  Any

.. py:data:: RouterTarget
   :type:  Any

.. py:data:: DecisionRule
   :type:  Any

.. py:data:: NarrowClassification
   :type:  Any

.. py:data:: SplitPolicy
   :type:  Any

.. py:data:: FeaturePolicy
   :type:  Any

.. py:data:: NarrowDataMode
   :type:  Any

.. py:class:: RunPhase

   Bases: :py:obj:`StrEnum`


   .. py:attribute:: MAP
      :type:  Any


   .. py:attribute:: MATRIX
      :type:  Any


   .. py:attribute:: NARROW
      :type:  Any


   .. py:attribute:: FULL
      :type:  Any


.. py:class:: RunMetadata

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: run_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: timestamp
      :type:  datetime
      :value: Ellipsis



   .. py:attribute:: phase
      :type:  RunPhase
      :value: Ellipsis



   .. py:attribute:: git_commit
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: python_version
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: random_seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: config_hash
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: notes
      :type:  str
      :value: Ellipsis



.. py:class:: PrimaryDataPanelEntry

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: surface_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: provider
      :type:  str
      :value: Ellipsis



   .. py:attribute:: dataset_name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: path
      :type:  str
      :value: Ellipsis



   .. py:attribute:: date_start
      :type:  str
      :value: Ellipsis



   .. py:attribute:: date_end
      :type:  str
      :value: Ellipsis



   .. py:attribute:: row_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: instrument_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: trading_day_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: status
      :type:  Literal['available_primary', 'blocked_dependency_missing']
      :value: Ellipsis



   .. py:attribute:: adjusted_prices_for
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: raw_prices_volume_for
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: pit_safe
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: reason
      :type:  str | None
      :value: Ellipsis



.. py:class:: DerivedSupervisionSurfaceEntry

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: surface_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: family
      :type:  str
      :value: Ellipsis



   .. py:attribute:: status
      :type:  SurfaceStatus
      :value: Ellipsis



   .. py:attribute:: supervision_path
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: bundle_id
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: bundle_surface_id
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: schema_version
      :type:  str
      :value: Ellipsis



   .. py:attribute:: derived_from_panel
      :type:  str
      :value: Ellipsis



   .. py:attribute:: role
      :type:  Literal['primary_narrow', 'stress_report_only', 'embedded_features']
      :value: Ellipsis



   .. py:attribute:: reason
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: pit_safe
      :type:  bool
      :value: Ellipsis



.. py:class:: SurfaceRegistryEntry

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: surface_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: family
      :type:  str
      :value: Ellipsis



   .. py:attribute:: status
      :type:  SurfaceStatus
      :value: Ellipsis



   .. py:attribute:: reason
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: path
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: row_count
      :type:  int | None
      :value: Ellipsis



   .. py:attribute:: feature_count
      :type:  int | None
      :value: Ellipsis



   .. py:attribute:: available_at_decision_time
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: pit_safe
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: columns_sample
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: derived_from_panel
      :type:  str | None
      :value: Ellipsis



.. py:class:: ModelFamilyEntry

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: status
      :type:  ModelStatus
      :value: Ellipsis



   .. py:attribute:: reason
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: supported_router_targets
      :type:  list[RouterTarget]
      :value: Ellipsis



   .. py:attribute:: supported_decision_rules
      :type:  list[DecisionRule]
      :value: Ellipsis



   .. py:attribute:: requires_extra
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: default_hyperparams
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:class:: SignalFamilyEntry

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: family
      :type:  str
      :value: Ellipsis



   .. py:attribute:: signals
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: status
      :type:  SurfaceStatus
      :value: Ellipsis



   .. py:attribute:: reason
      :type:  str | None
      :value: Ellipsis



.. py:class:: ArchitectureMap

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: meta
      :type:  RunMetadata
      :value: Ellipsis



   .. py:attribute:: primary_panel
      :type:  PrimaryDataPanelEntry | None
      :value: Ellipsis



   .. py:attribute:: derived_surfaces
      :type:  list[DerivedSupervisionSurfaceEntry]
      :value: Ellipsis



   .. py:attribute:: surfaces
      :type:  list[SurfaceRegistryEntry]
      :value: Ellipsis



   .. py:attribute:: summary
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:class:: ModelFamilyRegistry

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: meta
      :type:  RunMetadata
      :value: Ellipsis



   .. py:attribute:: families
      :type:  list[ModelFamilyEntry]
      :value: Ellipsis



.. py:class:: SignalFamilyRegistry

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: meta
      :type:  RunMetadata
      :value: Ellipsis



   .. py:attribute:: families
      :type:  list[SignalFamilyEntry]
      :value: Ellipsis



.. py:class:: SurfaceMarketRegistry

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: meta
      :type:  RunMetadata
      :value: Ellipsis



   .. py:attribute:: primary_panel
      :type:  PrimaryDataPanelEntry | None
      :value: Ellipsis



   .. py:attribute:: surfaces
      :type:  list[SurfaceRegistryEntry]
      :value: Ellipsis



   .. py:attribute:: blocked_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: available_count
      :type:  int
      :value: Ellipsis



   .. py:attribute:: available_primary_count
      :type:  int
      :value: Ellipsis



.. py:class:: CandidateSpec

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: candidate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: model_family
      :type:  str
      :value: Ellipsis



   .. py:attribute:: router_target
      :type:  RouterTarget
      :value: Ellipsis



   .. py:attribute:: decision_rule
      :type:  DecisionRule
      :value: Ellipsis



   .. py:attribute:: input_surface
      :type:  str
      :value: Ellipsis



   .. py:attribute:: feature_allowlist
      :type:  list[str] | FeaturePolicy
      :value: Ellipsis



   .. py:attribute:: forbidden_features
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: comparators
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: split_policy
      :type:  SplitPolicy
      :value: Ellipsis



   .. py:attribute:: status
      :type:  CandidateStatus
      :value: Ellipsis



   .. py:attribute:: reason
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: hyperparams
      :type:  dict[str, Any]
      :value: Ellipsis



   .. py:attribute:: created_by
      :type:  str
      :value: Ellipsis



   .. py:attribute:: supervision_path
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: feature_policy
      :type:  FeaturePolicy
      :value: Ellipsis



.. py:class:: CandidateMatrix

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: meta
      :type:  RunMetadata
      :value: Ellipsis



   .. py:attribute:: candidates
      :type:  list[CandidateSpec]
      :value: Ellipsis



   .. py:attribute:: summary
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:class:: SurfaceStressResult

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: evaluated
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: reason
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: utility
      :type:  float | None
      :value: Ellipsis



.. py:class:: BaselineMetrics

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: name
      :type:  str
      :value: Ellipsis



   .. py:attribute:: test_utility
      :type:  float
      :value: Ellipsis



   .. py:attribute:: test_sharpe_like
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: win_rate_vs_cash
      :type:  float | None
      :value: Ellipsis



   .. py:attribute:: notes
      :type:  str
      :value: Ellipsis



.. py:class:: CandidateResult

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: candidate_id
      :type:  str
      :value: Ellipsis



   .. py:attribute:: test_utility
      :type:  float
      :value: Ellipsis



   .. py:attribute:: best_child_test_utility
      :type:  float
      :value: Ellipsis



   .. py:attribute:: delta_vs_best_child
      :type:  float
      :value: Ellipsis



   .. py:attribute:: classification
      :type:  NarrowClassification
      :value: Ellipsis



   .. py:attribute:: robustness_passed
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: stress_surface_c
      :type:  SurfaceStressResult
      :value: Ellipsis



   .. py:attribute:: notes
      :type:  str
      :value: Ellipsis



   .. py:attribute:: metrics
      :type:  dict[str, float]
      :value: Ellipsis



.. py:class:: NarrowingReport

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: meta
      :type:  RunMetadata
      :value: Ellipsis



   .. py:attribute:: input_surface
      :type:  str
      :value: Ellipsis



   .. py:attribute:: n_candidates_evaluated
      :type:  int
      :value: Ellipsis



   .. py:attribute:: n_survivors
      :type:  int
      :value: Ellipsis



   .. py:attribute:: best_child_baseline
      :type:  BaselineMetrics
      :value: Ellipsis



   .. py:attribute:: other_baselines
      :type:  list[BaselineMetrics]
      :value: Ellipsis



   .. py:attribute:: results
      :type:  list[CandidateResult]
      :value: Ellipsis



   .. py:attribute:: summary
      :type:  dict[str, Any]
      :value: Ellipsis



.. py:class:: SurvivorManifest

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: meta
      :type:  RunMetadata
      :value: Ellipsis



   .. py:attribute:: survivors
      :type:  list[CandidateResult]
      :value: Ellipsis



   .. py:attribute:: ready_for_portfolio
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: recommendation
      :type:  str
      :value: Ellipsis



   .. py:attribute:: next_step
      :type:  Literal['P2-PORTFOLIO', 'investigate_failures', 'expand_matrix']
      :value: Ellipsis



.. py:class:: HumanSummary

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: meta
      :type:  RunMetadata
      :value: Ellipsis



   .. py:attribute:: markdown
      :type:  str
      :value: Ellipsis



   .. py:attribute:: key_findings
      :type:  list[str]
      :value: Ellipsis



   .. py:attribute:: survivor_table
      :type:  str | None
      :value: Ellipsis



.. py:class:: P2Config

   Bases: :py:obj:`BaseModel`


   .. py:attribute:: model_config
      :type:  Any


   .. py:attribute:: random_seed
      :type:  int
      :value: Ellipsis



   .. py:attribute:: smoke_test
      :type:  bool
      :value: Ellipsis



   .. py:attribute:: data_path
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: test_size
      :type:  float
      :value: Ellipsis



   .. py:attribute:: min_delta_for_override
      :type:  float
      :value: Ellipsis



   .. py:attribute:: confidence_level
      :type:  float
      :value: Ellipsis



   .. py:attribute:: output_dir
      :type:  str
      :value: Ellipsis



   .. py:attribute:: max_candidates_first_run
      :type:  int
      :value: Ellipsis



   .. py:attribute:: panel_root
      :type:  str
      :value: Ellipsis



   .. py:attribute:: panel_manifest_path
      :type:  str | None
      :value: Ellipsis



   .. py:attribute:: supervision_root
      :type:  str
      :value: Ellipsis



   .. py:attribute:: supervision_bundle
      :type:  str
      :value: Ellipsis



   .. py:attribute:: supervision_surface
      :type:  str
      :value: Ellipsis



   .. py:attribute:: narrow_data_mode
      :type:  NarrowDataMode
      :value: Ellipsis



   .. py:attribute:: narrow_workers
      :type:  int
      :value: Ellipsis



   .. py:attribute:: sklearn_n_jobs
      :type:  int
      :value: Ellipsis



   .. py:method:: default_supervision_path()


