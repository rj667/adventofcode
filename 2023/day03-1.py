#!/usr/bin/env python3

import sys
import time

# This solution reads the input lines and adds dots around the borders.
# Then it loops over the lines char-by-char. If that is a digit, it saves
# it to the current number and checks the 8 surrounding fields for a symbol.
# If not, then the current number is complete and will be counted if it
# has a an adjacent symbol.

try:
    infile = sys.argv[1]
except IndexError:
    infile = sys.argv[0].split('-')[0] + '.input.txt'

t0 = time.perf_counter()

total = 0

with open(infile, 'r') as input:
    data = ['.' + line.rstrip() + '.' for line in input]
data.insert(0, '.' * len(data[0]))
data.append('.' * len(data[0]))

number = ''
symbol_adjacent = False
for y in range(1, len(data) -1):
    for x in range(1, len(data[0])):
        if data[y][x].isdigit():
            number += data[y][x]
            if symbol_adjacent:
                continue
            for dy,dx in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                if not data[y+dy][x+dx].isdigit() and not data[y+dy][x+dx] == '.':
                    symbol_adjacent = True
        else:
            if number:
                if symbol_adjacent:
                    total += int(number)
                number = ''
                symbol_adjacent = False

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
