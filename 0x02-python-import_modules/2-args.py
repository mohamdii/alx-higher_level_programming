#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    for i in range(len(sys.argv)):
        if i == 0:
            continue
        print("{}: {}".format(i,sys.argv[i]))
