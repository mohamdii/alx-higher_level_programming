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
