#!/usr/bin/python3
""" Student class again"""


class Student:
    """student class with get attr"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, (list, str)):
            return {attr: getattr(self, attr, None) for attr in attrs if hasattr(self, attr)}
        return self.__dict__
    
