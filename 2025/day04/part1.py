#!/usr/bin/env python3

import sys
import time
from pprint import pprint

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
with open(infile, 'r') as file:
    grid = [list(line.strip()) for line in file]

def print_grid():
    for y in range(len(grid)):
        print(''.join(grid[y]))
    print()

roll = "@"
removed = "x"
empty = "."

print_grid()
for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] != roll:
            continue
        surrounding_rolls = 0
        if y > 0 and x > 0:
            if grid[y-1][x-1] != empty:
                surrounding_rolls += 1
        if y > 0:
            if grid[y-1][x] != empty:
                surrounding_rolls += 1
        if y > 0 and x < len(grid[y]) - 1:
            if grid[y-1][x+1] != empty:
                surrounding_rolls += 1
        if x > 0:
            if grid[y][x-1] != empty:
                surrounding_rolls += 1
        if x < len(grid[y]) - 1:
            if grid[y][x+1] != empty:
                surrounding_rolls += 1
        if y < len(grid) - 1 and x > 0:
            if grid[y+1][x-1] != empty:
                surrounding_rolls += 1
        if y < len(grid) - 1:
            if grid[y+1][x] != empty:
                surrounding_rolls += 1
        if y < len(grid) - 1 and x < len(grid[y]) - 1:
            if grid[y+1][x+1] != empty:
                surrounding_rolls += 1
        if surrounding_rolls < 4:
            total += 1
            grid[y][x] = removed

print_grid()

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
