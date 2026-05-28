pysrc.meta.reptile_k_sweep_runner
=================================

.. py:module:: pysrc.meta.reptile_k_sweep_runner


Attributes
----------

.. autoapisummary::

   pysrc.meta.reptile_k_sweep_runner.LOG


Functions
---------

.. autoapisummary::

   pysrc.meta.reptile_k_sweep_runner.saturation_from_adjacent_means
   pysrc.meta.reptile_k_sweep_runner.run_k_sweep
   pysrc.meta.reptile_k_sweep_runner.emit_reptile_k_sweep_report_json
   pysrc.meta.reptile_k_sweep_runner.load_k_sweep_report_json
   pysrc.meta.reptile_k_sweep_runner.recompute_content_hash_from_document


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:function:: saturation_from_adjacent_means(prev_mean, mean_delta, *, epsilon)

.. py:function:: run_k_sweep(config)

.. py:function:: emit_reptile_k_sweep_report_json(path, report)

.. py:function:: load_k_sweep_report_json(path)

.. py:function:: recompute_content_hash_from_document(doc)

