#!/bin/python
import sys

def main():
    with open(sys.argv[1]) as input_file:
        def str2int(arr):
            return [int(x) for x in arr]

        def print_sudokus():
            for row in range(len(sudokus[0])):
                print("\t".join([' '.join([f'{str(n).rjust(2, " ")}' for n in sudoku[row]]) for sudoku in sudokus]))

        drawed = str2int(input_file.readline().strip().split(','))
        input_file.readline()
        sudokus = []
        sudoku = []
        for line in input_file.readlines():
            line = str2int(line.strip().split())
            if not line:
                sudokus.append(sudoku)
                sudoku = []
                continue
            sudoku.append(line)
        print(drawed)
        print_sudokus()
if __name__ == "__main__":
    main()

