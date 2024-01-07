#!/usr/bin/python3
def print_reversed_list_integer(mylist=[]):
    if mylist is None:
        return None
    mylist.reverse()
    for i in mylist:
        print("{:d}".format(i))
