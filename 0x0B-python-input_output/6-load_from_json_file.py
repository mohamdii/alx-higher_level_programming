#!/usr/bin/python3
"""loads from json file"""
import json


def load_from_json_file(filename, mode="r", encoding="utf-8"):
    """function return an object"""
    with open(filename) as file:
        return json.loads(file.read())
