#!/bin/python
import sys
from collections import namedtuple
Point = namedtuple('Point', 'x y')

def print_grid(points, fold_direction=None, edge=None):
    def draw_point(x, y, edge=None):
        if edge is not None:
            return "|"
        if Point(x, y) in points:
            return "#"
        else:
            return '.'
    points = set(points)
    max_x = max([x for x, y in points]) + 1
    max_y = max([y for x, y in points]) + 1
    grid = [[False]*max_x for _ in range(max_y)]
    padding = 1
    print("  " + (" "*(padding-1)), ''.join([str(n).ljust(padding) for n in range(max_x)]))
    for y in range(max_y):
        row = str(y).rjust(2) + " "
        if fold_direction == 'y' and edge == y:
            row += '='*max_x*padding
        if fold_direction == 'x':
            row += (' '*(padding-1)).join([draw_point(x, y, edge) for x in range(max_x)])
        else:
            row += (' '*(padding-1)).join([draw_point(x, y) for x in range(max_x)])
        print(row)


def main():
    with open(sys.argv[1]) as input_file:
        points = []
        folds = []
        for line in input_file.readlines():
            line = line.strip()
            if not line:
                continue
            if line.startswith("fold"):
                fold, num = line.split('=')
                direction = fold[-1]
                folds.append((direction, int(num)))
                continue
            x, y = [int(n) for n in line.split(',')]
            points.append(Point(x,y))
        #print(points)
        print(folds)
        max_x = max([x for x, y in points]) + 1
        max_y = max([y for x, y in points]) + 1
        print(max_x, max_y)
        print_grid(points)
        for direction, edge in folds:
            if direction == 'y':
                fold_map = dict(zip(range(edge, max_y + 1), range(edge, -1, -1)))
            if direction == 'x':
                fold_map = dict(zip(range(edge, max_x + 1), range(edge, -1, -1)))
            print(f'Fold along {direction} -> {edge}')
            print(fold_map)
            #print_grid(points, direction, edge)
            new_points = set()
            for x, y in points:
                if direction == 'y':
                    if y < edge:
                        new_points.add(Point(x, y))
                    else:
                        new_points.add(Point(x, fold_map[y]))
                if direction == 'x':
                    if x < edge:
                        new_points.add(Point(x, y))
                    else:
                        new_points.add(Point(fold_map[x], y))
            points = new_points
            print_grid(points)
            print(f'num of points: {len(points)}')




if __name__ == "__main__":
    main()

