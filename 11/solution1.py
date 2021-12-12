#!/bin/python
import sys
from termcolor import colored

def colour(num):
    if num < 0:
        return colored(str(num).rjust(2), 'red')
    if num == 0:
        return colored(str(num).rjust(2), 'cyan')
    return str(num).rjust(2)


def main():

    def print_grid():
        for row in grid:
            print(' '.join([colour(cell) for cell in row]))

    def pass_energy(x, y):
        #out of bounds
        if x < 0 or x > border_right:
            return 0
        if y < 0 or y > border_bottom:
            return 0

        # already flashed
        if grid[x][y] == 0:
            return 0

        grid[x][y] += 1
        if grid[x][y] > 9:
            flash_queue.append((x, y))
            grid[x][y] = 0
            return 1
        return 0

    with open(sys.argv[1]) as input_file:
        grid = [[int(num) for num in row.strip()] for row in input_file.readlines()]
        print_grid()
        flash_queue = [] #queue of things to flash and modify neightbours (x,y)
        border_bottom = len(grid) -1
        border_right = len(grid[0]) -1
        flash_counter = 0
        for stepno in range(100):
            # add_one
            for x, row in enumerate(grid):
                for y, cell in enumerate(row):
                    row[y] += 1
                    if row[y] > 9:
                        flash_queue.append((x, y))
                        row[y] = 0
                        flash_counter += 1
            while flash_queue:
                x, y = flash_queue.pop()
                flash_counter += pass_energy(x + (-1), y + (-1))
                flash_counter += pass_energy(x + (-1), y + (0))
                flash_counter += pass_energy(x + (-1), y + (1))
                flash_counter += pass_energy(x + (0),  y + (-1))
                flash_counter += pass_energy(x + (0),  y + (1))
                flash_counter += pass_energy(x + (1),  y + (-1))
                flash_counter += pass_energy(x + (1),  y + (0))
                flash_counter += pass_energy(x + (1),  y + (1))



            print(f'Step {stepno}')
            print_grid()
        print(flash_counter)




if __name__ == "__main__":
    main()

