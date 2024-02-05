#!/usr/bin/python3
""" Square Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """initialize with sup() with size and size"""
    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, width = size, height = size)
        self.__size = size

    def __str__(self):
        return "[Square]" + "{}/{}".format(self.__size, self.__size)
