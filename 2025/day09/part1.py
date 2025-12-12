#!/usr/bin/env python3

import sys
import time
from pprint import pprint

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
with open(infile, 'r') as file:
    data = [tuple(map(int, line.strip().split(","))) for line in file]

seen_tiles = []
largest_area = 0
for tile in data:
    for seen in seen_tiles:
        area = (abs(tile[0]-seen[0])+1)*(abs(tile[1]-seen[1])+1)
        if largest_area < area:
            largest_area = area
    seen_tiles.append(tile)
total = largest_area

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
