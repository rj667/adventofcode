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
    plan = [list(line.strip()) for line in file]

for row in plan:
    print(''.join(row))

for y, line in enumerate(plan):
    for x, char in enumerate(plan[y]):
        if plan[y][x] in list('^>v<'):
            g = plan[y][x]
            break
    else:
        continue
    break

print(y, x, g)

while True:
    match g:
        case '^':
            next_y = y-1
            next_x = x
            next_g = '>'
        case '>':
            next_y = y
            next_x = x+1
            next_g = 'v'
        case 'v':
            next_y = y+1
            next_x = x
            next_g = '<'
        case '<':
            next_y = y
            next_x = x-1
            next_g = '^'
    if next_y < 0 or next_x < 0 or next_y >= len(plan) or next_x >= len(plan[next_y]):
        if plan[y][x] != 'X':
            plan[y][x] = 'X'
            total += 1
        break
    if plan[next_y][next_x] == '#':
        g = next_g
    else:
        if plan[y][x] != 'X':
            plan[y][x] = 'X'
            total += 1
        y = next_y
        x = next_x
    print(y,x,g)

for row in plan:
    print(''.join(row))

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
