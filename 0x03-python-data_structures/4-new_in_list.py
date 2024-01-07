#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    count = 0
    for i in my_list:
        if idx == count:
            my_list[count] = element
        count += 1
    return my_list


