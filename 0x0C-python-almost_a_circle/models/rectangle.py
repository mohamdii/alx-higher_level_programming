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

    @staticmethod
    def validate_setter(name, val):
        if type(val) != int:
            raise TypeError("{} must be an integer".format(name))
        if name == "x" or name == "y":
            if val < 0:
                raise ValueError("{} must be >= 0".format(name))
        elif val <= 0:
            raise ValueError("{} must be > 0".format(name))
 
    def area(self):
        '''
            Returns the area of rec
        '''
        return self.height * self.width

    def display(self):
        '''prints squares'''
        for line in range(self.__y):
            print()
        for row in range(self.__height):
            for space in range(self.__x):
                print(" ", end="")
            for col in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        '''return a string
        '''
        return "({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        '''update
        '''
        try:
            self.id = args[0]
            self.__width = args[1]
            self.__height = args[2]
            self.__x = args[3]
            self.__y = args[4]
        except IndexError:
            pass
        for key, value in kwargs.items():
            setattr(self, key, value)
