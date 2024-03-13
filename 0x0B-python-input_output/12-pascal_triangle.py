#!/usr/bin/python3

def pascal_triangle(n):

    if n <= 0:
        return []
    triangle = [1]
    for i in range(n):
        triangle.append([1])
        print(triangle)
