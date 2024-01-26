#!/usr/bin/python3
"""Square class"""


class Square:
    """ initialize """
    def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
    """ function that returns area """
    def area(self):
        return self.__size ** 2
