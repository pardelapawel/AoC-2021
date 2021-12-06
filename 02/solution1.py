#!/bin/python
import sys

def main():
    with open(sys.argv[1]) as input_file:
        horizontal = 0
        depth = 0
        for line in input_file.readlines():
            command, num = line.strip().split()
            num = int(num)
            if command == "forward":
                horizontal += num
            elif command == "up":
                depth -= num
            elif command == "down":
                depth += num
        print(horizontal * depth)

if __name__ == "__main__":
    main()

