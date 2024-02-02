#!/usr/bin/python3
"""function that compares if directly or inderectly inheriting from class"""

def inherits_from(obj, a_class):
    """
    Check if the obj is directly or indirectly inheriting from class
    Args:
        obj (any type): input to be compared
        a_class (target): class
    Returns:
        if obj is compared return True
        otherwise - False
    """
    if (isinstance(obj, a_class)):
        return True
    return False
