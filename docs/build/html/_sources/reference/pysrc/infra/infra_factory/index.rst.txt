pysrc.infra.infra_factory
=========================

.. py:module:: pysrc.infra.infra_factory


Attributes
----------

.. autoapisummary::

   pysrc.infra.infra_factory.creator


Classes
-------

.. autoapisummary::

   pysrc.infra.infra_factory.DataSourceFactory


Functions
---------

.. autoapisummary::

   pysrc.infra.infra_factory.register_source
   pysrc.infra.infra_factory.unregister_source
   pysrc.infra.infra_factory.get_creator
   pysrc.infra.infra_factory.list_sources


Module Contents
---------------

.. py:function:: register_source(name, creator)

.. py:function:: unregister_source(name)

.. py:function:: get_creator(source_type)

.. py:function:: list_sources()

.. py:class:: DataSourceFactory

   .. py:method:: create(**kwargs)


.. py:data:: creator
   :type:  Any

