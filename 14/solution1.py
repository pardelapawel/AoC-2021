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


        for step in range(10):
            quantity = {template[0]: 1}
            new_template = template[0]
            print(step, len(template))
            for i in range(len(template) - 1):
                left = template[i]
                right = template[i+1]
                mid = rules.get(left + right, "")
                new_template += mid + right
                quantity[right] = quantity.setdefault(right, 0) + 1
                if mid:
                    quantity[mid] = quantity.setdefault(mid, 0) + 1
            template = new_template
            #print(template, len(template))
            print(quantity)
            print(max(quantity.values()) - min(quantity.values()))



if __name__ == "__main__":
    main()

