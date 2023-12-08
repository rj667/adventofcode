#!/usr/bin/env python3

import sys
import time
from pprint import pprint

try:
    infile = sys.argv[1]
except IndexError:
    infile = sys.argv[0].split('-')[0] + '.input.txt'

t0 = time.perf_counter()

schematic = []
total = 0

with open(infile, 'r') as input:
    y = 0
    for line in input:
        print(f'{line.rstrip()}')
        schematic.append(line.rstrip())
        for x, char in enumerate(schematic[y]):
            pass
        y += 1

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
