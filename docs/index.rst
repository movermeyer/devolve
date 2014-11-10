.. Devolve documentation master file, created by
   sphinx-quickstart on Mon Nov 10 13:47:37 2014.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Devolve's documentation!
===================================


The Devolve ``Registry`` is a tool for registering callables that return key/value data.  The registry can then be used to call all of the registered callables, aggregate their responses and return them.


Usage
-----


In the example below, we register three functions that gather some basic data
about numeric values.


.. code-block:: python
   
   >>> from devolve import Registry
   >>> registry = Registry()
   >>> @registry.register('even', 'div3')
   ... def foo(v):
   ...     return {'even': bool(v % 2), 'div3': bool(v % 3)}
   ...
   >>> @registry.register('positive')
   ... def foo(v):
   ...     return v >= 0
   ...
   >>> @registry.register('log10')
   ... def foo(v):
   ...     return math.log(v, 10)
   ...
   >>> registry(1)
   {'even': False, 'div3': False, 'positive': True, 'log10': 0}
   >>> registry(6)
   {'even': True, 'div3': True, 'positive': True, 'log10': 0.7781512503836435}
   >>> registry(-6)
   {'even': True, 'div3': True, 'positive': False}



Contents:

.. toctree::
   :maxdepth: 2



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

