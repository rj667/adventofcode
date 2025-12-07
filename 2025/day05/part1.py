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
    available = list(map(int, data[data.index('')+1:]))

for a in available:
    for r in ranges:
        start, end = map(int, r.split('-'))
        if start <= a <= end:
            #print(f"{a} is in range {r}")
            total += 1
            break

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
