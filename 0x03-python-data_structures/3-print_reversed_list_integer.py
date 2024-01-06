#!/usr/bin/python3
def print_reversed_list_integer(mylist=[]):
    mylist.reverse()
    count = 0
    for i in mylist:
        print(mylist[count])
        count += 1
