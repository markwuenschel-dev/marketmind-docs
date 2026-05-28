pysrc.meta.allocator_benchmark.frozen_inputs
============================================

.. py:module:: pysrc.meta.allocator_benchmark.frozen_inputs


Attributes
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.frozen_inputs.FROZEN_BASELINE_REPORT_HASH
   pysrc.meta.allocator_benchmark.frozen_inputs.FROZEN_BASELINE_REPORT_HASH_HEX
   pysrc.meta.allocator_benchmark.frozen_inputs.FROZEN_SPLIT_BOUNDARIES
   pysrc.meta.allocator_benchmark.frozen_inputs.FROZEN_SIGNAL_REQUIRED_COLUMNS
   pysrc.meta.allocator_benchmark.frozen_inputs.FROZEN_SIGNAL_SORT_COLUMNS


Exceptions
----------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.frozen_inputs.FrozenInputValidationError


Classes
-------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.frozen_inputs.FrozenW2V1Inputs


Functions
---------

.. autoapisummary::

   pysrc.meta.allocator_benchmark.frozen_inputs.sha256_hex_of_file
   pysrc.meta.allocator_benchmark.frozen_inputs.sha256_of_file
   pysrc.meta.allocator_benchmark.frozen_inputs.load_and_validate_frozen_w2v1_inputs
   pysrc.meta.allocator_benchmark.frozen_inputs.load_frozen_signal_rows


Module Contents
---------------

.. py:data:: FROZEN_BASELINE_REPORT_HASH
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: FROZEN_BASELINE_REPORT_HASH_HEX
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: FROZEN_SPLIT_BOUNDARIES
   :type:  Final[dict[str, tuple[str, str]]]
   :value: Ellipsis


.. py:data:: FROZEN_SIGNAL_REQUIRED_COLUMNS
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:data:: FROZEN_SIGNAL_SORT_COLUMNS
   :type:  Final[tuple[str, Ellipsis]]
   :value: Ellipsis


.. py:exception:: FrozenInputValidationError

   Bases: :py:obj:`ValueError`


   Inappropriate argument value (of correct type).


.. py:class:: FrozenW2V1Inputs

   .. py:attribute:: freeze_manifest
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: baseline_report
      :type:  dict[str, object]
      :value: Ellipsis



   .. py:attribute:: signal_rows
      :type:  pd.DataFrame
      :value: Ellipsis



   .. py:attribute:: baseline_report_hash
      :type:  str
      :value: Ellipsis



.. py:function:: sha256_hex_of_file(path)

.. py:function:: sha256_of_file(path)

.. py:function:: load_and_validate_frozen_w2v1_inputs(freeze_manifest_path, baseline_report_path, signal_rows_path, expected_baseline_report_hash = ..., expected_hash = ..., validate_split_boundaries = ...)

.. py:function:: load_frozen_signal_rows(path, *, validate_split_boundaries = ...)

