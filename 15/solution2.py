#!/bin/python
import sys
from heapdict import heapdict
from termcolor import colored

INF = 999999

def main():
    def increase_risk(num, i):
        if num + i > 9:
            return num+i - 9
        else:
            return num + i

    def get_neigbour(sourcex, sourcey):
        #for h, v in [(-1, -1), (-1, 0), (-1, 1), ( 0, -1), ( 0, 1), ( 1, -1), ( 1, 0), ( 1, 1)]:
        for h, v in [(-1, 0), (1, 0), ( 0, -1), (0, 1)]:
            x = sourcex + h
            y = sourcey + v
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                yield x, y, grid[x][y]

    def print_grid(px=None, py=None, trace=None):
        return
        if trace is None:
            trace = []
        def colorize(x, y, num):
            #return(str(num))
            point = (x, y)
            res = str(num).rjust(1)
            if point in trace:
                return colored(res, 'magenta')
            if px is not None and py is not None:
                if x == px and y == py:
                    return colored(res, 'red')
            attrs = []
            if dist[point] is not None:
                attrs.append('bold')
            if dist[point] < INF:
                res = colored(res, 'blue', attrs=attrs)
            return res

        if px is not None and py is not None:
            print(f'==({px}, {py})==')
        else:
            print('-'*len(grid[0])*3)
        for x, row in enumerate(grid):
            row = ''.join([colorize(x, y, num) for y, num in enumerate(row)])
            print(row)

    grid = []
    with open(sys.argv[1]) as input_file:
        for line in input_file.readlines():
            int_line = [int(x) for x in line.strip()]
            row = int_line.copy()
            row += [increase_risk(x, 1) for x in int_line]
            row += [increase_risk(x, 2) for x in int_line]
            row += [increase_risk(x, 3) for x in int_line]
            row += [increase_risk(x, 4) for x in int_line]
            grid.append(row)
        grid_copy = grid.copy()
        for g in range(1, 5):
            for row in range(len(grid_copy)):
                row = [increase_risk(x, g) for x in grid_copy[row]]
                grid.append(row)


        dist = {}
        prev = {}
        q = heapdict()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                point = (x, y)
                dist[point] = INF
                prev[point] = None
                q[point] = INF
        dist[(0,0)] = 0
        q[point] = 0
        print_grid()

        c = 0
        while len(q):
            u, d = q.popitem()

            neighbours = list(get_neigbour(u[0], u[1]))
            #print(neighbours)
            c += 1
            if c == 100:
                print_grid(u[0], u[1], trace=[(x[0], x[1]) for x in neighbours])
                c = 0

            for x, y, risk in neighbours:
                alt = dist[(u[0], u[1])] + risk
                point = (x, y)
                if alt < dist[point]:
                    #print(f'{alt} < {dist[(x, y)]}')
                    dist[point] = alt
                    prev[point] = u
                    q[point] = alt
        #print(dist)
        #print(prev)
        u = (len(grid)-1, len(grid[0])-1)
        trace = []
        while u:
            trace.append(u)
            u = prev[u]
        trace = trace[:-1]
        print(trace)
        print(sum([grid[x][y] for x, y in trace]))
        print_grid(trace=trace)



if __name__ == "__main__":
    main()

