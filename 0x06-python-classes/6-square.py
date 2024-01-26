#!/usr/bin/python3
""" class square"""


class Square:
    """initialize """
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size
    
    @property
    def position(self):
        return self.__postion
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if(not isinstance(value, tuple) or
        not all(isinstance(num, int) for num in value)
        or not all(num >= 0 for num in value)
        or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        if self.__position[1] > 0:
            for breaks in range(self.__position[1]):
                print()
        for row in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for column in range(self.__size):
                print("#", end="")
            print()
        









