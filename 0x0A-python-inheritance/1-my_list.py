#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """ sub class mylist"""
    def __init__(self):
        super().__init__(self)

    def print_sorted(self):
        print(sorted(self))
