#!/usr/bin/python3
"""main function that adds args into alist """
import sys


if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    lis = []
    filename = "add_item.json"
    save_to_json_file(lis, filename)
    for i in sys.argv[1:]:
        lis.append(i)
    load_from_json_file(filename)
