#!/usr/bin/env python3

import sys
import time
import re
from operator import mul

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
with open(infile, 'r') as file:
    memory = file.read()

enabled = True
seen = ''
for c in memory:
    seen += c
    if c == ')':
        if seen.endswith('do()'):
            enabled = True
        if seen.endswith('don\'t()'):
            enabled = False
        if match := re.search(r'mul\((\d{1,3}),(\d{1,3})\)$', seen):
            if enabled:
                total += mul(*map(int, match.group(1, 2)))

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
