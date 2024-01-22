#!/usr/bin/python3
lists = [1 , 2, 3, 4, 5]
n = 4
index = 0
try:
    while True:
        if index < n:
            print("{}".format(lists[index]))
            index+=1
            return
except IndexError:
    print("index error")
