#!/usr/bin/python3
""" square from rec 
"""
from models.rectangle import Rectangle


def Square(Rectangle):
    """square from rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        '''initialize variables
        '''
        super().__init__(size, size, x, y, id)
