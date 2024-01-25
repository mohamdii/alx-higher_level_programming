#!/usr/bin/python3
def best_score(a_dictionary):
    largestNumber = 0
    if not a_dictionary:
        return None
    for i, value in a_dictionary.items():
        if largestNumber < value:
            largestNumber = value
    for key, value in a_dictionary.items():
        if value == largestNumber:
            return key
