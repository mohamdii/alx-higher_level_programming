#!/usr/bin/python3
""" function that returns object from json"""
import json


def from_json_string(my_str):
    """function takes str and returns json"""

    return json.loads(my_str)
