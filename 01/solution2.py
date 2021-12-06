#!/bin/python
import sys

def interate_file(filename):
    with open(filename) as f:
        arr = f.readlines()
        for idx, l in enumerate(arr[:-2]):
            res = [l, arr[idx+1], arr[idx+2]]
            yield [int(x.strip()) for x in res]

def main():
    prev = 0
    for window in interate_file(sys.argv[1]):
        curr = sum(window)
        if(prev < curr):
            print("increased")
        else:
            print("decreased")
        prev = curr
    #with open(sys.argv[1]) as input_file:
    #    prev = 0
    #    for line in input_file.readlines():
    #        line = int(line.strip())
    #        if(prev < line):
    #            print("increased")
    #        else:
    #            print("decreased")
    #        prev = line

if __name__ == "__main__":
    main()

