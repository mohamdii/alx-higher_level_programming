#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    count = 0
    for i in my_list:
        if idx == count:
            return i
        count += 1
    return None
