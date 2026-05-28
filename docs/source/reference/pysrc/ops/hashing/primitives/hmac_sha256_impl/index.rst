pysrc.ops.hashing.primitives.hmac_sha256_impl
=============================================

.. py:module:: pysrc.ops.hashing.primitives.hmac_sha256_impl


Classes
-------

.. autoapisummary::

   pysrc.ops.hashing.primitives.hmac_sha256_impl.HmacSha256Deriver


Module Contents
---------------

.. py:class:: HmacSha256Deriver(master_key, master_key_id)

   .. py:method:: derive_run_seed(run_id)


   .. py:method:: derive_fold_seed(run_id, fold_idx)


   .. py:method:: derive_worker_seed(run_id, fold_idx, worker_id)


   .. py:method:: derive_strategy_seed(run_id, fold_idx, worker_id, strategy_id)


   .. py:method:: derive_asset_seed(run_id, fold_idx, worker_id, strategy_id, asset_id)


   .. py:method:: seed_to_rng(seed_bytes)


   .. py:method:: make_hashref(seed_bytes)


