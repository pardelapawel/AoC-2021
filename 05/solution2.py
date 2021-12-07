#!/bin/python
import sys

def main():
    def num2str(num):
        if num == 0:
            return "."
        else:
            return str(num)
    def print_grid():
        for row in grid:
            print("\t", ' '.join([num2str(n) for n in row]))
    with open(sys.argv[1]) as input_file:
        grid = [[]]
        max_width = 1
        max_height = 1
        for line in input_file.readlines():
            start, _, end = line.strip().split()
            xs, ys = [int(n) for n in start.split(',')]
            xe, ye = [int(n) for n in end.split(',')]
            print('> ', xs, ys, xe, ye)
            #print_grid()
            if ys > max_height or ye > max_height:
                print(f'expanding height {ys} or {ye} > {max_height}')
                new_height = max(ys, ye) + 1
                grid.extend([[0]*len(grid[0]) for _ in range(new_height - max_height)])
                max_height = new_height
                #print_grid()
            if xs > max_width or xe > max_width:
                print(f'expanding width {xs} or {xe} > {max_width}')
                new_width = max(xs, xe) + 1
                for idx in range(len(grid)):
                    grid[idx].extend([0]*(new_width - max_width + 1))
                max_width = new_width
                #print_grid()
            if xs == xe:
                left = min(ys, ye)
                right = max(ys, ye)
                for idx in range(left, right + 1):
                    grid[idx][xs] += 1
            elif ys == ye:
                left = min(xs, xe)
                right = max(xs, xe)
                for idx in range(left, right + 1):
                    grid[ys][idx] += 1
            else:
                if xs < xe:
                    x_range = list(range(xs,xe+1))
                else:
                    x_range = list(range(xs,xe-1, -1))
                if ys < ye:
                    y_range = list(range(ys,ye+1))
                else:
                    y_range = list(range(ys,ye-1, -1))
                for x, y in zip(x_range, y_range):
                    grid[y][x] += 1
        print()
        print_grid()
        print(sum([len([n for n in row if n > 1]) for row in grid]))




if __name__ == "__main__":
    main()

