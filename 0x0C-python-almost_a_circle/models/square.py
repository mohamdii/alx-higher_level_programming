#!/usr/bin/python3
"""Defines a square class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This is a square
"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialiize a Square
        """
        self.__size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        '''getter for size
        '''
        return self.__size

    @size.setter
    def size(self, value):
        '''setter for size
        '''
        self.validate_setter("width", value)
        self.__width = value
        self.validate_setter("height", value)
        self.__height = value
        self.__size = value

    def update(self, *args, **kwargs):
        '''update function
        '''
        try:
            self.id = args[0]
            self.__size = args[1]
            self.__x = args[2]
            self.__y = args[3]
        except IndexError:
            pass
        for key, value in kwargs.items():
            if hasattr(self, key) is True:
                setattr(self, key, value)

    def __str__(self):
        '''str
        '''
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.__size)
