#!/bin/python
import sys
from enum import Enum
Parameter = Enum('Parameter', 'gamma epsilon')

def main():
    with open(sys.argv[1]) as input_file:
        def accumulated2bin(num, param):
            if num < mid:
                return int(param != Parameter.gamma)
            else:
                return int(param == Parameter.gamma)

        arr = [0]*12
        gamma = ""
        epsilon = ""

        for idx, line in enumerate(input_file.readlines()):
            for jdx, c in enumerate(line.strip()):
                arr[jdx] += int(c)

        mid = idx/2
        gamma = int(''.join([str(accumulated2bin(n, Parameter.gamma)) for n in arr]), base=2)
        epsilon = int(''.join([str(accumulated2bin(n, Parameter.epsilon)) for n in arr]), base=2)
        print(gamma, epsilon, gamma*epsilon)

if __name__ == "__main__":
    main()

