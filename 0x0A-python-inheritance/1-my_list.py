#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """ sub class mylist"""
    def __init__(self):
        """initializes the object"""
        super().__init__(self)

    def print_sorted(self):
        """prints list sorted"""
        print(sorted(self))
