#!/usr/bin/python3
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
l = []
count = 0
for i in sys.argv:
    if count == 0:
        count+=1
        continue
    l.append(i)
filename = "add_item.json"
"""load_json = load_from_json_file(filename)"""
save_to_json_file(l, filename)

load_from_json_file(filename)
