#!/usr/bin/python3
def uniq_add(my_list=[]):
    for i in set(my_list):
        i+=i
    return i
