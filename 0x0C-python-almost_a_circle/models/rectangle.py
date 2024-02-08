#!/usr/bin/python3
from models.base import Base
class Rectangle(Base):
    
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
        validated = self.validate_setter("width", value)
        self.__width = validated

    @height.setter
    def height(self, value):
        validated = self.validate_setter("height", value)
        self.__height = validated

    @x.setter
    def x(self, value):
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    
    @y.setter
    def y(self, value):
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
    @staticmethod
    def validate_setter(name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        elif value < 0:
            raise ValueError("{} must be > 0".format(name))
        return value
