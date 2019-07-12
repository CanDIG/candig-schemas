"""
Glue for running schemas code during development
Import this module before using any other module that imports candig.schemas.
Otherwise, python will look for schemas in the installed candig package.
See __path__ documentation at:
    https://docs.python.org/2/tutorial/modules.html
"""

import candig
candig.__path__.append('candig')
