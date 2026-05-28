pysrc.pipeline.stages.cleaning.validators.anonymization
=======================================================

.. py:module:: pysrc.pipeline.stages.cleaning.validators.anonymization


Attributes
----------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.validators.anonymization.np
   pysrc.pipeline.stages.cleaning.validators.anonymization.pl
   pysrc.pipeline.stages.cleaning.validators.anonymization.logger
   pysrc.pipeline.stages.cleaning.validators.anonymization.ANONYMIZERS


Classes
-------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.validators.anonymization.Anonymizer
   pysrc.pipeline.stages.cleaning.validators.anonymization.AnonymizationManager
   pysrc.pipeline.stages.cleaning.validators.anonymization.MaskingAnonymizer
   pysrc.pipeline.stages.cleaning.validators.anonymization.HashingAnonymizer
   pysrc.pipeline.stages.cleaning.validators.anonymization.DPAnonymizer


Functions
---------

.. autoapisummary::

   pysrc.pipeline.stages.cleaning.validators.anonymization.register_anonymizer


Module Contents
---------------

.. py:data:: np
   :type:  Any

.. py:data:: pl
   :type:  Any

.. py:data:: logger
   :type:  Any

.. py:data:: ANONYMIZERS
   :type:  Dict[str, type[Anonymizer]]
   :value: Ellipsis


.. py:function:: register_anonymizer(anon_type)

.. py:class:: Anonymizer

   Bases: :py:obj:`ABC`


   .. py:method:: apply(df, columns)


.. py:class:: AnonymizationManager(config, max_workers = ...)

   .. py:method:: add_anonymizer(anon_type, anonymizer)


   .. py:method:: anonymize(data, columns = ..., eager = ...)


.. py:class:: MaskingAnonymizer(config = ...)

   Bases: :py:obj:`Anonymizer`


   .. py:method:: apply(df, columns)


.. py:class:: HashingAnonymizer(config = ...)

   Bases: :py:obj:`Anonymizer`


   .. py:method:: apply(df, columns)


.. py:class:: DPAnonymizer(config = ...)

   Bases: :py:obj:`Anonymizer`


   .. py:method:: apply(df, columns)


