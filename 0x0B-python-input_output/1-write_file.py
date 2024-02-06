#!/usr/bin/python3
""" write function """
def write_file(filename="", text=""):
    """ Write with error handler with"""
    with open(filename, mode="w", encoding = "UTF8") as file:
        file.write(text)
        return len(text)
