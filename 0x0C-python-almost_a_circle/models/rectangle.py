#!/usr/bin/python3
""" Rectangle from base"""

from models.base import Base


class Rectangle(Base):
    '''
        rectangle methods and const.
        Inherist from:
            Base
    '''


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

    def area(self):
        return self.__height * self.__width

    def display(self):
        for i in range(self.__y):
            print()
        for rows in range(self.__height):
            for i in range(self.__x):
                print(end=" ")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
            exit
        except IndexError:
            pass
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        return self.__dict__
