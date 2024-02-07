#!/usr/bin/python3
""" Student Class """


class Student:
    """student class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age =age

    def to_json(self, attrs = None):
        if isinstance(attrs, (list, str)):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        return self.__dict__

    def reload_from_json(self, json):
        return self.to_json(json)
