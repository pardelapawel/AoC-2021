#!/bin/python
import sys

def main():
    with open(sys.argv[1]) as input_file:
        horizontal = 0
        depth = 0
        aim = 0
        for line in input_file.readlines():
            command, num = line.strip().split()
            num = int(num)
            if command == "forward":
                horizontal += num
                depth += aim * num
            elif command == "up":
                aim -= num
            elif command == "down":
                aim += num
        print(horizontal * depth)

if __name__ == "__main__":
    main()

