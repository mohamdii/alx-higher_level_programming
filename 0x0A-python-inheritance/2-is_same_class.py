#!/usr/bin/python3
""" function that compares between obj and class"""


def is_same_class(obj, a_class):
    """Check if an abject is exctly an instance of a class
    Args:
        obj (any): input to check
        a_class (type): comparing to this class
    Returns:
        if obj is an instance exactly of the a_class return True
        otherwise return False
    """
    if(type(obj) == a_class):
        return True
    return False
