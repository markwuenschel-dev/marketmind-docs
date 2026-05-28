pysrc.preprocessor.utils.validate
=================================

.. py:module:: pysrc.preprocessor.utils.validate


Attributes
----------

.. autoapisummary::

   pysrc.preprocessor.utils.validate.logger


Classes
-------

.. autoapisummary::

   pysrc.preprocessor.utils.validate.Validator
   pysrc.preprocessor.utils.validate.SchemaValidator
   pysrc.preprocessor.utils.validate.PlanValidator
   pysrc.preprocessor.utils.validate.ValidatorFactory


Functions
---------

.. autoapisummary::

   pysrc.preprocessor.utils.validate.schema_checks
   pysrc.preprocessor.utils.validate.plan_checks


Module Contents
---------------

.. py:data:: logger
   :type:  Any

.. py:class:: Validator

   Bases: :py:obj:`ABC`


   .. py:method:: validate(obj)


.. py:class:: SchemaValidator(expected, strict = ...)

   Bases: :py:obj:`Validator`


   .. py:method:: validate(df)


.. py:class:: PlanValidator

   Bases: :py:obj:`Validator`


   .. py:method:: validate(graph)


.. py:class:: ValidatorFactory

   .. py:method:: schema(strict = ...)


   .. py:method:: plan()


.. py:function:: schema_checks(df, expected, strict = ...)

.. py:function:: plan_checks(graph)

