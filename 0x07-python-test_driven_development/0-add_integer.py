#!/usr/bin/python3
"""Defines an addition function"""

def add_integer(a, b=98):
    """Return the addition of funciton inputs
    if its fload cast it to ints
    
    Raises:
        TypeError: if a or b neither float nor integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        a = int(a)
        b = int(b)
        return a + b
