#!/usr/bin/python3
"""function that writes json to text file"""
import json


def save_to_json_file(my_obj, filename):
    """it modifies text file to take python object"""
    with open(filename, mode="w") as file:
        file.write(json.dumps(my_obj))
