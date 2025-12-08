#!/usr/bin/env python3

import sys
import time
from pprint import pprint

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
with open(infile, 'r') as file:
    #data = [line.rstrip("\n") for line in file]
    #data = [list(map(str, line.split())) for line in file]
    grid = [list(line.strip()) for line in file]

def print_grid():
    for y in range(len(grid)):
        print(''.join(grid[y]))
    print()

print_grid()

for y in range(len(grid)-1):
    for x in range(len(grid[y])):
        if grid[y][x] == "S":
            grid[y+1][x] = "|"
        if grid[y][x] == "|":
            if grid[y+1][x] == "^":
                grid[y+1][x-1] = "|"
                grid[y+1][x+1] = "|"
                total += 1
            else:
                grid[y+1][x] = "|"
print_grid()

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
