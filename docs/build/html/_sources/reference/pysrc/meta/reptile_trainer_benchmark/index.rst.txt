pysrc.meta.reptile_trainer_benchmark
====================================

.. py:module:: pysrc.meta.reptile_trainer_benchmark


Functions
---------

.. autoapisummary::

   pysrc.meta.reptile_trainer_benchmark.build_synthetic_benchmark_pool
   pysrc.meta.reptile_trainer_benchmark.run_bounded_benchmark
   pysrc.meta.reptile_trainer_benchmark.run_default_mlc5_proxy_alignment_evidence
   pysrc.meta.reptile_trainer_benchmark.run_default_mlc4_k_sweep_evidence
   pysrc.meta.reptile_trainer_benchmark.run_default_mlc6_ewc_forgetting_evidence
   pysrc.meta.reptile_trainer_benchmark.run_real_w1_baseline_evidence
   pysrc.meta.reptile_trainer_benchmark.run_default_w1_baseline_evidence
   pysrc.meta.reptile_trainer_benchmark.main


Module Contents
---------------

.. py:function:: build_synthetic_benchmark_pool()

.. py:function:: run_bounded_benchmark(*, seed = ...)

.. py:function:: run_default_mlc5_proxy_alignment_evidence(*, trainer_seed = ..., curriculum_sampler_seed = ..., heldout_partition_seed = ...)

.. py:function:: run_default_mlc4_k_sweep_evidence(*, trainer_seed = ..., curriculum_sampler_seed = ...)

.. py:function:: run_default_mlc6_ewc_forgetting_evidence(*, trainer_seed = ..., historical_partition_seed = ...)

.. py:function:: run_real_w1_baseline_evidence(*, output_dir, pool_cfg, dataset_manifest, seed, timestamp_utc, w1_cfg = ..., challenger_surface = ..., pit_heterogeneity_governance_acknowledged = ...)

.. py:function:: run_default_w1_baseline_evidence(config = ..., n_synthetic_tasks = ...)

.. py:function:: main()

