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
        for x in map(str, grid[y]):
            print(f"{x:>3}", end="")
        print()
    print()

#print_grid()

for y in range(len(grid)-1):
    for x in range(len(grid[y])):
        if grid[y][x] == "S":
            grid[y+1][x] = 1
        if type(grid[y][x]) == int:
            if grid[y+1][x] == "^":
                # left split
                if not type(grid[y+1][x-1]) == int:
                    grid[y+1][x-1] = 0
                grid[y+1][x-1] += grid[y][x]
                # right split
                if not type(grid[y+1][x+1]) == int:
                    grid[y+1][x+1] = 0
                grid[y+1][x+1] += grid[y][x]
            else:
                # no split
                if not type(grid[y+1][x]) == int:
                    grid[y+1][x] = 0
                grid[y+1][x] += grid[y][x]
#print_grid()

for x in range(len(grid[-1])):
    if type(grid[-1][x]) == int:
        total += grid[-1][x]

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
