# __main__.py

from importlib import import_module

# Import everything from the current package's __init__.py
if __package__:
    globals().update(import_module(__package__).__dict__)
else:
    # Fallback for running directly without the -m flag
    from __init__ import *

