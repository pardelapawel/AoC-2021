#!/bin/python
import sys

def spaced(arr):
    print(' '.join([str(x).rjust(2) for x in arr]))

def main():
    with open(sys.argv[1]) as input_file:
        bracket_lookup = {
                '(': ')',
                '[': ']',
                '{': '}',
                '<': '>',
                ')': '(',
                ']': '[',
                '}': '{',
                '>': '<'
                }
        point_lookup = {
                ')': 3,
                ']': 57,
                '}': 1197,
                '>': 25137
                }
        o_brackets = set('( [ { <'.split())
        c_brackets = set(') ] } >'.split())
        points = 0
        for line in input_file.readlines():
            #print(len(line))
            #print()
            line = line.strip()
            nums = [0]*len(line)
            counter = 0
            stack = []
            chunks = 0
            for it, b in enumerate(line):
                if b in o_brackets:
                    stack = [b] + stack
                    counter += 1
                    #print(" "*counter*2, b)
                if b in c_brackets:
                    #print(" "*counter*2, b)
                    counter -= 1
                    if bracket_lookup[b] == stack[0]:
                        chunks += 1
                        #print(f"chunk {chunks} found of {stack[0]}{b}")
                        stack.pop(0)
                    else:
                        print(f"expected {bracket_lookup[stack[0]]} but got {b}")
                        points += point_lookup[b]
                        stack.pop(0)

        print(points)
                #nums[it] = counter
            #spaced(line)
            #spaced(nums)





if __name__ == "__main__":
    main()

