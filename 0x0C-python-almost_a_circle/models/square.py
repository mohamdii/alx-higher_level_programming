#!/usr/bin/python3
from models.rectangle import Rectangle
""" square from rec"""
def Square(Rectangle):
    """square from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        '''initialize variables
        '''
        self.size = width
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """string for rec
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

