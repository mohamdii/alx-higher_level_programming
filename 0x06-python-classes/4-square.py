#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, l):
        if not isinstance(l, int):
            raise TypeError("size must be an integer")
        elif l < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = l
    def area(self):
        return self.size ** 2
