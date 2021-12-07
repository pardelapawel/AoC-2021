#!/bin/python
import sys

def stringify(num):
    if isinstance(num, bool):
        if num:
            return "X"
        else:
            return "_"
    return str(num)

def is_bingo(bingo, row, col):
    return all(bingo[row]) or all([x[col] for x in bingo])

def main():
    with open(sys.argv[1]) as input_file:
        def str2int(arr):
            return [int(x) for x in arr]

        def print_bingos(matrix=None):
            if matrix is None:
                matrix = bingos
            for row in range(len(matrix[0])):
                print("|", "|\t|".join([' '.join([f'{stringify(n).rjust(2, " ")}' for n in bingo[row]]) for bingo in matrix]), "|")

        drawed = str2int(input_file.readline().strip().split(','))
        input_file.readline()
        bingos = []
        bingo = []
        markers = []
        marker = []
        num_map = {}
        counter = 0
        row = 0
        for line in input_file.readlines():
            line = str2int(line.strip().split())
            if not line:
                markers.append([[False]*len(bingo) for i in range(len(bingo))])
                bingos.append(bingo)
                bingo = []
                counter += 1
                row = 0
                continue
            bingo.append(line)
            for col, n in enumerate(line):
                n_coord = num_map.setdefault(n, [])
                n_coord.append((counter, row, col))
            row += 1
        print(num_map)
        print(drawed)
        print_bingos()
        print_bingos(markers)

        got_bingo = False
        playable_bingos = set(range(len(bingos)))
        for num in drawed:
            #candidates = num_map[num]
            #for bingo in [markers[x[0]] for x in candidates]
            print(f"  mark {num}")
            for bingo_num, row, col in num_map[num]:
                if bingo_num not in playable_bingos:
                    continue
                print(f"    marking in bingo {bingo_num}, {row}x{col}")
                markers[bingo_num][row][col] = True
                if is_bingo(markers[bingo_num], row, col):
                    print(f'Bingo in {bingo_num}')
                    playable_bingos.remove(bingo_num)
                    if len(playable_bingos) == 0:
                        unmarked = sum([sum([c for ci, c in enumerate(r) if not markers[bingo_num][ri][ci]]) for ri, r in enumerate(bingos[bingo_num])])
                        got_bingo = True
                        break
            if got_bingo:
                break
        print_bingos(markers)
        print(unmarked, num, unmarked*num)




if __name__ == "__main__":
    main()

