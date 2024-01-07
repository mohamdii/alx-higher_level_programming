#!/usr/bin/python3
def max_integer(my_list=[]):
    i = len(my_list) - 1
    while i < 1:
        temp = my_list[i]
        while my_list[i] > temp:
            continue
    return temp
