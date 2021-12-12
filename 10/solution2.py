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
                ')': 1,
                ']': 2,
                '}': 3,
                '>': 4
                }
        o_brackets = set('( [ { <'.split())
        c_brackets = set(') ] } >'.split())
        points = []
        for line in input_file.readlines():
            #print(len(line))
            #print()
            line = line.strip()
            nums = [0]*len(line)
            counter = 0
            stack = []
            chunks = 0
            corrupted = False
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
                        #print(f"expected {bracket_lookup[stack[0]]} but got {b}")
                        corrupted = True
                        stack.pop(0)
            if corrupted:
                continue
            compliment = [bracket_lookup[x] for x in stack]
            print(compliment)
            score = 0
            for b in compliment:
                score *= 5
                score += point_lookup[b]

            points.append(score)
        print(sorted(points))
        print(sorted(points)[len(points)//2])






if __name__ == "__main__":
    main()

