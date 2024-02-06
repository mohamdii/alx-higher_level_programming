#!/usr/bin/python3

import json
""" saving to json file"""


def save_to_json_file(my_obj, filename):
    """it modifies text file to take python object"""
    with open(filename, mode="w") as file:
        file.write(json.loads(my_obj))
