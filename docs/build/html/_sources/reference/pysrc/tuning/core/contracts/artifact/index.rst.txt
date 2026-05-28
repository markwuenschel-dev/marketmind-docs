pysrc.tuning.core.contracts.artifact
====================================

.. py:module:: pysrc.tuning.core.contracts.artifact


Classes
-------

.. autoapisummary::

   pysrc.tuning.core.contracts.artifact.ArtifactWriterProtocol
   pysrc.tuning.core.contracts.artifact.ArtifactReaderProtocol


Module Contents
---------------

.. py:class:: ArtifactWriterProtocol

   Bases: :py:obj:`Protocol`


   .. py:method:: write(payload, metadata)


.. py:class:: ArtifactReaderProtocol

   Bases: :py:obj:`Protocol`


   .. py:method:: read(cas_hash)


   .. py:method:: exists(cas_hash)


