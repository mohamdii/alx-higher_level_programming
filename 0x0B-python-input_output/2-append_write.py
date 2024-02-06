#!/usr/bin/python3
""" append function """


def append_write(filename="", text=""):
    """ append_write adds to text"""

    with open(filename, mode="a", encoding="utf-8") as file:
        return file.write(text)
