#!/usr/bin/python3
"""Defines a square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialiize a Square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''getter for size
        '''
        return self.width

    @size.setter
    def size(self, value):
        '''setter for size
        '''
        self.validate_setter("width", value)
        self.width = value
        self.validate_setter("height", value)
        self.height = value

    def __str__(self):
        '''str
        '''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
