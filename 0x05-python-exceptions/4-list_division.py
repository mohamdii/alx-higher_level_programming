#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    index = 0
    nlist = []
    while True:
        try:
            if index < list_length:
                result = my_list_1[index] / my_list_2[index]
            else:
                return nlist
        except TypeError:
            result = 0
            print("wrong type")
        except ZeroDivisionError:
            result = 0
            print("division by 0")
        except IndexError:
            result = 0
            print("out of range")
            return nlist
        finally:
            nlist.append(result)
            index+=1
