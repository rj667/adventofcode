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
        #vertical_board = list(map(list, zip(*horizontal_board)))
        #boards.extend((horizontal_board, vertical_board))
        boards.append(horizontal_board)

boards_with_bingo = set({})
for number in drawn:
    print(f'DRAW: {number}')
    for i in range(len(boards)):
        if i in boards_with_bingo: continue
        board = boards[i]
        bingo = False
        for row in board:
            try:
                row[row.index(number)] = marker
                print(f'found {number} in {board}')
            except ValueError:
                pass
            if ''.join(map(str, row)) == marker * boardsize:
                bingo = True
        for col in list(map(list, zip(*board))):
            if ''.join(map(str, col)) == marker * boardsize:
                bingo = True
        if bingo:
            score = sum(list(filter(lambda x: x != marker, sum(board, [])))) * number
            print(f'{score} is the score')
            if len(boards_with_bingo) == len(boards) - 1:
                sys.exit()
            else:
                boards_with_bingo.add(i)
                print(boards_with_bingo)
