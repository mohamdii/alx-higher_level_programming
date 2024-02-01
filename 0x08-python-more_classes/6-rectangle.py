#!/usr/bin/python3
"""
    Rectangle Class
"""


class Rectangle:
    """Rectangle class"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("widht must be >= 0")
        else:
            self.__width = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if (self.__height == 0 or self.__width == 0):
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        rec = ""
        if self.__width == 0 or self.__height == 0:
            return rec
        for col in range(self.__height):
            for row in range(self.__width):
                rec += "#"
            if self.__height - 1 != col:
                rec += '\n'
        return rec

    def __repr__(self):
        rec = "Rectangle(" + str(self.__width)
        rec += ", " + str(self.__height) + ")"
        return rec

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
