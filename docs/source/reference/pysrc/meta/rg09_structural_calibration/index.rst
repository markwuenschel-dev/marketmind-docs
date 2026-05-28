pysrc.meta.rg09_structural_calibration
======================================

.. py:module:: pysrc.meta.rg09_structural_calibration


Attributes
----------

.. autoapisummary::

   pysrc.meta.rg09_structural_calibration.LOG
   pysrc.meta.rg09_structural_calibration.CALIBRATION_SCHEMA_VERSION
   pysrc.meta.rg09_structural_calibration.CALIBRATION_REPORT_FILENAME


Functions
---------

.. autoapisummary::

   pysrc.meta.rg09_structural_calibration.compute_structural_null_distribution
   pysrc.meta.rg09_structural_calibration.calibrate_structural_threshold
   pysrc.meta.rg09_structural_calibration.build_structural_calibration_report


Module Contents
---------------

.. py:data:: LOG
   :type:  Any

.. py:data:: CALIBRATION_SCHEMA_VERSION
   :type:  Final[str]
   :value: Ellipsis


.. py:data:: CALIBRATION_REPORT_FILENAME
   :type:  Final[str]
   :value: Ellipsis


.. py:function:: compute_structural_null_distribution(episodes, *, config, fixture_sha256, fold_id)

.. py:function:: calibrate_structural_threshold(fold_distributions, *, calibration_quantile = ...)

.. py:function:: build_structural_calibration_report(*, fixture_path, fixture_summary_path, fixture_metadata_path, config_path, output_path, calibration_quantile = ...)

