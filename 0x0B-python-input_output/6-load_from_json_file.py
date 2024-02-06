#!/usr/bin/python3
"""loads from json file"""


def load_from_json_file(filename):
    """function return an object"""
    with open(filename, mode="r", encoding="utf-8") as file:
        return json.loads(file.read())
