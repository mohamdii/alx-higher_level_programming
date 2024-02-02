#!/usr/bin/python3
"""Ract subclass"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator(self, width)
        self.integer_validator(self, height)
        self.__width = width
        self.__height = height
