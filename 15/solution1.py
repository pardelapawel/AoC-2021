#!/bin/python
import sys
from queue import PriorityQueue
from termcolor import colored

INF = 999999

def dijskra(grid):


    return dist, prev


def main():
    def get_neigbour(sourcex, sourcey):
        #for h, v in [(-1, -1), (-1, 0), (-1, 1), ( 0, -1), ( 0, 1), ( 1, -1), ( 1, 0), ( 1, 1)]:
        for h, v in [(-1, 0), (1, 0), ( 0, -1), (0, 1)]:
            x = sourcex + h
            y = sourcey + v
            if x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0]):
                yield x, y, grid[x][y]
    def print_grid(px=None, py=None, trace=None):
        if trace is None:
            trace = []
        def colorize(x, y, num):

            point = (x, y)
            res = str(num).rjust(2)
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
            row = ' '.join([colorize(x, y, num) for y, num in enumerate(row)])
            print(row)

    grid = []
    with open(sys.argv[1]) as input_file:
        for line in input_file.readlines():
            row = [int(x) for x in line.strip()]
            grid.append(row)

        dist = {}
        prev = {}
        q = []
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                point = (x, y)
                dist[point] = INF
                prev[point] = None
                q.append(point)
        dist[(0,0)] = 0

        c = 0
        while q:
            idx = q.index(min(q, key=dist.get))
            u = q.pop(idx)
            #u_risk = grid[u[0], u[1]]

            neighbours = list(get_neigbour(u[0], u[1]))
            #print(neighbours)
            c += 1
            if c == 100:
                print_grid(u[0], u[1], trace=[(x[0], x[1]) for x in neighbours])
                c = 0

            for x, y, risk in neighbours:
                alt = dist[(u[0], u[1])] + risk
                if alt < dist[(x, y)]:
                    #print(f'{alt} < {dist[(x, y)]}')
                    dist[(x, y)] = alt
                    prev[(x, y)] = u
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

