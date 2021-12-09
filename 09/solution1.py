#!/bin/python
import sys
from functools import lru_cache

def intify(arr):
    return [int(x) for x in arr]

def stringify(foo):
    if isinstance(foo, bool):
        if foo:
            return "T"
        else:
            return "F"
    return str(foo)

def main():
    def print_grid(matrix=None):
        if matrix is None:
            matrix = grid
        for row in matrix:
            print(' '.join([stringify(cell).rjust(2) for cell in row]))

    with open(sys.argv[1]) as input_file:
        grid = [intify(line.strip()) for line in input_file.readlines()]
        low_points = [['.']*len(grid[0]) for _ in grid]
        border_right = len(grid[0]) - 1
        border_bottom = len(grid) - 1
        print_grid()
        print()
        print_grid(low_points)
        risk = 0
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                cells_to_check = set()
                print(f'checking {x} {y} = {cell} borders = {border_right} {border_bottom}')
                if x != 0:
                    print(f'  1adding grid[{x-1}][{y}] ')
                    cells_to_check.add(grid[x-1][y])
                if x != border_bottom:
                    print(f'  2adding grid[{x+1}][{y}] ')
                    cells_to_check.add(grid[x+1][y])
                if y != 0:
                    print(f'  3adding grid[{x}][{y-1}] ')
                    cells_to_check.add(grid[x][y-1])
                if y != border_right:
                    print(f'  4adding grid[{x}][{y+1}] ')
                    cells_to_check.add(grid[x][y+1])
                print(f'check {cell} against {cells_to_check}')
                if cell < min(cells_to_check):
                    low_points[x][y] = cell + 1
                    risk += cell + 1
            print_grid()
            print_grid(low_points)
            print(risk)



if __name__ == "__main__":
    main()

