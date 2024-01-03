#!/usr/bin/python3
def pow(a, b):
    c = a
    for i in range(b - 1):
        a = a * c
    return a
