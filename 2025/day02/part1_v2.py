#!/usr/bin/env python3

import sys
import time
from pprint import pprint
import re

t0 = time.perf_counter()

infile = sys.argv[1:] and sys.argv[1] or "input.txt"

total = 0
with open(infile, 'r') as file:
    data = file.read().rstrip().split(',')

print(data)
for range_str in data:
    start, end = map(int, range_str.split('-'))
    for id in range(start, end + 1):
        id_str = str(id)
        if match := re.search(r'^(\d*?)\1$', id_str):
            #print(match.group(0))
            total += id

t1 = time.perf_counter()
print(f"Answer: {total}")
print(f"Execution time: {t1 - t0:.6f} seconds")
