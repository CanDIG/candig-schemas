"""
Utility methods for handling protocol buffer
"""

DEFAULT_STRING = ''
DEFAULT_INT = 0


def string(val):
    """
    Default value for "string" fields
    """
    return DEFAULT_STRING if val is None else val


def int(val):
    """
    Default value for "int32" or "int64 fields
    """
    return DEFAULT_INT if val is None else val
