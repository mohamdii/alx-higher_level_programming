#usr/bin/python3
"""class Square """


class Square:
    """instance and sizes square"""
    def __init__(self, size=0):
        """initialize a new square.
        Args:
            size (int): size of square.
        """     
        if isinstance(size, int) != True: 
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
            

        self.__size = size
        
