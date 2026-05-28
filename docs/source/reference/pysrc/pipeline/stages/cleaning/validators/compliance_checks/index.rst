pysrc.pipeline.stages.cleaning.validators.compliance_checks
===========================================================

.. py:module:: pysrc.pipeline.stages.cleaning.validators.compliance_checks


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.validators.compliance_checks.pl
   pysrc.pipeline.stages.cleaning.validators.compliance_checks.logger
   pysrc.pipeline.stages.cleaning.validators.compliance_checks.COMPLIANCE_CHECKS


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.validators.compliance_checks.ComplianceCheck
   pysrc.pipeline.stages.cleaning.validators.compliance_checks.ComplianceManager
   pysrc.pipeline.stages.cleaning.validators.compliance_checks.SchemaCompliance
   pysrc.pipeline.stages.cleaning.validators.compliance_checks.GDPRCompliance
   pysrc.pipeline.stages.cleaning.validators.compliance_checks.DriftCompliance


Functions
---------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.validators.compliance_checks.register_compliance_check


Module Contents
---------------

.. py:data:: pl
   :type:  Any

.. py:data:: logger
   :type:  Any

.. py:data:: COMPLIANCE_CHECKS
   :type:  Dict[str, type[ComplianceCheck]]
   :value: Ellipsis


.. py:function:: register_compliance_check(check_type)

.. py:class:: ComplianceCheck

   Bases: :py:obj:`ABC`


   .. py:method:: apply(df, sample_size = ...)


.. py:class:: ComplianceManager(config, max_workers = ...)

   .. py:method:: add_check(check)


   .. py:method:: enforce(data, eager = ..., sample_size = ...)


.. py:class:: SchemaCompliance(config = ...)

   Bases: :py:obj:`ComplianceCheck`


   .. py:method:: apply(df, sample_size = ...)


.. py:class:: GDPRCompliance(config = ...)

   Bases: :py:obj:`ComplianceCheck`


   .. py:method:: apply(df, sample_size = ...)


.. py:class:: DriftCompliance(config = ...)

   Bases: :py:obj:`ComplianceCheck`


   .. py:method:: apply(df, sample_size = ...)


