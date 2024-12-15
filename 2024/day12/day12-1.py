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
    garden = ['.' + line.strip() + '.' for line in file]
    garden.insert(0, '.' * len(garden[0]))
    garden.append('.' * len(garden[0]))
    garden = [[[char, -1] for char in row] for row in garden]

pprint(garden)


regions = []
for y in range(1, len(garden)-1):
    for x in range(1, len(garden[y])-1):
        if garden[y][x][0] == garden[y][x-1][0]:
            garden[y][x][1] = garden[y][x-1][1]
        if garden[y][x][0] == garden[y-1][x][0]:
            garden[y][x][1] = garden[y-1][x][1]
    for x in reversed(list(range(1, len(garden[y])-1))):
        if garden[y][x-1][0] == garden[y][x][0]:
            garden[y][x-1][1] = garden[y][x][1]
        else:
            garden[y][x-1][1] = len(regions)+1
            regions.append('')
        print(f'{garden[y][x][0]},{garden[y][x][1]:02d} ', end='')
    print('')

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
