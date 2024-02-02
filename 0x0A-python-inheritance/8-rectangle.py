#!/usr/bin/python3
"""Ract subclass"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """rectanlge inherits for geometry !"""
    def __init__(self, width, height):
        self.integer_validator("width", height)
        self.integer_validator("height", width)
        self.__width = width
        self.__height = height
