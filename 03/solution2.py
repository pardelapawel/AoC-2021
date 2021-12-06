#!/bin/python
import sys
from enum import Enum
Parameter = Enum('Parameter', 'gamma epsilon')

def main():
    with open(sys.argv[1]) as input_file:

        def arr_it(arr, indexes, pos):
            for i in indexes:
                yield arr[i][pos]

        def count_life_support(arr, param):
            def accumulated2bin(num, param):
                if num < mid:
                    return int(param != Parameter.gamma)
                else:
                    return int(param == Parameter.gamma)
            pos = 0
            indexes = range(len(arr))
            while len(indexes) > 1 and pos < bin_len:
                sumn = 0
                for num in arr_it(arr, indexes, pos):
                    sumn += int(num)
                mid = len(indexes)/2
                common = accumulated2bin(sumn, param)
                indexes = [n for i, n in enumerate(indexes) if int(arr[n][pos]) == common]
                #tmp_indexes = []
                #for i, n in enumerate(indexes):
                #    if int(arr[n][pos]) == common:
                #        print(f"appenidng {arr[n][0:pos]}[{arr[n][pos]}]{arr[n][pos+1:]}")
                #        tmp_indexes.append(n)
                #indexes = tmp_indexes
                print(f'pos:{pos} sumn:{sumn} mid: {mid} common:{common} indexes:{indexes} nums:{[arr[x] for x in indexes]}')
                pos += 1
            return arr[indexes[0]]


        bin_len = len(input_file.readline().rstrip())
        input_file.seek(0) # the above peeks the first line and goes back to the beginning

        arr = [0]*bin_len
        gamma = ""
        epsilon = ""


        oxygen = [l.strip() for l in input_file.readlines()]
        carbon = oxygen.copy()

        oxygen_rating = count_life_support(oxygen, Parameter.gamma)
        carbon_rating = count_life_support(carbon, Parameter.epsilon)

        print(oxygen_rating, carbon_rating, int(oxygen_rating, base=2) * int(carbon_rating, base=2))


        #for idx, line in enumerate(input_file.readlines()):
        #    for jdx, c in enumerate(line.strip()):
        #        arr[jdx] += int(c)

        #gamma = int(''.join([str(accumulated2bin(n, Parameter.gamma)) for n in arr]), base=2)
        #epsilon = int(''.join([str(accumulated2bin(n, Parameter.epsilon)) for n in arr]), base=2)
        #print(gamma, epsilon, gamma*epsilon)

if __name__ == "__main__":
    main()

