#!/bin/python
import sys
from functools import reduce

def intify(arr):
    return [int(x) for x in arr]

def stringify(foo):
    if isinstance(foo, bool):
        if foo:
            return "X"
        else:
            return "."
    return str(foo)

def main():
    def print_grid(matrix=None):
        if matrix is None:
            matrix = grid
        for row in matrix:
            print(' '.join([stringify(cell).rjust(2) for cell in row]))

    def check_spill(x, y):
        if grid[x][y] == 9:
            #visited[x][y] = grid[x][y]
            return 0
        if visited[x][y] != '.': # I tried just doing False, but it broke when cell value is 0; I want to print stuff, so we have this abbomination
            return 0
        visited[x][y] = grid[x][y]
        spill_size = 1
        if x != 0:
            spill_size += check_spill(x-1, y)
        if x != border_bottom:
            spill_size += check_spill(x+1, y)
        if y != 0:
            spill_size += check_spill(x, y-1)
        if y != border_right:
            spill_size += check_spill(x, y+1)
        return spill_size


    with open(sys.argv[1]) as input_file:
        grid = [intify(line.strip()) for line in input_file.readlines()]
        visited = [['.']*len(grid[0]) for _ in grid]
        border_right = len(grid[0]) - 1
        border_bottom = len(grid) - 1
        print_grid()
        print()
        print_grid(visited)
        basins = []
        for x, row in enumerate(grid):
            for y, cell in enumerate(row):
                if visited[x][y] == '.': # see long comment above
                    spill_size = check_spill(x, y)
                    if spill_size:
                        print(f" spill size is {spill_size} starting at {x} {y} = {cell}")
                        #print_grid(visited)
                        basins.append(spill_size)
        print(sorted(basins, reverse=True))
        print(reduce(lambda x,y: x*y, sorted(basins, reverse=True)[:3]))



if __name__ == "__main__":
    main()

