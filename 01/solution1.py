#!/bin/python
import sys

def main():
    with open(sys.argv[1]) as input_file:
        prev = 0
        for line in input_file.readlines():
            line = int(line.strip())
            if(prev < line):
                print("increased")
            else:
                print("decreased")
            prev = line

if __name__ == "__main__":
    main()

