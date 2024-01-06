#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    for i in my_list:
        if i == idx:
            x = my_list.index(idx)
    return x
