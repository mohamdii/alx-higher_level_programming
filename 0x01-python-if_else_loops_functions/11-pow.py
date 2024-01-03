#!/usr/bin/python3
def pow(a, b):
    c = a
    if b > 0:
        for i in range(b - 1):
            a = a * c
    else:
        for i in range(b - 1):
            a = 1 / a * 1 / c
    return a
