# FLEX

[![Build Status](https://travis-ci.org/simpleenergy/devolve.png)](https://travis-ci.org/simpleenergy/devolve)
[![Documentation Status](https://readthedocs.org/projects/devolve-swagger/badge/?version=latest)](https://readthedocs.org/projects/devolve-swagger/?badge=latest)
[![PyPi version](https://img.shields.io/pypi/v/devolve.svg)](https://pypi.python.org/pypi/devolve)
[![PyPi downloads](https://img.shields.io/pypi/dm/devolve.svg)](https://pypi.python.org/pypi/devolve)
   

[Documentation on ReadTheDocs](http://devolve.readthedocs.org/en/latest/)


Devolve is a callback registry.  Callable objects can be registered against a
set of keys.  The registry can then be used to delegate a single call across
all of the registered callables and to gather all of the returned key/value
pairs into a single mapping.


## Features

* Prevents duplicate registration of the same key.
* Validation that a callable did not return any extra keys.
* Validation that a callable returned all of the keys it was registered for.
