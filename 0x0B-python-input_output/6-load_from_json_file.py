#!/usr/bin/python3
"""loads from json file"""
import json


def load_from_json_file(filename):
    """function return an object"""
    with open(filename) as file:
        json.load(file)
