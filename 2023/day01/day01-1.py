#!/usr/bin/env python3

import sys
import time

t0 = time.perf_counter()

infile = sys.argv[0].split('-')[0] + '.input.txt'

total = 0
with open(infile, 'r') as input:
    for line in input:
        digits = list(filter(str.isdigit, line))
        number = int(digits[0] + digits[-1])
        total += number

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
