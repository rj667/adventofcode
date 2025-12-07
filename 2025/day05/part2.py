#!/usr/bin/env python3

import sys
import time
from pprint import pprint

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
with open(infile, 'r') as file:
    data = [line.strip() for line in file]
    input_ranges = data[:data.index('')]

while True:
    merged_ranges = []
    for ir in input_ranges:
        if isinstance(ir, str):
            ir = list(map(int, ir.split('-')))
        for mr in merged_ranges:
            if ir[0] <= mr[1] and mr[0] <= ir[1]:
                mr[0] = min(ir[0], mr[0])
                mr[1] = max(ir[1], mr[1])
                break
        else:
            merged_ranges.append(ir)
            continue
    if merged_ranges == input_ranges:
        break
    input_ranges = merged_ranges

for mr in merged_ranges:
    total += mr[1] - mr[0] +1

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
