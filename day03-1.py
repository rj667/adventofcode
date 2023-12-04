#!/usr/bin/env python3

import sys
import time

t0 = time.perf_counter()

infile = sys.argv[0].split('-')[0] + '.example.txt'

schematic = []
total = 0
with open(infile, 'r') as input:
    y = 0
    for line in input:
        schematic.append(line.rstrip())
        for x, char in enumerate(schematic[-1]):
            if char != '.':
                if x > 1:
                    print(schematic[y][x-1])
                if y > 1:
                    if x > 1:
                        print(schematic[y-1][x-1])
                    print(schematic[y-1][x])
                    print(schematic[y-1][x+1])
        y += 1

print(schematic)

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
