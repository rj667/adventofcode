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
    #puzzle = [list(line.strip()) for line in file]
    puzzle = [[char for char in line.strip()] for line in file]

for y, line in enumerate(puzzle):
    for x, char in enumerate(puzzle[y]):
        if puzzle[y][x] == 'A':
            if y-1 >= 0 and x-1 >= 0 and y+1 < len(puzzle) and x+1 < len(puzzle[y]):
                letters1 = puzzle[y-1][x-1] + puzzle[y+1][x+1]
                letters2 = puzzle[y-1][x+1] + puzzle[y+1][x-1]
                if sorted(letters1) == sorted(letters2) == ['M', 'S']:
                    total += 1

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
