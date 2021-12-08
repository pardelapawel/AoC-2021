#!/bin/python
import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def calculate_children(fish_timer, time_left):
    if time_left < 0:
        return 0
    if time_left == 0:
        return 1
    if fish_timer == 0:
        return calculate_children(8, time_left - 1) + calculate_children(6, time_left - 1)
    return calculate_children(fish_timer - 1, time_left - 1)

def main():
    with open(sys.argv[1]) as input_file:
        fishes = [int(x) for x in input_file.readline().strip().split(',')]
        print(fishes)
        print(sum([calculate_children(x, 80) for x in fishes]))



if __name__ == "__main__":
    main()

