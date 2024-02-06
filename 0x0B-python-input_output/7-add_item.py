#!/usr/bin/python3
"""main function that adds args into alist """
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
    lis = []
    count = 0
    for i in sys.argv:
        if count == 0:
            count+=1
            continue
        lis.append(i)
    filename = "add_item.json"
    save_to_json_file(lis, filename)
    load_from_json_file(filename)
