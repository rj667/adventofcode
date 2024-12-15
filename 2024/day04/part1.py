#!/usr/bin/env python3

import sys
import time
from pprint import pprint

try:
    infile = sys.argv[1]
except IndexError:
    infile = sys.argv[0].split('-')[0] + '.input.txt'

t0 = time.perf_counter()

total = 0
with open(infile, 'r') as file:
    puzzle = [[char for char in line.strip()] for line in file]

for y, line in enumerate(puzzle):
    for x, char in enumerate(puzzle[y]):
        if puzzle[y][x] == 'X':
            # →
            if x+3 < len(puzzle[y]):
                if puzzle[y][x+1] + puzzle[y][x+2] + puzzle[y][x+3] == 'MAS':
                    total += 1
            # 🡦
            if y+3 < len(puzzle) and x+3 < len(puzzle[y]):
                if puzzle[y+1][x+1] + puzzle[y+2][x+2] + puzzle[y+3][x+3] == 'MAS':
                    total += 1
            # 🡣
            if y+3 < len(puzzle):
                if puzzle[y+1][x] + puzzle[y+2][x] + puzzle[y+3][x] == 'MAS':
                    total += 1
            # 🡧
            if y+3 < len(puzzle) and x-3 >= 0:
                if puzzle[y+1][x-1] + puzzle[y+2][x-2] + puzzle[y+3][x-3] == 'MAS':
                    total += 1
            # 🡠
            if x-3 >= 0:
                if puzzle[y][x-1] + puzzle[y][x-2] + puzzle[y][x-3] == 'MAS':
                    total += 1
            if y-3 >= 0 and x-3 >= 0:
                if puzzle[y-1][x-1] + puzzle[y-2][x-2] + puzzle[y-3][x-3] == 'MAS':
                    total += 1
            # 🡡
            if y-3 >= 0:
                if puzzle[y-1][x] + puzzle[y-2][x] + puzzle[y-3][x] == 'MAS':
                    total += 1
            # 🡥
            if y-3 >= 0 and x+3 < len(puzzle[y]):
                if puzzle[y-1][x+1] + puzzle[y-2][x+2] + puzzle[y-3][x+3] == 'MAS':
                    total += 1

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
