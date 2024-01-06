#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    count = 1
    for i in my_list:
        if idx == i:
            return count + 1
        count+=1
    return None
