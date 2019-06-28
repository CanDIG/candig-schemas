"""
Glue for running schemas code during development
Import this module before using any other module that imports ga4gh.schemas.
Otherwise, python will look for schemas in the installed ga4gh package.
See __path__ documentation at:
    https://docs.python.org/2/tutorial/modules.html
"""

import ga4gh
ga4gh.__path__.append('ga4gh')
