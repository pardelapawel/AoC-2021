#!/bin/python
import sys
from functools import lru_cache


def most_common(lst):
    return max(set(lst), key=lst.count)

@lru_cache(maxsize=None)
def count_fuel(pos_from, pos_to):
    return abs(pos_from - pos_to)

def main():
    with open(sys.argv[1]) as input_file:
        crabs = [int(x) for x in input_file.readline().strip().split(',')]
        print(crabs, sum(crabs)/len(crabs), most_common(crabs), min(crabs), max(crabs))
        min_fuel = 99999999
        picked_pos = -1
        for i in range(max(crabs)):
            fuel = [count_fuel(x, i) for x in crabs]
            sum_fuel = sum(fuel)
            if sum_fuel < min_fuel:
                min_fuel = sum_fuel
                picked_pos = i
                print(i, ": ", sum(fuel))
        print(f'the least amount of fuel will be used for position {picked_pos}: {min_fuel}')


if __name__ == "__main__":
    main()

