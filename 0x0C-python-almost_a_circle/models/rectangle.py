#!/usr/bin/python3
'''
    Class Rectangle
'''
from models.base import Base


class Rectangle(Base):
    """rectangle methods inherits from base """""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        self.validate_setter("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.validate_setter("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.validate_setter("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.validate_setter("y", value)
        self.__y = value

    def area(self):
        return (self.__width * self.__height)
    @staticmethod
    def validate_setter(name, val):
        if type(val) != int:
            raise TypeError("{} must be an integer".format(name))
        if name == "x" or name == "y":
            if val < 0:
                raise ValueError("{} must be >= 0".format(name))
        elif val <= 0:
            raise ValueError("{} must be > 0".format(name))
