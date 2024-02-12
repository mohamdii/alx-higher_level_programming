#!/usr/bin/python3
import json
import csv
""" Base class """


class Base:
    """has nb objects read as follows"""
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries == None:
            return "[]"
        return  json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):

        filename = cls.__name__ + ".json"
        new_dict = []
        for i in list_objs:
            i = i.to_dictionary()
            json_dict = json.loads(cls.to_json_string(i))
            new_dict.append(json_dict)

        with open(filename, mode="w") as file:
            json.dump(new_dict, file)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        if cls.__name__ == "Rectangle":
            rec = Rectangle(5, 8)
        elif cls.__name__ == "Square":
            rec = Square(5)

        rec.update(**dictionary)
        return rec

