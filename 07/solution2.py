#!/bin/python
import sys
from functools import lru_cache


def most_common(lst):
    return max(set(lst), key=lst.count)

def arythmetic_progression(n):
    the_sum = ((1+n)/2)*n
    print(f'  sum for {n} steps is {the_sum}')
    return the_sum

def main():
    with open(sys.argv[1]) as input_file:
        crabs = [int(x) for x in input_file.readline().strip().split(',')]
        print(crabs, sum(crabs)/len(crabs), most_common(crabs), min(crabs), max(crabs))
        min_fuel = 99999999
        picked_pos = -1
        for i in range(max(crabs)):
            print(f'travelling towards {i}')
            fuel = [arythmetic_progression(abs(x - i)) for x in crabs]
            sum_fuel = sum(fuel)
            print(fuel)
            #print(i, ": ", sum_fuel)
            if sum_fuel < min_fuel:
                min_fuel = sum_fuel
                picked_pos = i
        print(f'the least amount of fuel will be used for position {picked_pos}: {min_fuel}')


if __name__ == "__main__":
    main()

