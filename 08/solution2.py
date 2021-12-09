#!/bin/python
import sys
from collections import Counter
from types import SimpleNamespace

len2digit = {
        2: 1,
        #5:2,
        #5:3,
        4: 4,
        #5:5,
        #6:6,
        3: 7,
        7: 8
        #6:9,
        }





def print_digit(key):
    print(f' {key.t*4} ')
    print(f'{key.tl}    {key.tr}')
    print(f'{key.tl}    {key.tr}')
    print(f' {key.m*4} ')
    print(f'{key.bl}    {key.br}')
    print(f'{key.bl}    {key.br}')
    print(f' {key.b*4} ')

def lookup_by_value(where):
    def lookup_(what):
        return next(k for k, v in where.items() if what == v)
    return lookup_

def find_in_arr(arr):
    def find_(function):
        return next(x for x in arr if function(x))
    return find_

def len_eq(num):
    def len_eq_(num_str):
        return len(num_str) == num
    return len_eq_

def main():
    with open(sys.argv[1]) as input_file:
        res = 0
        for line in input_file.readlines():
            #print("--------------")
            key = SimpleNamespace(**dict.fromkeys("t tl tr m bl br b".split(), '.'))
            in_digits, out_digits = line.strip().split('|')
            in_digits = in_digits.split()
            out_digits = out_digits.split()
            #print(f'to decipher: {out_digits}')

            counter = Counter(''.join(in_digits))
            #print(counter)
            lookup = lookup_by_value(counter)
            key.bl = lookup(4)
            key.br = lookup(9)
            key.tl = lookup(6)
            #print_digit(key)

            one = set(find_in_arr(in_digits)(len_eq(2)))
            one.remove(key.br)
            (key.tr, ) = one
            seven = set(find_in_arr(in_digits)(len_eq(3)))
            seven.difference_update({key.br, key.tr})
            (key.t, ) = seven
            four = set(find_in_arr(in_digits)(len_eq(4)))
            four.difference_update({key.br, key.tr, key.tl})
            (key.m, ) = four
            #print_digit(key)

            #print(counter)
            #print(key.__dict__.values())
            key.b = next(c for c in counter.keys() if c not in key.__dict__.values())
            #print_digit(key)

            signals2digit = {
                    frozenset([key.t, key.tl, key.tr, key.bl, key.br, key.b]): "0",
                    frozenset([key.tr, key.br]): "1",
                    frozenset([key.t, key.tr, key.m, key.bl, key.b]): "2",
                    frozenset([key.t, key.tr, key.m, key.br, key.b]): "3",
                    frozenset([key.tl, key.tr, key.m, key.br]): "4",
                    frozenset([key.t, key.tl, key.m, key.br, key.b]): "5",
                    frozenset([key.t, key.tl, key.m, key.bl, key.br, key.b]): "6",
                    frozenset([key.t, key.tr, key.br]): "7",
                    frozenset([key.t, key.tl, key.tr, key.m, key.bl, key.br, key.b]): "8",
                    frozenset([key.t, key.tl, key.tr, key.m, key.br, key.b]): "9"
                    }
            deciphered = int(''.join(signals2digit[frozenset(d)] for d in out_digits))
            print(deciphered)
            res += deciphered


            #known = [len(d) for d in out_digits if len(d) in len2digit]
            #res += len(known)
        print(f"answer is {res}")



if __name__ == "__main__":
    main()

