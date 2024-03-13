#!/usr/bin/python3
def is_it_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
def alist(num, func):
    oddlist = []
    for i in num:
        if func(i):
            oddlist.append(i)
    return oddlist
List =range(1, 10)
print(alist(List, is_it_odd))
