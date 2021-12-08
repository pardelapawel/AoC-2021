#!/bin/python
import sys

len2digit = {
        2: 1,
        4: 4,
        3: 7,
        7: 8
        }

def main():
    with open(sys.argv[1]) as input_file:
        res = 0
        for line in input_file.readlines():
            in_digits, out_digits = line.strip().split('|')
            out_digits = out_digits.split()
            known = [len(d) for d in out_digits if len(d) in len2digit]
            res += len(known)
        print(res)



if __name__ == "__main__":
    main()

