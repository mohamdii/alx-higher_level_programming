#!/usr/bin/python3
"""is_kind_of_class that checks the kind"""


def is_kind_of_class(obj, a_class):
    """
    Compares between obj and class
    Args:
        obj (any type): input to check
        a_class (targeted type): class
    Returns:
        if obj matches return True
        otherwise return false
    """
    if isinstance(obj, a_class):
        return True
    return False
