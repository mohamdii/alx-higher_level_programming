#!/usr/bin/python3
import json
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)
    
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        self.__width  = self.validate_setter("width", value)
        self.__height = self.validate_setter("height", value)

    def update(self, *args, **kwargs):
        try:
            self.id = args[0]
            self.__size = args[1]
            self.__x = args[2]
            self.__y = args[3]
        except IndexError:
            pass
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        return self.__dict__


    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.__size)
