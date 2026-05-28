pysrc.models.ensemble.ensemble_model
====================================

.. py:module:: pysrc.models.ensemble.ensemble_model


Classes
-------

.. autoapisummary::

   pysrc.models.ensemble.ensemble_model.EnsembleStrategy
   pysrc.models.ensemble.ensemble_model.EnsembleModel


Module Contents
---------------

.. py:class:: EnsembleStrategy

   Bases: :py:obj:`ABC`


   .. py:method:: combine(predictions)


.. py:class:: EnsembleModel

   Bases: :py:obj:`ABC`


   .. py:method:: add_member(model, weight = ...)


   .. py:method:: forward(x)


