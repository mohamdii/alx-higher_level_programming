#!/usr/bin/python3
""" Read file function"""

def read_file(filename=""):
    """read file functon with handler"""
    with open(filename, mode = "r", encoding = "UTF8") as file:
        print(file.read())
