# -*- coding: utf-8 -*-

__version__ = '0.1.0'

try:
    __PANDAS_SHOULD_SETUP__
except NameError:
    __PANDAS_SHOULD_SETUP__ = False

if not __PANDAS_SHOULD_SETUP__:
    from . import dataframe
    from . import series
