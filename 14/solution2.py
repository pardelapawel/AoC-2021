#!/bin/python
import sys
from collections import defaultdict

def main():
    with open(sys.argv[1]) as input_file:
        template = input_file.readline().strip()
        input_file.readline()
        rules = {}
        for line in input_file.readlines():
            left, right = line.strip().split(' -> ')
            rules[left] = right

        print(template)
        pairs = defaultdict(int)
        for i in range(len(template) - 1):
            left = template[i]
            right = template[i+1]
            pairs[left+right] += 1
        print(pairs)

        for step in range(40):
            print(f'Step {step}')
            new_pairs = defaultdict(int)
            quantity = defaultdict(int)
            quantity[template[0]] += 1
            for pair, count in pairs.items():
                print(f'processing {pair} with count {count}')
                if pair in rules:
                    mid = rules[pair]
                    new_pairs[pair[0] + mid] += count
                    new_pairs[mid + pair[1]] += count
                    quantity[mid] += count
                    quantity[pair[1]] += count
                else:
                    new_pairs[pair] += count
            pairs = new_pairs.copy()
            print(pairs)
            print(quantity)
            print(max(quantity.values()) - min(quantity.values()))




if __name__ == "__main__":
    main()

