#!/bin/python
import sys

def stringify(num):
    if isinstance(num, bool):
        if num:
            return "X"
        else:
            return "_"
    return str(num)

def is_bingo(sudoku, row, col):
    return all(sudoku[row]) or all([x[col] for x in sudoku])

def main():
    with open(sys.argv[1]) as input_file:
        def str2int(arr):
            return [int(x) for x in arr]

        def print_sudokus(matrix=None):
            if matrix is None:
                matrix = sudokus
            for row in range(len(matrix[0])):
                print("|", "|\t|".join([' '.join([f'{stringify(n).rjust(2, " ")}' for n in sudoku[row]]) for sudoku in matrix]), "|")

        drawed = str2int(input_file.readline().strip().split(','))
        input_file.readline()
        sudokus = []
        sudoku = []
        markers = []
        marker = []
        num_map = {}
        counter = 0
        row = 0
        for line in input_file.readlines():
            line = str2int(line.strip().split())
            if not line:
                markers.append([[False]*len(sudoku) for i in range(len(sudoku))])
                sudokus.append(sudoku)
                sudoku = []
                counter += 1
                row = 0
                continue
            sudoku.append(line)
            for col, n in enumerate(line):
                n_coord = num_map.setdefault(n, [])
                n_coord.append((counter, row, col))
            row += 1
        print(num_map)
        print(drawed)
        print_sudokus()
        print_sudokus(markers)

        got_bingo = False
        for num in drawed:
            #candidates = num_map[num]
            #for sudoku in [markers[x[0]] for x in candidates]
            print(f"mark {num}")
            for sudoku_num, row, col in num_map[num]:
                print(f"  marking in sudoku {sudoku_num}, {row}x{col}")
                markers[sudoku_num][row][col] = True
                if is_bingo(markers[sudoku_num], row, col):
                    print(f'Bingo in {sudoku_num}')
                    unmarked = sum([sum([c for ci, c in enumerate(r) if not markers[sudoku_num][ri][ci]]) for ri, r in enumerate(sudokus[sudoku_num])])
                    got_bingo = True
                    break
            if got_bingo:
                break
        print_sudokus(markers)
        print(unmarked, num, unmarked*num)




if __name__ == "__main__":
    main()

