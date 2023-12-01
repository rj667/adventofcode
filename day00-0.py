#!/usr/bin/env python3

import sys
import time

t0 = time.time()

infile = sys.argv[0].split('-')[0] + '.input.txt'

total = 0
with open(infile, 'r') as input:
    for line in input:
        print(line, end='')

t1 = time.time()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
