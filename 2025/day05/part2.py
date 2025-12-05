#!/usr/bin/env python3

import sys
import time
from pprint import pprint

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
with open(infile, 'r') as file:
    data = [line.strip() for line in file]
    ranges = data[:data.index('')]
pprint(ranges)

aggregated_ranges = []
for r in ranges:
    start, end = map(int, r.split('-'))
    for ar in aggregated_ranges:
        if not (end < ar[0] or start > ar[1]):
            ar[0] = min(ar[0], start)
            ar[1] = max(ar[1], end)
            continue


    pprint(newranges)

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
