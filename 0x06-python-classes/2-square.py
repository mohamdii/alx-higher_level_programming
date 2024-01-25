#usr/bin/python3
"""class square """


class Square:
    
    def __init__(self, size=0):
        self.size = size
    def sizevalue(self):
        if self.size < 0:
            raise ValueError("size must be >= 0")
    def sizetype(self):
        if self.size.isdigit() != True:
            raise TypeError
