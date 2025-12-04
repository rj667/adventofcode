#!/usr/bin/env python3
import sys
infile = sys.argv[0].split('part')[0] + '.input'

class Bingo(Exception):
    pass

boards = []
boardsize = 5
marker = 'X'
scores = []

with open(infile, 'r') as input:
    drawn = list(map(int, input.readline().split(',')))
    while True:
        if input.readline() == '': break
        horizontal_board = []
        for i in range(boardsize):
            row = list(map(int, input.readline().split()))
            horizontal_board.append(row)
        vertical_board = list(map(list, zip(*horizontal_board)))
        boards.extend((horizontal_board, vertical_board))

for number in drawn:
    for board in boards:
        try:
            for row in board:
                try:
                    row[row.index(number)] = marker
                except ValueError:
                    pass
                if ''.join(map(str, row)) == marker * boardsize:
                    raise Bingo
        except Bingo:
            score = sum(list(filter(lambda x: x != marker, sum(board, [])))) * number
            print(f'{score} is the final score of the first board to win')
            sys.exit()

